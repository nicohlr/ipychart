# Getting Started

## Installation

ipychart can be installed using pip. Don't forget to activate the jupyter notebook extension after the installation:

``` bash
$ pip install ipychart

# activate jupyter notebook extension
$ jupyter nbextension enable --py --sys-prefix ipychart
```

## Quick start

To create a chart, we first need to import the Chart class from ipychart:

``` python
from ipychart import Chart
```

After that, we need to create an instance of that class. We need to create a python dict to format our data. We also need to specify with what type of chart we want to display our data using the **kind** argument. 

Concretely, we can do that very easily in one cell of our notebook in the following way:

``` python
dataset = {
    'labels': ['Germany','Spain', 'UK', 'Italy', 'Norway', 'France', 'Poland', 'Portugal'],
    'datasets': [{'data': [114, 106, 106, 107, 111, 133, 109, 109]}]}

mychart = Chart(data=dataset, kind='bar')

mychart
```

<getting-started/>