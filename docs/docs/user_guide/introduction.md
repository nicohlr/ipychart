# Introduction

Ipychart is a python package for datavizualisation. 

## How It Works

Ipychart is an [ipywidget](https://ipywidgets.readthedocs.io/en/stable/). More specifically, it wraps a javascript library called [Chart.js](https://www.chartjs.org/) into a custom ipywidget to make it usable in the python environment Jupyter notebook.

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

## Why Not ...?

**<span style="font-size:larger;">Matplotlib</span>**

Nuxt is capable of doing what VuePress does, but it’s designed for building applications. VuePress is focused on content-centric static sites and provides features tailored for technical documentation out of the box.

**<span style="font-size:larger;">Seaborn</span>**

Both are great projects and also Vue-powered. Except they are both fully runtime-driven and therefore not SEO-friendly. If you don’t care for SEO and don’t want to mess with installing dependencies, these are still great choices.

**<span style="font-size:larger;">Plotly</span>**

Hexo has been serving the Vue docs well - in fact, we are probably still a long way to go from migrating away from it for our main site. The biggest problem is that its theming system is static and string-based - we want to take advantage of Vue for both the layout and the interactivity. Also, Hexo’s Markdown rendering isn’t the most flexible to configure.
