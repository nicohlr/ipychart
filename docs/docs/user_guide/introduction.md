# Introduction

This package is a python package made for data vizualisation. It allows to create dynamic, refined and customizable charts within the famous Jupyter Notebook environment. It is particularly suitable for Data Scientists who are looking for a smart way of displaying and presenting their data directly from the output cells of their notebooks.

## How It Works

Ipychart is an [ipywidget](https://ipywidgets.readthedocs.io/en/stable/). Ipywidgets are tools developed by the creators of Jupyter themselves. It allows to use pure Javascript code directly in the Jupyter environment, which is a Python environment. This bridge between Javascript and Python is made available in open source via the possibility for anyone to create a custom ipywidget. This package, which is therefore a custom ipywidget, takes advantage of the power of this bridge between Javascript and Python to make the [Chart.js](https://www.chartjs.org/) Javascript library available to all Jupyter Notebooks users.

The ipychart API is extremely similar - not to say identical - to the API of Chart.js. It is made to make all options and possibilities offered by Chart.js avaible in ipychart. As a lot of informations present in the official Chart.js documentation can be transposed in ipychart, with an adaptation to the syntax of python, do not hesitate to refer to the [official documentation of Chart.js](https://www.chartjs.org/docs/latest/) if you cannot find what you are looking for here.

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

* [Pandas integration](../user_guide/advanced.md#Work\with\Pandas\Dataframes\and\Numpy\Arrays)
* [Datalabels](../user_guide/advanced.md#Advanced\configuration\with\callback\functions)
* [Callback functions](../user_guide/advanced.md#Advanced\configuration\with\callback\functions)
* [Export & embedding](../user_guide/advanced.md#Advanced\configuration\with\callback\functions)
