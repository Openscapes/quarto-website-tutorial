---
title: "Create & Publish with Quarto (without R or Python)"
---



## Option 1: Setup from the Browser

### Download template site

1.  Download <https://github.com/Openscapes/quarto-site-template>
2.  Green button \> Download ZIP
3.  On your computer: unzip files

### Create a GitHub repo

### Add template site files

1.  Add file \> Upload files \> Select all the files in unzipped folder \> drag to GitHub
2.  Commit

### Set up GitHub publishing

1.  Add file \> create new file \> name it exactly `.github/workflows/quarto-render.yml`
2.  Paste inside:

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

1. Check that there is a second branch called `gh-pages` - all lowercase, with a hyphen - should be already made!
2.  Settings \> Pages \> Source > make sure this is set to `gh-pages` > root
3.  Go into `_quarto.yml` and update the urls with your own urls, i.e. `https://your-username/your-repo-name.github.io`
4.  Wait until orange dot turns green
5.  Inspect: `https://your-username/your-repo-name.github.io`. For example: <https://openscapes.github.io/quarto-site-template>


