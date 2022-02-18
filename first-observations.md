---
title: First Observations
---

With this tutorial, we have a working example website that we will explore together. We'll learn a few rules and look for patterns to get an understanding of what things do to help you start customizing and making it your own. And you can continue to use this website as a reference after the tutorial, along with [**Quarto**](https://quarto.org) documentation. (Sidenote: this is actually a Quarto website that looks like a book - books are better for cross-referencing chapters, figures, equations, and references so that might be an option for you to explore too.)

We'll start our exploration online looking at the website architecture, and discuss how you can make modifications from the browser with GitHub automatically publishing via GitHub Actions. Then we'll clone the repo and explore further workflows with different tools. 

## Exploring online

### The website itself

This website has 5 things you can see on the left sidebar: 

- Welcome
- First Observations
- Basic Workflows
- Render vs. Preview
- Getting Sophisticated

Most of these are pages, but you'll see that "Basic Workflows" is a subfolder with additional pages inside.

### The website's repo

TODO develop

Let's go to **<https://github.com/openscapes/quarto-website-tutorial>**.

![screenshot of github repo]

**Now let’s look at the filenames.** We can recognize the names of the webpages we’ve seen, and there is also a `_quarto.yml` file, which is the website’s configuration file. 

![screenshot of annotated filenames]

`_quarto.yml` is a directory of the order that the pages/chapters will be in. This is where you update the organization of your website, while you update the content of those pages in the specific file. 

Committing will trigger the GitHub Action to rebuild and republish the book. Note that the GitHub Action for this book does not include R or Python so those will need to be added if your website relies on code. 

## Your turn

These instructions are for starting with an existing Quarto site and copying it into your space to edit. 

### Choose an existing website/book

A simple option is to start with this site: [quarto-website-tutorial](https://github.com/Openscapes/quarto-website-tutorial). 

Other options of potential interest: 

- [2021-Cloud-Hackathon](https://github.com/NASA-Openscapes/2021-Cloud-Hackathon)
- [2022-SWOT-Ocean-Cloud-Workshop](https://github.com/podaac/2022-SWOT-Ocean-Cloud-Workshop)
- [Approach-Guide](https://openscapes.github.io/approach-guide)

### Fork the existing repo

Follow [these steps to fork and setup your repo](https://github.com/thefaylab/lab-manual/wiki/Quick-steps-to-making-a-copy-of-the-lab-manual-&-publishing-it) from Gavin Fay, using the repo you chose.



Now you're set up to edit from the GitHub browser and your book will be republished with our edits. A workflow from the browser if good for getting started/making small contributions but is definitely limited. Once you feel comfortable here, you can move to a different setup. 
