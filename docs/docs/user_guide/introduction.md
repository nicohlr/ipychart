# Introduction

This package is a python package made for datavizualisation. It allows to create dynamic, refined and customizable charts within the famous Jupyter Notebook environment. It is paticularly suitable for Data Sientists who are looking for a smart way of displaying and presenting their data directly from the output cells of their notebook.

## How It Works

Ipychart is an [ipywidget](https://ipywidgets.readthedocs.io/en/stable/). Ipywidgets are "objects" developed by the creators of Jupyter themself. It allows to use pure javascript code directly in the jupyter environment which is a Python environment. This bridge between javascript and Python is is made available in open source via the possibility for anyone to create a custom ipywidget. This package, which is therefore a custom ipywidget, takes advantage of the power of ipywidgets to make the [Chart.js](https://www.chartjs.org/) javascript library available to all jupyter notebooks users.

The ipychart API is extremely similar - not to say identical - to the API of Chart.js. Is is made to make all features of Chart.js avaible in ipychart. As a lot of informations visible in the official Chart.js documentation can be transposed in ipychart, with an adaptation to the syntax of python, do not hesitate to refer to the documentaiton of chart.js if you cannot find what you are looking for in this documentation,

## Features

**Charts**

* [Line](../user_guide/charts.md#Line)
* [Bar](../user_guide/charts.md#Bar)
* [Radar](../user_guide/charts.md#Radar)
* [Doughnut](../user_guide/charts.md#Doughnut)
* [Polar Area](../user_guide/charts.md#Polar\Area)
* [Bubble](../user_guide/charts.md#Bubble)
* [Scatter](../user_guide/charts.md#Scatter)
* [Area](../user_guide/charts.md#Area)
* [Mixed](../user_guide/charts.md#Mixed)

**Configuration**

* [Scales](../user_guide/config.md#Scales)
* [Title](../user_guide/config.md#Title)
* [Legend](../user_guide/config.md#Legend)
* [Tooltips](../user_guide/config.md#Tooltips)
* [Layout](../user_guide/config.md#Layout)
* [Animations](../user_guide/config.md#Animations)

**Advanced Features**

* [Work with Pandas Dataframes and Numpy Arrays](../user_guide/advanced.md#Work\with\Pandas\Dataframes\and\Numpy\Arrays)
* [Advanced configuration with callback functions](../user_guide/advanced.md#Advanced\configuration\with\callback\functions)
