# Usage

The ipychart API is composed of only one *Chart* class which allows you to create all types of chart. This class takes 4 arguments as input : **data**, **kind**, **options** and **colorscheme**. This arguments have a particular structure to match the backend Chart.js API. If you don't respect the structure of these arguments the package may not work. 

In this section, we will go through each argument to present its use and its structure. But before that, let's start with a little aside to compare the APIs of Chart.js and ipychart.

## Chart.js vs ipychart

::: tip
If you are already familiar with Chart.js, you can skip this part.
:::

Before looking at ipychart, lets take a look at what it looks like to create a chart with Chart.js. It will allow us to better understand how ipychart works:

``` js
// This is to gather the html container of the chart
// Don't pay too much attention to this line of code
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

This example is taken from [the getting-started page of the Chart.js documentation](https://www.chartjs.org/docs/latest/getting-started/). As you can see, there are also three main arguments in Chart.js : **data**, **type** and **options**. These are the same arguments in ipychart, except for the `type` argument which as been renamed `kind` in ipychart because `type` is a reserved keyword in the Python language. Now, lets take a look of how we can create the same chart as above but using Python code and the ipychart library in our Jupyter Notebook environment:

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

As you can see, a Chart.js user will not be disoriented by switching to ipychart. Now, let's take a look at the specificities of each of these three arguments.


## Chart arguments

### Data

The `data` argument is the most important one of the *Chart* class. Without this argument, the chart cannot be displayed (how to display a chart without data?). The `data` argument **must be a dict**. This constraint is imposed by Chart.js, which takes its arguments via a Javascript dict. This data dict must have the following structure : 

``` py
data = {
    'datasets': list of dict,
    'labels': list
}
```

The value for `'datasets'` will hold your data, it **must be a list of dict, each dict containing at least a key named** `'data'`. It is a list because you can print more than one ensemble of data points in one chart. Each sub dict corresponds to an ensemble of data points, representing a dataset, and must also follow a specific structure. However, this structure may change according to the type of chart. 

Please refer to [the documentation of each chart type](/user_guide/charts) to have more details about the dataset structure to adopt. 

The value for `'labels'` **must be a list**. If only one dataset is passed (i.e. if len(data['datasets] is 1)), the labels list will represent the labels of each datapoint of the only dataset passed. However, if more than one dataset is passed, the label list will represent the labels of each dataset.

::: warning
The data dict must have these two elements, otherwise you can expect dysfunction or unexpected behavior.
:::

### Kind

The `kind` argument allows you to choose the type of chart you wants to draw. It **must be a string**. You can choose a type of string in the following values :

``` py
# Possible values for the kind argument
'line'
'bar'
'horizontalBar'
'radar'
'doughnut'
'pie'
'polarArea'
'bubble'
'scatter'
```

::: tip
The `type` argument in Chart.js became `kind` argument in Python because, unlike Javascript, type is a reserved keyword in Python.
:::

### Options

Finally, the last argument of the *Chart* class is `options`. This argument **must be a dict**, it allows you to completely configure your chart.

``` py
options = {
    'legend': dict, 
    'title': dict,
    'tooltips': dict,
    'scales': dict,
    'layout': dict,
    'hover': dict,
    'animation': dict,
}
```
Below are the use of each of these dict. Of course, these five dict have numerous sub arguments. This is why two whole sections of this documentation are dedicated them. 

- **legend:** you can configure the legend of your chart with this dict. In ipychart, legend is dynamic and allow you to display or hide some of your inputed datasets ! To find out how you can customize the legend of your chart, please check the [legend documentation section](/user_guide/configuration#legend).
- **title:** you can configure the title of your chart with this dict. To find out how, please check the [title documentation section](/user_guide/configuration#title).
- **tooltips:** you can configure the tooltips of your chart with this dict. In ipychart, hovering a chart display some information, these popus are called "tooltips". You can configure these tooltips in many ways. To find out how, please check the [tooltips documentation section](/user_guide/configuration#tooltips). You can even inject some Javascript code do display your own text around your data on hover a chart. The procedure for doing this is described in the [callback functions section of the documentation](/user_guide/advanced#callback-functions).
- **scales:** you can configure the scales of your chart with this dict. To find out how, please check the [scales page](/user_guide/scales).
- **layout:** you can configure the layout of your chart with this dict. To find out how, please check the [layout documentation section](/user_guide/configuration#layout).
- **hover:** you can configure the hovering options of your chart with this dict. To find out how, please check the [hover documentation section](/user_guide/configuration#hover).
- **animation:** you can configure the animations of your chart with this dict. To find out how, please check the [animation documentation section](/user_guide/configuration#animations).

### Colorscheme

::: warning
The `colorscheme` argument will be ignored if any color configuration is set in one of the datasets passed to the chart. In other words, **the argument will only work if no color configuration option is used in the chart**.
:::

The `colorscheme` arguments allows you to automatically set a predefined color scheme to your chart. This is a feature which is not present natively in Chart.js. It has been added in ipychart using [an open-source implementation](https://github.com/nagix/chartjs-plugin-colorschemes). 

The `colorscheme` argument must be a string corresponding to the choosen color scheme ([click here to see the list of all available color schemes](https://nagix.github.io/chartjs-plugin-colorschemes/colorchart.html)). Color schemes are based on popular tools such as ColorBrewer, Microsoft Office and Tableau.

Example of setting a colorscheme to a chart:

``` py
mychart = Chart(data=mydata, 'bar', options=myoptions, colorscheme='tableau.Blue20')
```

Please note that the chart will associate one color of the colorscheme to each dataset. Thus, if your chart contains only one dataset, this one will be drawn only in one color.


Now that you are familiar with the structure of each argument, you can head to the next section to learn about the different types of charts.
