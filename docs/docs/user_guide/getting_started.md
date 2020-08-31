# Getting Started

## Installation

You can install ipychart from your terminal using pip or conda:

``` bash
# using pip
$ pip install ipychart

# using conda
$ conda install -c conda-forge ipychart
```

That's about it. You can now start a Jupyter Notebook and start using ipychart !

::: danger
If you are working within a virtual environment, **please make sure to launch the notebook from the same environment out of which you installed ipychart**:
```bash
$ source activate myenv # or conda activate myenv
(myenv) $ jupyter notebook # notebook is launched from myenv environment
```
Otherwise, the charts will not be displayed.
:::

## Check Installation

You may have to enable the Jupyter notebook extension if it is not already done. You can view enabled extensions using the following command:

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

To create a chart, we first need to import the *Chart* class from ipychart:

``` py
from ipychart import Chart
```

After that, we need to create an instance of that class. We'll have to create a Python dictionary to format our data. We'll also specify with what type of chart we want to display our data using the **kind** argument. 

Concretely, we can do that very easily in the following way:

``` py
dataset = {
  'labels': ['Data 1', 'Data 2', 'Data 3', 'Data 4', 
             'Data 5', 'Data 6', 'Data 7', 'Data 8'],
  'datasets': [{'data': [14, 22, 36, 48, 60, 90, 28, 12]}]
}

mychart = Chart(data=dataset, kind='bar')
mychart
```
The chart is displayed directly as an output from the notebook cell. It looks like this:

<getting-started/>

::: tip
You can hover the chart to display some data for each bar. These popups are called "tooltips" and are [fully configurable](/ipychart/user_guide/configuration#tooltips).
:::