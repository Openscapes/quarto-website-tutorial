---
title: From RStudio
---

The RStudio software (called an IDE, integrated development environment) is an excellent way to edit files and interface with GitHub. Plus, as it is made by the same folks who make Quarto, it has many integrated features for streamlining your workflow with Quarto, including how it previews your edits and provides debugging support for yaml! Here is what you'll need to do to set up and use RStudio.

## Setup 

### RStudio and GitHub

For a workflow with RStudio and GitHub on your local computer, you will need four things:

1.  R
2.  RStudio
3.  Git
4.  GitHub

Follow the [UCSB MEDS Installation Guide](https://ucsb-meds.github.io/meds-install-guide.html) for detailed instructions on how to create accounts, download, install, and configure on Mac and Windows. This takes about 20 minutes. (For an even more detailed walk-through, see [Allison Horst's ESM 206 Google Doc](https://docs.google.com/document/d/1zx2upJJqFZe94O3BQSMI56Z76s3haLXC0otKSpcZaJQ/edit)). Thanks for sharing Allison!

### Clone your repo

You'll start by cloning your repository into RStudio.

File \> New Project \> Version Control \> Git \> paste your repository name.

[R for Excel Users: Clone your repository using RStudio](https://rstudio-conf-2020.github.io/r-for-excel/github.html#clone-your-repository-using-rstudio) has detailed instructions and screenshots of these steps.

### Install Quarto

Next, you'll install Quarto. Download Quarto from <https://quarto.org/docs/get-started/>. Follow the installation wizard on your computer. When it is complete, you won't see an application or any new software, but it is now available to RStudio (as well as other applications, including the command line).

### RStudio orientation

Now let's take a moment to get oriented. This is an RStudio project, which is indicated in the top-left. The bottom right pane shows all the files in your project; everything we've cloned from GitHub.

![RStudio IDE highlighting the project name and files pane](images/rstudio-orientation.png){fig-alt="Screenshot of the RStudio IDE highlighting the project name and files pane" fig-align="center"}

### Visual Editor

The RStudio Visual Editor is quite new and has features that improve your writing experience.

-   Visual editor makes a familiar experience

-   copy-paste formatting from Google Doc

## Quarto render

In the Build tab in the top-right pane, click "Render Website". This will build the .html files and preview your website. It's equivalent to "knitting" in RMarkdown.

Note that you can also click "Preview Website". With "Render Website" in RStudio, Quarto is able to render and preview in one step.

If you'd ever like to stop the preview, in the bottom-left, click on the Jobs tab and then the red Stop button.

### Make a small change and render it

Click on `index.md`. This will open this markdown file in a fourth pane; the editor pane. Make a small change, for example change to today's date on Line 4. Then, save your file; there is a disc icon at the top of the file.

Then, render this file: press "Render" which is to the right of the disc icon that saves the file. This will render only this single file, as opposed to rerendering the whole website like when we clicked "Render Website" in the top right pane. Checking **Render on Save** (between the disc icon and the Render button) is a great strategy for doing this in one step.

## Create a new `.Rmd` page

Example:

load packages and data

explore

tidy

plot

## Update `_quarto.yml`

## 

## Authoring
