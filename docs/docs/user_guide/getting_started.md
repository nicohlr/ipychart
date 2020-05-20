# Getting Started

## Installation

You can install ipychart from your terminal using pip:

``` bash
$ pip install ipychart
```

You can now start a notebook jupyter and start using ipychart !

::: danger
If you are working with a virtual environment, **please be sure to launch the notebook from the same environment where you installed ipychart**:
```bash
$ source activate myenv # or conda activate myenv
(myenv) $ jupyter notebook # notebook is launched from myenv environment
```
Otherwise, the charts will not be displayed.
:::

## Check Installation

You may have to enable the jupyter notebook extension if it is not done already. You can check which extension is enabled using the folowing command:

``` bash
$ jupyter nbextension list
# You should see something like this:
config dir: /home/user/anaconda3/etc/jupyter/nbconfig
notebook section
    ipychart/extension  enabled
    - Validating: OK
```

If you see that ipychart is not enabled in the output of the previous command, run:  

``` bash
# enable jupyter notebook extension
$ jupyter nbextension enable --py --sys-prefix ipychart
```

## Quick start

To create a chart, we first need to import the Chart class from ipychart:

``` python
from ipychart import Chart
```

After that, we need to create an instance of that class. We'll have to create a python dict to format our data. We'll also specify with what type of chart we want to display our data using the **kind** argument. 

Concretely, we can do that very easily in one cell of our notebook in the following way:

``` python
dataset = {
    'labels': ['Germany','Spain', 'UK', 'Italy', 'Norway', 'France', 
               'Poland', 'Portugal'],
    'datasets': [{'data': [114, 106, 106, 107, 111, 133, 109, 109]}]
    }

mychart = Chart(data=dataset, kind='bar')
mychart
```
The chart is displayed directly as an output from the notebook cell. It looks like this:

<getting-started/>

::: tip
You can hover the chart to display some data for each bar. These popups are called "tooltips" and are [fully configurable]().
:::