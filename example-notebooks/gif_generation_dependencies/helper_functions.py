import datetime
import os
import requests
import time

import folium
import numpy as np
from PIL import Image, ImageFont, ImageDraw
import rasterio
import rasterio.features

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from scipy.ndimage import binary_dilation


# Constants
STAC_API_URL = "https://staging-stac.delta-backend.com"
RASTER_API_URL = "https://staging-raster.delta-backend.com"

# Collection we'll be using to generate the GIF
collection = 'no2-monthly'

def get_image(item, geojson, image_format="tif", additional_args={}, image_height=512, image_width=512):

    response = requests.post(
        f"{RASTER_API_URL}/cog/crop", 
        params={
            "format": image_format,
            "height": image_height, 
            "width": image_width, 
            "url":item["assets"]["cog_default"]["href"],
            **additional_args
        },
        json=geojson
    ) 
    if not response.status_code == 200: 
        print(response.content)
        raise Exception
    return response.content

def overlay_geojson(image_filepath, geojson):
    with rasterio.open(image_filepath, "r+") as src:
        arr = src.read()
        
        # TODO: move validation logic higher up in the call stack
        if geojson["type"] == "FeatureCollection": 
            features = geojson["features"]
        elif geojson["type"] == "Feature": 
            features = [geojson]
        else: 
            raise Exception("Geojson to overlay must be either type Feature or FeatureCollection")
        
        for feature in geojson["features"]:
            mask = rasterio.features.rasterize(
                ((feature["geometry"], 255),),
                fill=0,
                out_shape=src.shape,
                transform=src.transform,
                all_touched=False
            )
            dilated = binary_dilation(mask, iterations=1).astype(mask.dtype)
            outer = dilated > mask 
            arr = np.where(outer, 255, arr)

        # WARNING: Overwriting file
        src.write(arr)
    return image_filepath

def overlay_raster_on_folium(image_filepath):
    # open with rasterio to get band data and bounds
    with rasterio.open(image_filepath) as dataset:

        [lon_min, lat_min, lon_max, lat_max] = list(dataset.bounds)

        data = dataset.read()

        # reshape data from 3 x 512 x 512 to RGB (512 x 512 x 3)
        data_reshaped = np.zeros((data.shape[1], data.shape[2], data.shape[0]), 'uint8')
        data_reshaped[...,0] = data[0]
        data_reshaped[...,1] = data[1]
        data_reshaped[...,2] = data[2]
        data_reshaped[...,3] = data[3]

        # create folium base map over which to display each frame of the gif
        m = folium.Map(
            location=[(lat_max-lat_min)/2+lat_min, (lon_max-lon_min)/2+lon_min],
            zoom_start=4,
            zoom_control=False
        )

        # Add RGB image as overlay to folium map object
        image_overlay = folium.raster_layers.ImageOverlay(
            image=data_reshaped, 
            bounds=[[lat_min,lon_min],[lat_max, lon_max]], 
            opacity=0.85
        )
        image_overlay.add_to(m)
    
    # use folium + selenium + geckodriver (webdriver) to convert folium HTML elements 
    # (which now contain both the base map and the overlayed raster data) to a png 
    # file and store locally
    html_filepath = image_filepath.replace(".tif", ".html")
    
    m.save(html_filepath)

    options = webdriver.ChromeOptions()
    options.headless=True
    driver = webdriver.Chrome(
        service=ChromeService(
            ChromeDriverManager(path="./gif_generation_dependencies/").install()
        ), 
        options=options
    )
    driver.set_window_size(400, 400)  # choose a resolution
    driver.get(f"file://{html_filepath}")
    time.sleep(2)
    driver.save_screenshot(image_filepath.replace(".tif", ".png"))

    return image_filepath.replace(".tif", ".png")

def overlay_date(image_filepath, datestring):
    
     # Open the PNG file with PIL 
    image = Image.open(image_filepath)
    
    # Load draw module to add date string to png frame 
    image_draw = ImageDraw.Draw(image)

    # set font and size for date string
    font = ImageFont.truetype("./gif_generation_dependencies/Gidole-Regular.ttf",size=45)
    
    
    # calculate text size for date string
    xs,ys = image_draw.textsize(datestring, font=font)

    # get image size to calculate date string position
    image_width, image_height=image.size

    # position date string background rectangle at in the lower left 
    # hand corner with a 5px boundary between background rectangle 
    # the datestring itself
    text_rectangle_top_left = (0,image_height-ys-15)

    # draw background rectangle
    image_draw.rectangle(
        [ 
            text_rectangle_top_left, 
            (text_rectangle_top_left[0] + xs + 15, text_rectangle_top_left[1] + ys + 15) 
        ], 
        fill=(255,255,255))

    # draw text over the background rectangle
    image_draw.text(tuple(i+5 for i in text_rectangle_top_left), datestring, (0,0,0), font=font)
    # Save output image
    image.save(image_filepath)
    
    return image_filepath


def generate_frame(
    item, 
    aoi, 
    dir_path, 
    image_format="png", 
    overlay=None, 
    additional_cog_crop_args={}, 
    image_height=512, 
    image_width=512
):
    if image_format=="png" and overlay is not None: 
        raise Exception("Unable to add overlay to png format image")
        
    datestring = datetime.datetime.strptime(
            item["properties"]["start_datetime"], "%Y-%m-%dT%H:%M:%S"
        ).date().isoformat()  
    
    # prepend datestring in filename so that we can sort the files by alphabetical order
    # when generating the GIF
    filepath = os.path.join(dir_path, "_".join([datestring, item["id"].replace(".nc", f".{image_format}")]))
    
    with open(filepath, "wb") as f: 
        f.write(
            get_image(
                item, 
                geojson=aoi, 
                image_format=image_format,
                additional_args= additional_cog_crop_args,
                image_height=image_height, 
                image_width=image_width
            )
        )
    if overlay is None: 
        return filepath
    
    if overlay=="folium": 
        overlay_raster_on_folium(filepath)
        # folium screenshots get saved as png
        filepath = filepath.replace(".tif", ".png")
    else: 
        if not isinstance(overlay, dict):
            # TODO: add check for geojson validity (ie: Feature/FeatureCollection "type" field, etc)
            raise Exception("Param: overlay must be a valid geojson dict")
        
        overlay_geojson(filepath, overlay)     
    
    overlay_date(filepath, datestring)
    
    return filepath 
