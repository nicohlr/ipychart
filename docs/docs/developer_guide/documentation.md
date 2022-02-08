# Build the documentation

The documentation of ipychart is made using [Vuepress](https://vuepress.vuejs.org/). You can find the files used to build it in the [docs folder of the project on GitHub](https://github.com/nicohlr/ipychart/tree/master/docs).

## Install & start locally

From the ipychart/docs folder, run:

``` bash
$ yarn add -D vuepress # OR npm install -D vuepress
```

Then, you can launch the documentation website on localhost using:

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