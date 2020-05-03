# Publish

## Versions

Set the **same** version number in all the following files.  

+ `ipychart/js/package.json`
+ `ipychart/js/package-lock.json`
+ `ipychart/__meta__.py`
+ `ipychart/_version.py`

::: warning
This is a **manual** sync.
:::

## Node

Build the Javascript files and publish the node package to [npmjs.org](https://www.npmjs.com/).  
For more info see the [official doc](https://docs.npmjs.com/getting-started/publishing-npm-packages).

```bash
# build notebook extension javascript
$ cd js
$ npm install

# test run to see what you will publish
# npm pack

# login npm if necessary
npm login

# publish npm package to npmjs.org - using ~/.npmrc
$ npm publish --access=public
# if you made a mistake you can unpublish in the first 24h
```

## Python

Publish the Python package to PyPI.  
For more info see the [official doc](https://packaging.python.org/tutorials/distributing-packages/). 

```bash
# clear dist/ from previous bundles
rm -rf dist

# build Python package
$ python setup.py sdist
$ python setup.py bdist_wheel --universal
$ python3 -m twine upload dist/*
```
