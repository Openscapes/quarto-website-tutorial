---
title: From Jupyter
---

Your Jupyter setup will involve `.ipynb` notebooks and the command line. You can interact with Quarto through JupyterLab or JupyterHub. [Quarto's JupyterLab tutorials](https://quarto.org/docs/get-started/hello/jupyter.html) has great instructions on getting started with JupyterLab, including computations and authoring.

This example uses the NASA-Openscapes JupyterHub that already has all python environments as well as Quarto installed.

## Setup JupyterHub

Our JupyterHub is already setup with python environments as well as Quarto (through [nasa-openscapes/corn](https://github.com/nasa-openscapes/corn)), so there is no further installation required.

### Clone your repo

You'll start by cloning your repository into JupyterHub. Do this by opening a terminal (File \> New \> Terminal). In the Terminal, `git clone` your repository and `cd` into it:

```{.bash}
git clone https://github.com/openscapes/quarto-website-tutorial
cd quarto-website-tutorial
```

## Quarto preview

Let's start off by previewing our quarto site locally. In Terminal, type `quarto preview`, which will provide a URL with a preview of our site!

```{.bash}
quarto preview
# Preparing to preview
# Watching files for changes
# Browse at https://openscapes.2i2c.cloud/user/jules32/proxy/4593/
```

Copy this URL into another browser window; and arrange them so you can see them both (I make a bit more space by collapsing the file menu by clicking on the file icon in the top left)

![](images/jupyter-side-by-side.png){fig-align="center"}

Now we'll be able to see live changes in the preview as we edit in our `.md` files. Let's try it: Change the date in `index.md` by opening it from the file directory. Change to today's date, and save. Then refresh the previewed site and you'll see your changes displayed!

## Create a new `.ipynb` page

Let's add a new page to our site. Instead of an `.md` file like the others, let's add a \`.ipynb\` file.

## Authoring

https://quarto.org/docs/reference/cells/cells-jupyter.html

## Troubleshooting

If it hangs/if I get errors:

Check the specific notebook, are there \`---\`? Delete those. Is there too much in the first raw cell? Change that

## 
