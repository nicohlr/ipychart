# Advanced Features

## Datalabels

In ipychart, you can add labels directly to your chart. This is not a native feature in Chart.js and it has been added using [an external open source package](https://chartjs-plugin-datalabels.netlify.app/). 

In practice, the datalabels are controlled from the 'datalabels' key (which takes a dictionary as value) present in each dataset that you pass to the *Chart* class. For example, with the following code, we will display the datalabels on the second dataset:

```py
dataset = {
  'labels': ['Label 1', 'Label 2', 'Label 3'],
  'datasets': [{'data': [221, 783, 2478], 'label': "Africa"},
               {'data': [1402, 3700, 5267], 'label': "Asia",
                'datalabels':  {'display': True}}, # Toggle display datalabels
               {'data': [547, 675, 734], 'label': "Europe"},
               {'data': [167, 508, 784], 'label': "Latin America"},
               {'data': [172, 312, 433], 'label': "North America"}]
}

mychart = Chart(dataset, 'bar', colorscheme='tableau.Tableau10')
mychart
```

<advanced-datalabels-simple/>

By default, datalabels are just the values of the y axis for each data point, written in gray on each point. However, it is possible to personalize them. Some of the available options are listed below. You can see all the possible options on the documentation of the [chartjs-plugin-datalabels](https://chartjs-plugin-datalabels.netlify.app/guide/options.html#scriptable-options).

```py
# More detail on arguments are available here : 
# https://chartjs-plugin-datalabels.netlify.app/guide/positioning.html#anchoring

dataset = {
  'datasets': [{
    'datalabels': {
      'align': str # Position of the label | Default: 'center'
      'anchor': str # Orientation of the label | Default: 'end' 
      'borderRadius':  int # Radius of the border | Default: 0 
      'borderWidth': int # Width of the border | Default: 0  
      'color': str # Font color | Default: '#666'
      'display': # Display datalabels | Default: False
    }
  }]
}
```

When the `'borderRadius'` argument is set, ipychart will automatically fill the `'borderColor'` and `'backgroundColor'` arguments (if they are not already set by the user) to match the chart colors. Therefore, you can quickly format the datalabels so that they appear harmoniously on the chart:

```py
datalabels_arguments = {'display': True, 'borderWidth': 1, 'anchor': 'end', 
                        'align': 'end', 'borderRadius': 5, 'color': '#fff'}

dataset = {
  'labels': ['Label 1', 'Label 2', 'Label 3'],
  'datasets': [{'data': [221, 783, 2478], 'label': "Africa", 
                'datalabels':  datalabels_arguments},  
                {'data': [1402, 3700, 5267], 'label': "Asia", 
                'datalabels':  datalabels_arguments}, 
                {'data': [547, 675, 734], 'label': "Europe", 
                'datalabels':  datalabels_arguments},
                {'data': [167, 508, 784], 'label': "Latin America", 
                'datalabels':  datalabels_arguments},
                {'data': [172, 312, 433], 'label': "North America", 
                'datalabels':  datalabels_arguments}]
}

mychart = Chart(dataset, 'bar', colorscheme='tableau.Tableau10')
mychart
```

<advanced-datalabels-full/>

## Ipywidgets compatibility

As ipychart is an [ipywidget](https://ipywidgets.readthedocs.io/en/latest/), you can benefit from the compatibility between ipychart and other ipywidgets. For example, we can imagine controlling a chart with a slider or a button, or even hiding a chart in a dropdown. Another use, illustrated below, can be to create subplots using [layout widgets](https://ipywidgets.readthedocs.io/en/latest/examples/Layout%20Templates.html):

```py
import ipywidgets as wd

dataset1 = {'labels': ['D' + str(i) for i in range(10)],
            'datasets': [{'data': [random.randint(0, 100) for _ in range(10)]}]}
dataset2 = {'labels': ['D' + str(i) for i in range(10)],
            'datasets': [{'data': [random.randint(0, 100) for _ in range(10)]}]}
dataset3 = {'labels': ['D' + str(i) for i in range(10)],
            'datasets': [{'data': [random.randint(0, 100) for _ in range(10)]}]}
dataset4 = {'labels': ['D' + str(i) for i in range(10)],
            'datasets': [{'data': [random.randint(0, 100) for _ in range(10)]}]}

mychart1 = Chart(dataset1, 'line', colorscheme='tableau.Tableau10')
mychart2 = Chart(dataset2, 'bar', colorscheme='brewer.Accent5')
mychart3 = Chart(dataset3, 'bar', colorscheme='brewer.PuOr3')
mychart4 = Chart(dataset4, 'line', colorscheme='office.Celestial6')

grid = wd.TwoByTwoLayout(top_left=mychart1, top_right=mychart2, 
                         bottom_left=mychart3, bottom_right=mychart4)
grid
```

<advanced-ipywidgets/>

## Callback functions

A Callback function is a Javascript functions inputted into the chart to do some specific actions. There are a lot of things that can be customizable with callback functions in Chart.js (and therefore in ipychart). Often, they are used for advanced customization of some aspects of the chart. For example we saw previously, in the configuration section, that we could modify the text of tooltips (the text bubbles that appear when we hover a data point on a chart) with a callback function.

Concretely, a callback function is a function written in Javascript that will be given as an argument and which will then be executed by Chart.js when the chart is created. To pass a callback function to ipychart while coding in Python, all you have to do is wrap the function in a string. As functions can contain single or double quotes ('or "), it is advisable to encapsulate them in triple quotes:

```py
callback_function = '''function(value, index, values) {return '$' + value;}'''
```

Below is an example (from Chart.js documentation) of a callback function that will include a dollar sign in the ticks of the Chart:

```js
var chart = new Chart(ctx, {
    type: 'line',
    data: data,
    options: {
        scales: {
            y: {
                ticks: {
                    // Include a dollar sign in the ticks
                    callback: function(value, index, values) {
                        return '$' + value;
                    }
                }
            }
        }
    }
});
```

Here is the same example with ipychart:

```py
chart = Chart(
    kind='line',
    data=data,
    options= {
        'scales': {
            'y': {
                'ticks': {
                    # Include a dollar sign in the ticks
                    'callback': '''function(value, index, values) {
                        return '$' + value;
                    }'''
                }
            }
        }
    }
)
```

## Export & embedding

Ipychart offers three ways to export a created Chart. These ways correspond to three methods of the *Chart* class: 

- `to_html(path)`: This function embeds the chart widget into an HTML file dumped at the inputted path location.
- `get_html_template()`: This function returns a string containing HTML code to embed the Chart.
- `get_python_template()`: This function returns the Python code to run in order to reproduce exactly the same chart.
