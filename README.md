# DfE Statistics Production Guidance

## Introduction

An rmarkdown website used as a central place to hold guidance, helpful links and code examples for statisticians working on Official Statistics at DfE. This is deployed via the DfE visual studio and rsconnect subscriptions. The source repository is hosted in Azure DevOps, though is also mirrored to GitHub after every update to the production environment. This mirror is then deployed via GitHub pages to provide a publicly accessible copy.

---

## Hosted environments

The guidance is publicly at:

https://dfe-analytical-services.github.io/stats-production-guidance-quarto/

---

## Requirements

### i. Software requirements 

- Installation of R 3.6.2 or higher

- Installation of RTools40 or higher

### ii. Programming skills required

- Basic knowledge of [Quarto](https://rmarkdown.rstudio.com/articles_intro.html)

- Understanding of [Quarto websites](https://bookdown.org/yihui/rmarkdown/rmarkdown-site.html)
  
### iii. Access

- The source repository is available publicly on GitHub.

- A number of internal DfE videos are embedded, unless you have specific access via DfE kit they will not appear. If you are interested in their content please get in touch with us.

---

## How to use

Each page of the site is a single quarto document, with index.qmd as the homepage. When the project is opened locally in RStudio you will be able to preview the website byt typing the command `quarto preview` into the terminal.

### Packages

Package control is handled using renv. You may need to run renv::restore() if this is your first time using the project.

### Deployment

Internal deployment is handled via the dfe-gov-uk Azure DevOps instance, using Azure pipelines to deploy to the DfE rsconnect servers. This pipeline then pushes a mirror of the repository to GitHub, where GitHub actions is used to deploy a publicly accessible copy to GitHub pages.

### Tests

There are currently no automated tests on this project, though we hope to add some soon.

### Diagrams

RAP Hexagons - https://app.diagrams.net/#G1usTSACWv_gRBgibnKRK52ksOksF303Dv

RAP Badges - https://app.diagrams.net/#G1uSCknFwmzhy-YHZTGmkuqoMM_zDH2yC0

Create release - https://app.diagrams.net/#G1NcVNEtMtNO--2NtV6RPxceiRv3fDGQ7y

PRA - https://app.diagrams.net/#G1x1VLZghqCCnmDWHqgjpdU6fSSehms4FL

---

## Contribution

If you're interested in contributing to this project, get in touch with us and we can arrange access to the source repository in Azure DevOps. The GitHub repo is only a mirror and any changes made directly to it will be overwritten when the next update is mirrored.

---

## Contact

statistics.development@education.gov.uk.