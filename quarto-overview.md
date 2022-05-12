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

Let's have a closer look at the `_quarto.yml` file.

This type of file (`.yml` or `.yaml`) is written in YAML ("Yet Another Markup Language"). You'll be able to shift the arrangement of webpages by reordering/adding/deleting them in the `_quarto.yml` file following the patterns you see in this example. As you modify `_quarto.yml`, the most important thing to know is that **spacing matters**. Pay attention to whether text is indented by one, two, four, or other spaces, and make sure you follow it; if your site is not looking as expected it is likely a silent error in your YAML. Some text editors like RStudio provide debugging support for YAML and are highly recommended to save you time and heartache.

![`_quarto.yml` and website side-by-side](images/quarto-yml-site-side-by-side3.png){alt="_quarto.yml and website side-by-side" fig-align="center" width="95%"}

Notice that there are multiple ways in the `_quarto.yml` for you to include a file in your website. For example, in the above image, the "First Observations" we see in the left sidebar of the published website (right image) is represented in `_quarto.yml` (left image) over two lines, with line 36 indicating the file reference and line 37 indicating the text to show up in the left sidebar. However, "From RStudio" is only represented in one line of `_quarto.yml`, on line 43. This represents two strategies for including a file in your website. By default, the title of a specified file will show up in the website's sidebar, which is what is happening with the "From RStudio" example. If you would like more control over what is written in the sidebar vs the title of your files, then the approach we took with "First Observations" is what you'll want to do: you'll see that only "First Observations" shows up in the sidebar as we specified in `_quarto.yml`, but the page's title says "First Observations & Setup" (which in our preference was too long for the sidebar).

## Authoring

As an author, you have a lot of options of how your text will be formatted, arranged, and interlinked. Check out the Quarto documentation about authoring, starting out with [https://quarto.org/docs/authoring/markdown-basics](https://quarto.org/docs/authoring/markdown-basics.htmlhttps://quarto.org/docs/authoring/markdown-basics.html), to learn more.

Each page of our site - currently all `.md` files - has a similar first couple of lines - this also YAML, and it is indicated by two sets of 3 dashes `---` :

``` bash
---
title: My title
---
```

You're able to add more features to individual pages by including it in the YAML, which for the most part here only includes a title. See [Quarto excecution options](https://quarto.org/docs/computations/execution-options.html) for more information of what you can include in the YAML.

## Learn more about Quarto

-   **Reproducible authoring with Quarto** - Mine Çetinkaya-Rundel, Feb 2022

    -   [slides](https://mine-cetinkaya-rundel.github.io/2022-repro-toronto/#/title-slide), [youtube](https://www.youtube.com/watch?v=6p4vOKS6Xls)

## Next up: workflows

In the next sections we'll see what this workflow looks like using different tools for editing your files. We'll start off from the browser so you don't need to install any additional software, however this approach is very limited and you will soon outgrow its capabilities. See all the tools that are supported at <https://quarto.org/docs/get-started/>.

**If you don't already have a workflow and to edit files and sync to GitHub from your computer, I recommend RStudio.** You don't need to know R to use RStudio, and it has powerful editor features that make for happy workflows.
