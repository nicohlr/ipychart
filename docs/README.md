# Documentation

This folder contains the documentation of ipychart. It is made using [Vuepress](https://vuepress.vuejs.org/).

## Install

``` bash
# in ipychart/docs
$ yarn add -D vuepress # OR npm install -D vuepress
```

## Development

``` bash
$ yarn docs:dev # OR npm run docs:dev
```

## Deployment

You can export the doc as a static website:

``` bash
$ yarn docs:build
```

All the files will be exported in the `public` folder.

You can also automate the deployment by pushing the doc on a GitHub repo with a [yaml file](https://github.com/nicohlr/ipychart/blob/master/.github/workflows/deploy-documentation.yml) located in the `.github` folder at the root of the project. Deployment will then be automated by [GitHub Actions](https://docs.github.com/en/actions).

Vuepress also offers [other deployment methods](https://vuepress.vuejs.org/guide/deploy.html).