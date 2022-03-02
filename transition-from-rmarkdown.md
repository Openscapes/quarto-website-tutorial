---
title: Transition from RMarkdown
---

*TODO: develop*

You may already have workflows in RMarkdown and are interested in transitioning to Quarto. 

There's no hurry to migrate to Quarto. Keep using Rmarkdown and when you're ready the migration will be fine.



- translating R code chunks

## Bookdown to quarto

create `_quarto.yml`

Project options > build tools > project build tools > none

Reload project

Don't need to delete anything immediately, but look at `output.yml`, purge afterbody. 

Bookdown might be most challenging because of citations and cross-refs but still not that hard

### GitHub actions

R

## Distill to quarto

*Upcoming*