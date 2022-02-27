---
title: Quarto Overview
---

[Quarto.org](https://quarto.org) has great documentation, including and [tutorials](https://quarto.org/docs/get-started/hello/jupyter.html) that can help you get started using Jupyter, RStudio, VSCode and Editor. Here, we'll introduce Quarto using our copy of this tutorial, and then show basic workflows using different tools: from the GitHub browser, RStudio, and Jupyter.

## Quarto basic workflow

Developing your quarto site will have the same basic workflow, no matter which tool you use to edit. It is very iterative.

1.  Create content (text, code, images, etc) in a file. Supported files include `.md`, `.Rmd`, `.qmd`, `.ipynb`...
2.  Update `_quarto.yml` as needed (for example, if you've created a new file you'd like included in your site)
3.  Quarto Render individual files and/or the whole website (if editing from the browser this step will not be separate but combined with Step 5)
4.  Repeat, repeat, repeat
5.  Commit and push your website to GitHub, your updates will publish automatically! (if editing from the brower, only commit - no need to push)
6.  Repeat all of the above

## `_quarto.yml`

There is also a `_quarto.yml` file, which is the website's configuration file. It is a directory of the order that the pages/chapters will be in. This is where you update the organization of your website, while you update the content of those pages in the specific file. If we compare side-by-side, you'll see that the pages that appear on our website are listed there.

![`_quarto.yml` and website side-by-side](images/quarto-yml-site-side-by-side.png){alt="_quarto.yml and website side-by-side" fig-align="center" width="95%"}

This type of file (`.yml` or `.yaml`) is written in YAML ("Yet Another Markup Language"). You'll be able to shift the arrangement of webpages by reordering/adding/deleting them in the `_quarto.yml` file following the patterns you see in this example. As you modify `_quarto.yml`, the most important thing to know is that **spacing matters**. Pay attention to whether text is indented by one, two, four, or other spaces, and make sure you follow it; if your site is not looking as expected it is likely a silent error in your YAML. Some text editors like RStudio provide debugging support for YAML and are highly recommended to save you hours of debugging time.

Note that there are multiple ways in the `_quarto.yml` for you to include a file in your website.

## Next up: workflows

In the next sections we'll see what this workflow looks like using different tools for editing your files. We'll start off from the browser so you don't need to install any additional software, however this approach is very limited and you will soon outgrow its capabilities. See all the tools that are supported at <https://quarto.org/docs/get-started/>.

**If you don't already have a workflow and to edit files and sync to GitHub from your computer, I recommend RStudio.** You don't need to know R to use RStudio, and it has powerful editor features that make for happy workflows.
