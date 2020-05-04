# Usage

The ipychart API is composed of only one **Chart** class which allow you to create all types of chart. This class takes 3 arguments as input : **data**, **kind** and **options**. This three arguments have a particular structure to match the backend Chart.js API. If you don't respect the structure of these arguments the package may not work. In this section, we will go through each argument to present its use and its structure. 

## Intro to Chart.js

::: tip
If you are already familiar with Chart.js, you can skip this part.
:::

Before looking at ipychart, lets take a look at what it looks like to create a chart with Chart.js. It will allow us to better understand how ipychart works:

``` js
// This is to gather the html container of the chart, don't pay too much attention to it
var ctx = document.getElementById('myChart').getContext('2d');

// The creation of the chart begins here
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [{
            label: 'My First dataset',
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data: [0, 10, 5, 2, 20, 30, 45]
        }]
    },

    // Configuration options go here
    options: {}
});
```

This example is taken from [the introduction page of the Chart.js documentation](https://www.chartjs.org/docs/latest/). As you can see, there are also three main arguments in Chart.js : data, type and options. These are the same arguments in ipychart, exept for the type argument which as been renamed in king in ipychart because type is a reserved keyword in the Python language. Now, lets take a look of how we can create the same chart as above bu using Python code and ipychart in our jupyter notebook environment :

``` py
from ipychart import Chart

# The creation of the chart begins here
mychart = Chart(
    # The type of chart we want to create
    kind='line',

    # The data for our dataset
    data= {
        'labels': ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        'datasets': [{
            'label': 'My First dataset',
            'backgroundColor': 'rgb(255, 99, 132)',
            'borderColor': 'rgb(255, 99, 132)',
            'data': [0, 10, 5, 2, 20, 30, 45]
        }]
    },

    # Configuration options go here
    'options': {}
})
```

As you can see, a Chart.js user will not be disoriented by switching to ipychart. Now we can take a look at the specificities of each of three arguments useful to create a chart with ipychart.


## Data

The data argument is the most important of the Chart class. Without this argument, the chart cannot be displayed (it is logical, how do you want to display a chart without data ?). The data argument **must be a dict**. This constraint is imposed by Chart.js, which takes its arguments via a javascript dict. This data dict must have the following structure : 

``` py
data = {
    'datasets': list of dict,
    'labels': list
}
```

The datasets argument will hold your data, it **must be a list of dict, each dict containing at least a key called 'data'**. It is a list because you can print more than one ensemble of data points in one chart. Each sub dict corresponds to an ensemble of data points, representing a dataset, and must also follow a specific structure. However, this structure may change according to the type of chart. Please refer to [the documentation of each chart type]() to have more detail about the dataset structure to adopt. 

The labels argument **must be a list**. If only one dataset is passed (i.e. if len(data['datasets] is 1)), the labels list will represent the labels of each datapoint of the only dataset passed. However, if more than one dataset is passed, the label list will represent the labels of each dataset.

::: danger
The data dict must have these two elements, otherwise you can expect dysfunction or unexpected behavior.
:::

## Kind

## Options
