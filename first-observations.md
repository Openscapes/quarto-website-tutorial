---
title: First Observations
---

With this tutorial, we have a working example website that we will explore together. We'll learn a few rules and look for patterns to get an understanding of what things do to help you start customizing and making it your own. And you can continue to use this website as a reference after the tutorial, along with [**Quarto**](https://quarto.org) documentation. (Sidenote: this is actually a Quarto website that looks like a book - books are better for cross-referencing chapters, figures, equations, and references so that might be an option for you to explore too.)

We'll start our exploration online looking at the website architecture and GitHub repository. Then we'll fork the repo and set it up so that any modifications (commits) will automatically be republished via GitHub Actions. Subsequent chapters will describe how to modify your forked repo using different tools (browser, RStudio, Jupyter).

## Exploring online

### The website itself

[This website](https://openscapes.github.io/quarto-website-tutorial/) has 5 things you can see on the left sidebar:

-   Welcome
-   First Observations
-   Basic Workflows
-   Render vs. Preview
-   Getting Sophisticated

Most of these are pages, but you'll see that "Basic Workflows" is a folder with additional pages inside.

### The website's repo

Let's go to this website's GitHub repository (also called a "repo"), [**https://github.com/openscapes/quarto-website-tutorial**](https://github.com/openscapes/quarto-website-tutorial){.uri}. From this website, you can get there by clicking the GitHub octocat icon underneath the Openscapes logo (click it holding command on Mac, or control on a PC to open it in a different tab in your browser).

**Have a look at the filenames.** We can recognize the names of the webpages we've seen above, they have red arrows marking them. You'll see the "basic-workflows" folder and the rest in this site are `.md` files, which are plain Markdown files. `index.md` is the home page.

![quarto-website-tutorial GitHub repository with files for webpages marked with red arrows](images/quarto-files-github.png){fig-alt="Screenshot of files on GitHub with red arrows identifying the files that we saw in the left sidebar" fig-align="center" width="80%"}

### `_quarto.yml`

There is also a `_quarto.yml` file, which is the website's configuration file. It is a directory of the order that the pages/chapters will be in. This is where you update the organization of your website, while you update the content of those pages in the specific file. If we compare side-by-side, you'll see that the pages that appear on our website are listed there.

![`_quarto.yml` and website side-by-side](images/quarto-yml-site-side-by-side.png){fig-align="center" width="95%"}

This type of file (`.yml` or `.yaml`) is written in YAML ("Yet Another Markup Language"). You'll be able to shift the arrangement of webpages by reordering/adding/deleting them in the `_quarto.yml` file following the patterns you see in this example. As you modify `_quarto.yml`, the most important thing to know is that **spacing matters**. Pay attention to whether text is indented by one, two, four, or other spaces, and make sure you follow it; if your site is not looking as expected it is likely a silent error in your YAML. Some text editors like RStudio provide debugging support for YAML and are highly recommended to save you hours of debugging time.

## Fork to your account

Let's start with an existing Quarto site and copy it into your space to edit. First, choose an existing website/book to copy. The simplest option is to start with this site: [quarto-website-tutorial](https://github.com/Openscapes/quarto-website-tutorial).

Other options of potential interest:

-   [2021-Cloud-Hackathon](https://github.com/NASA-Openscapes/2021-Cloud-Hackathon)
-   [2022-SWOT-Ocean-Cloud-Workshop](https://github.com/podaac/2022-SWOT-Ocean-Cloud-Workshop)
-   [Approach-Guide](https://openscapes.github.io/approach-guide)

Next, follow [these steps to fork and setup your repo with GitHub Actions](https://github.com/thefaylab/lab-manual/wiki/Quick-steps-to-making-a-copy-of-the-lab-manual-&-publishing-it) from Gavin Fay, using the repo you chose. These instructions will take \~5 minutes.

Now you've got a copy of your repo of choice in your own GitHub account, and you're set to start making your own edits. Your GitHub repo is set up with a GitHub Action that will use Quarto to rebuild and republish your site anytime you make a commit: committing will trigger the GitHub Action to rebuild and republish the book.

Note that the GitHub Action for this book does not include R or Python so those will need to be added if your website relies on code. See <https://github.com/r-lib/actions> for more details and examples.

### Download instead of fork

Forking might not always be the way to go - you can't fork into the same GitHub user account or organization so if for example you want to make a copy of [2021-Cloud-Hackathon](https://github.com/nasa-openscapes/2021-Cloud-Hackathon) repo within the same NASA-Openscapes GitHub Organization, you'll need to do the following. In this case, follow these steps to download and copy into a new repository, and set up the GitHub Action separately.

#### Download github repo files

Navigate to <https://github.com/openscapes/quarto-website-tutorial> (or any other quarto site repo of choice). Click the green "Code" button and select "Download ZIP". When it downloads on your computer, unzip the files.

#### Create a new GitHub repo

Navigate to your GitHub account or organization, and create a new repository, naming it what you'd like.

#### Add template site files

To use the GitHub file uploader, click the button next to the green "Code" button that says "Add file". Add file \> Upload files. Then, on your computer, select all the files in unzipped folder (command-A or control-A, and drag them to the GitHub uploader page. Scroll down to write a commit message, which effectively saves your files when you're working in the browser.

Note: if you're comfortable cloning the new repository and copying files into it locally before committing and pushing back to GitHub, that can be preferable to the uploader, which does have limitations with complex repos (although the uploader works fine with this tutorial repo).

#### Set up GitHub publishing

If you've used the GitHub uploader, you are not quite set up for publishing. We'll do this in a few steps: we'll set up a GitHub Action within your repo, and create a `gh-pages` branch.

First, the GitHub Action. Go back to your main view of your GitHub repository by clicking on the name of your repository in blue at the top-left (the url in your browser window should say https://github.com/username/repo-name.

Add file \> Create new file. Name it exactly this: `.github/workflows/quarto-render.yml`

Start by typing the `.` with `github` and when you type the `/` it will give you a new text box to type `workflows` (plural!) and finally, `quarto-render.yml`.

Then, you'll have an empty new file. Paste this inside - you can click on the top-right of this box to copy all the code inside this code box:

``` yaml
name: Render and deploy quarto files
on: 
  push:
  pull_request:

jobs:
  quarto-render-and-deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2

    - name: "Install Quarto and render project"
      uses: nasa-openscapes/quarto-render@v0.3.79 

    - name: "Deploy to gh-pages"
      uses: peaceiris/actions-gh-pages@v3
      if: github.ref == 'refs/heads/main'
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./_site
```

Commit this to save your new `quarto-render.yml` file. This is your GitHub Action.

Next, we'll create a new `gh-pages` branch. Go back to the main view of your GitHub repository. On the far left from the green "Code" button, click the button that says "main". In the pull-down menu, type `gh-pages` - all lowercase, with a hyphen. Click the bold text that says "Create branch: gh-pages from main".

Now click on the Settings tab in the top right of your repository. On the left sidebar, click Pages. At the top of Pages under "Source", select `gh-pages` root, and press Save. You'll then see a green highlighted text saying that your site is published at a "github.io" url .

![](images/github-source-gh-pages.png){fig-align="center" width="95%"}

To confirm this, go back to your main repository page. You'll now see an orange dot showing that the GitHub Action is beginning to publish the page.

![](images/github-action-orange.png){fig-align="center" width="95%"}

If you do not see this orange dot, you might need to make a small commit to trigger the GitHub Actions build. If this is the case, click the pencil on the top-right of the README.md file, add some small edit (like a space after a period), and scroll down to click commit. Now you should see the orange dot.

![](images/github-edit-readme.png){fig-align="center" width="95%"}

When your orange do becomes a green check, you can go inspect your published site at "https://username.github.io/your-repo). For example: <https://openscapes.github.io/quarto-website-tutorial>.

![](images/github-action-green.png){fig-align="center" width="95%"}

## Renaming your repo

If you'd like to rename your repo, go to Settings and the option to rename is on the top of the main settings page.

Now you can start editing. The next chapter describes how starting off from the browser, using Markdown.
