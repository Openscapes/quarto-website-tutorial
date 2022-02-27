---
title: Quarto Overview
---

## Quarto basic workflow

Developing your quarto site will have the same basic workflow, no matter which tool you use to edit. It is very iterative. 

1. Create content (text, code, images, etc) in a file. Supported files include `.md`, `.Rmd`, `.qmd`, `.ipynb`...
1. Update `_quarto.yml` as needed (for example, if you've created a new file you'd like included in your site)
1. Quarto Render individual files and/or the whole website (if editing from the browser this step will not be separate but combined with Step 5)
1. Repeat, repeat, repeat
1. Commit and push your website to GitHub, your updates will publish automatically! (if editing from the brower, only commit - no need to push)
1. Repeat all of the above

-----

In the next sections we'll see what this workflow looks like using different tools for editing your files. We'll start off from the browser so you don't need to install any additional software, however this approach is very limited and you will soon outgrow its capabilities. See all the tools that are supported at <https://quarto.org/docs/get-started/>.

**If you don't already have a workflow and to edit files and sync to GitHub from your computer, I recommend RStudio.** You don't need to know R to use RStudio, and it has powerful editor features that make for happy workflows. 
