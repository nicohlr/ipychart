# Introduction

This package is a Python package made for data vizualisation. It allows to create dynamic, refined and customizable charts using Python. It is particularly suitable for Data Scientists who are looking for a smart way to display and present their data directly from the output cells of their notebooks.

<p style="font-size:1.65rem;font-weight:600;line-height:1.25!important;margin-bottom:0;padding-top:4.6rem;padding-bottom:.3rem;margin-top:-3.1rem;border-bottom:1px solid #eaecef;">How does it work ?</p>

Ipychart is an [ipywidget](https://ipywidgets.readthedocs.io/en/stable/). Ipywidgets are tools developed by the creators of Jupyter themselves. It allows using pure Javascript code directly in the Jupyter environment, which is a Python environment. This bridge between Javascript and Python is made available in open source with the possibility for anyone to create a custom ipywidget. This package, which is therefore a custom ipywidget, utilizes the power of this link between Javascript and Python to make the [Chart.js](https://www.chartjs.org/) Javascript library available to all Python users.

The ipychart API is extremely similar - not to say identical - to the API of Chart.js. It is made to make all options and possibilities offered by Chart.js avaible in ipychart. As a lot of informations contained in the official Chart.js documentation can be transposed in ipychart, with an adaptation to the syntax of Python, do not hesitate to refer to the [official documentation of Chart.js](https://www.chartjs.org/docs/latest/) if you cannot find what you are looking for here.

<p style="font-size:1.65rem;font-weight:600;line-height:1.25!important;margin-bottom:0;padding-top:4.6rem;padding-bottom:.3rem;margin-top:-3.1rem;border-bottom:1px solid #eaecef;">Table of Contents</p>

- [**Introduction**](/ipychart/user_guide/introduction)
- [**Getting Started**](/ipychart/user_guide/getting_started)
- [**Usage**](/ipychart/user_guide/usage)
- [**Charts**](/ipychart/user_guide/charts)
- [**Configuration**](/ipychart/user_guide/configuration)
- [**Scales**](/ipychart/user_guide/scales)
- [**Pandas Interface**](/ipychart/user_guide/pandas)
- [**Advanced Features**](/ipychart/user_guide/advanced)
- [**Developers**](/ipychart/developer_guide/development_installation)

<p style="font-size:1.65rem;font-weight:600;line-height:1.25!important;margin-bottom:0;padding-top:4.6rem;padding-bottom:.3rem;margin-top:-3.1rem;border-bottom:1px solid #eaecef;">Related resources</p>

The source code of the ipychart package is available on GitHub at [github.com/nicohlr/ipychart](https://github.com/nicohlr/ipychart).

You can also find, on Github, a repo with notebooks containing various examples of use cases of ipychart. Many code snippets used to create all kinds of charts are gathered there. The repo **ipychart-demo-notebooks** is accessible at the following address : [github.com/nicohlr/ipychart-demo-notebooks](https://github.com/nicohlr/ipychart-demo-notebooks)

You can also try ipychart online, directly on the dedicated binder that uses the notebooks of the **ipychart-demo-notebooks** repo. To do so, [**click here**](https://mybinder.org/v2/gh/nicohlr/ipychart-demo-notebooks/master).

Finally, you can use docker to quickly try ipychart in a fresh Jupyter Notebook environment. To do so, install docker and run the following command in your terminal:

```sh
$ docker run -p 8888:8888 nicohlr/ipychart-demo-notebooks:0.1
```

You can now open your browser and go to http://localhost:5000/. Authenticate yourself into jupyter by copying the token from your terminal and pasting it in the browser.

<p style="font-size:1.65rem;font-weight:600;line-height:1.25!important;margin-bottom:0;padding-top:4.6rem;padding-bottom:.3rem;margin-top:-3.1rem;border-bottom:1px solid #eaecef;">References</p>

- [**Chart.js**](https://www.chartjs.org/)
- [**Ipywidgets**](https://ipywidgets.readthedocs.io/en/latest/index.html)
- [**Ipywidgets cookiecutter template**](https://github.com/jupyter-widgets/widget-cookiecutter)
- [**Chart.js Datalabels**](https://github.com/chartjs/chartjs-plugin-datalabels)
- [**Chart.js Colorschemes**](https://github.com/nagix/chartjs-plugin-colorschemes)
- [**Vuepress**](https://vuepress.vuejs.org/)
- [**GitHub Pages**](https://pages.github.com/)

<p style="font-size:1.65rem;font-weight:600;line-height:1.25!important;margin-bottom:0;padding-top:4.6rem;padding-bottom:.3rem;margin-top:-3.1rem;border-bottom:1px solid #eaecef;">License</p>

Ipychart is available under the [MIT license](https://opensource.org/licenses/MIT).