# Usage

The ipychart API is composed of two classes:

- The first one, named *Chart*, replicates the *Chart* class of Chart.js library while being adapted to the syntax of Python. The majority of the documentation is dedicated to it.

- The second class, named *ChartDataFrame*, allows you to draw charts directly from a Pandas dataframe. It is described in the [Pandas Interface section](/ipychart/user_guide/pandas).

## Chart.js vs ipychart

::: tip
If you are already familiar with Chart.js, you can skip this part.
:::

Before looking at ipychart, let's take a look at what it looks like to create a chart with Chart.js. It will allow us to better understand how ipychart works:

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

This example is taken from [the getting-started page of the Chart.js documentation](https://www.chartjs.org/docs/latest/getting-started/). As you can see, there are three main arguments in Chart.js : **data**, **type** and **options**. These are the same arguments in ipychart, except for the `type` argument which has been renamed `kind` in ipychart because `type` is a reserved keyword in the Python language. 

Now, let's take a look on how we can create the same chart as above while using Python code and the ipychart library in our Jupyter Notebook environment:

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

The *Chart* class takes 5 arguments as inputs: **data**, **kind**, **options**, **colorscheme** and **zoom**. These arguments have a particular structure to match the backend Chart.js API. If you don't respect the structure of these arguments the package may not work.

``` py
Chart(data: dict,
	  kind: str,
	  options: dict = None,
	  colorscheme: str = None,
	  zoom: bool = True)
```

In this section, we will go through each argument to present its use and its structure.

### Data

The `data` argument is the most important one of the *Chart* class. Without this argument, the chart cannot be displayed (how to display a chart without data?). The `data` argument **must be a dict**. This constraint is imposed by Chart.js, which takes its arguments via a Javascript object. This data dictionary must have the following structure : 

``` py
data = {
    'datasets': list of dict,
    'labels': list
}
```

The value of `'datasets'` will hold your data, it **must be a list of dictionaries, each one containing at least a key named** `'data'`. It is a list because you can display more than one ensemble of data points in one chart. Each sub dictionary corresponds to an ensemble of data points, representing a dataset, and must also follow a specific structure. However, this structure may change according to the type of chart. 

Please refer to [the documentation of each chart type](/ipychart/user_guide/charts) to have more details about the dataset structure to use. 

The value of `'labels'` **must be a list**. If only one dataset is passed (i.e. if len(data['datasets] is 1)), the labels list will represent the labels of each datapoint of the only dataset passed. However, if more than one dataset is passed, the label list will represent the labels of each dataset.

::: warning
The data dictionary must have these two elements, otherwise you can expect dysfunction or unexpected behavior.
:::

### Kind

The `kind` argument allows you to choose the type of chart you want to draw. It **must be a string**. You can choose a type of string from the following list:

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
Below is the use case of each of these dictionaries. Of course, these five dictionaries have numerous sub arguments. This is why two whole sections of this documentation have been dedicated to them. 

- **legend:** you can configure the legend of your chart with this dictionary. In ipychart, legend is dynamic and allows you to display or hide some of your inputted datasets! To find out how you can customize the legend of your chart, please check the [legend documentation section](/ipychart/user_guide/configuration#legend).
- **title:** you can configure the title of your chart with this dictionary. To find out how, please check the [title documentation section](/ipychart/user_guide/configuration#title).
- **tooltips:** you can configure the tooltips of your chart with this dictionary. In ipychart, hovering a chart displays some information, these popups are called "tooltips". You can configure these tooltips in many ways. To find out how, please check the [tooltips documentation section](/ipychart/user_guide/configuration#tooltips). You can even inject some Javascript code to display your own text around your data on while hovering a chart. The procedure for doing this is described in the [callback functions section of the documentation](/ipychart/user_guide/advanced#callback-functions).
- **scales:** you can configure the scales of your chart with this dictionary. To find out how, please check the [scales page](/ipychart/user_guide/scales).
- **layout:** you can configure the layout of your chart with this dictionary. To find out how, please check the [layout documentation section](/ipychart/user_guide/configuration#layout).
- **hover:** you can configure the hovering options of your chart with this dictionary. To find out how, please check the [hover documentation section](/ipychart/user_guide/configuration#hover).
- **animation:** you can configure the animations of your chart with this dictionary. To find out how, please check the [animation documentation section](/ipychart/user_guide/configuration#animations).

### Colorscheme

::: warning
The `colorscheme` argument will be ignored if any color configuration is set in one of the datasets passed to the chart. In other words, **the argument will only work if no color configuration option is used in the chart**.
:::

The `colorscheme` argument allow you to automatically set a predefined color scheme to your chart. This is a feature which is not present natively in Chart.js. It has been added in ipychart using [an open-source implementation](https://github.com/nagix/chartjs-plugin-colorschemes). 

The `colorscheme` argument must be a string corresponding to the chosen color scheme ([click here to see the list of all the available color schemes](https://nagix.github.io/chartjs-plugin-colorschemes/colorchart.html)). Color schemes are based on popular tools such as ColorBrewer, Microsoft Office and Tableau.

Example of setting a colorscheme to a chart:

``` py
mychart = Chart(data=mydata, 'bar', options=myoptions, colorscheme='tableau.Blue20')
```

Please note that the chart will associate one color of the colorscheme to each dataset. Thus, if your chart contains only one dataset, this one will be drawn only in one color.


Now that you are familiar with the structure of each argument, you can head to the next section to learn about the different types of charts.

### Zoom

::: warning
The zoom features is not available for **radar**, **doughnut**, **pie** and **polarArea** charts (i.e. the `zoom` argument will automatically be set to `False` for these charts).
:::

The `zoom` argument allow you to zoom on the chart once it is created. As the `colorscheme` argument, the `zoom` argument is not present natively in Chart.js. It has been added in ipychart using [an open-source implementation](https://github.com/chartjs/chartjs-plugin-zoom).

By default, the zoom is activated when you create a chart. To disable this feature, just set the zoom argument of the chart to `False`.

::: tip
To reset the zoom to its initial level, you only have to double click anywhere on the chart!
:::
