# Documentation

This folder contains the documentation of ipychart. It is made using [Vuepress](https://vuepress.vuejs.org/)

## Install

    # in ipychart/docs
    yarn add -D vuepress # OR npm install -D vuepress

## Development

    yarn docs:dev # OR npm run docs:dev

## Deployment

Upload on gitlab with [.gitlab-ci.yml](../.gitlab-ci.yml) file at the root of the project. Deployment will be automated by [GitLab pages](https://docs.gitlab.com/ee/user/project/pages/).