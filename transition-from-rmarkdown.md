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

We transitioned our [events site](https://openscapes.org/events) from distill to quarto in May 2022 (github view [before](https://github.com/Openscapes/events/tree/13f95f507629eba5e6ed721d1902258dcbc421e6) and [after](https://github.com/Openscapes/events/tree/237acd5144d810cb5465cc5616ee453f2e261fbc)). We followed excellent notes and examples from [Nick Tierney](https://www.njtierney.com/post/2022/04/11/rmd-to-qmd/) and [Danielle Navarro](https://blog.djnavarro.net/posts/2022-04-20_porting-to-quarto/). 

A few notes: 

- Our distill site was set up to output to a `docs` folder, and had GitHub Settings > Pages set to look there rather `gh-pages` branch. (Julie note: this was a new-to-me capability when we set up the events distill site in Spring 2021 so I had forgotten that was an option). We've kept this same set-up for now with our events page in `_quarto.yml`: [`output-dir: docs`](https://github.com/Openscapes/events/blob/237acd5144d810cb5465cc5616ee453f2e261fbc/_quarto.yml#L3)

