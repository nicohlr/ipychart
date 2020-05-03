# Building the documentation

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

To deploy the doc, the easiest way is to upload it on a GitLab repo with a [.gitlab-ci.yml](https://github.com/nicohlr/ipychart/blob/master/.gitlab-ci.yml) file at the root of the project. Deployment will then be automated by [GitLab pages](https://docs.gitlab.com/ee/user/project/pages/).

Vuepress also offers [other deployment methods](https://vuepress.vuejs.org/guide/deploy.html).