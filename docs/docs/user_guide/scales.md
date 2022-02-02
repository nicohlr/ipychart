# Scales

This section is dedicated to the `'scales'` argument of the options dictionary that you'll pass to your Chart. As the other arguments described if the [previous section](/ipychart/user_guide/configuration), the scales argument is a key of the `options` dictionary. However, as it has a lot of possible nested configurations, a whole section of the documentation is dedicated to it. 

With the `'scales'` argument, you can completely configure the axis of your chart. This configuration involves configuring the three axes of your Chart: the x axis, the y axis and the r axis.

Different charts don’t have the same type of scales. There are two types of scales available in ipychart:
* [**The Cartesian Scale**](/ipychart/user_guide/scales#cartesian-scale), used for the following types of chart: line, bar, bubble, scatter. These charts have two axes positioned on one of the edges (the **x** axis and the **y** axis). You can configure them using the `scales['x']` and the `scales['y']` options.

* [**The Radial Scale**](/ipychart/user_guide/scales#radial-scale), used for the following types of chart: radar, polarArea. These charts have only one axis which overlays the chart area. You can configure it using the `scales['r']` option.

Other types of charts (doughnut, pie) do not use scales.

::: tip
In this part, the term **arguments** corresponds to the options of the main dictionaries (dictionaries contained in `'x'`, `'y'` or `'r'` dictionaries), whereas the term **subarguments** corresponds to the options of the nested dictionaries (`'ticks'` or `'time'` sub-dictionaries for example)
:::

## Cartesian scale

::: warning
This section only applies to the following types of charts: **line**, **bar**, **bubble** & **scatter**.
:::

Axes that follow a cartesian grid are known as 'Cartesian Axes'. To configure your axes, you'll have to use the `'scales'` option and the `'x'` and `'y'` sub-options.

The following options are available:

```py
options = {
  'scales': {
    'x': {

      'type': str # Among 'category', 'linear', 'logarithmic', 'time' | Default: ''
      'position': str # Among 'top', 'left', 'bottom', 'right' | Default: ''
      'offset': bool # Add extra space to the both edges | Default: False
      'id': str # Used to link datasets and scale axis together | Default: ''
      'min': int or str # Minimum value for the scale
                        # str if for category axis | Default: None
      'max': int or str # Maximum value for the scale
                        # str if for category axis | Default: None
      'reverse': bool # Reverses order of tick labels | Default: False
      'suggestedMax': int # Adjustment used when calculating the 
                          # maximum data value | Default: None
      'suggestedMin': int # Adjustment used when calculating the 
                          # minimum data value | Default: None

      # Nested options
      'grid': dict # See Grid Argument below | Default: {}
      'title': dict # See title Argument below | Default: {}
      'ticks': dict # See Ticks Argument below | Default: {}
      'time': dict # See Time Argument below | Default: {}
	
      # Only for time cartesian scales & only when 'type' is set to 'time'
      'beginAtZero': bool # Scale include 0 | Default: True
      'distribution': str # See below | Default: 'linear'
      'bounds': str # See below | Default: 'data'
      
    },
    'y': {
      # You can use the same arguments than above to configure the y axis.
    }
  }
}
```

### Grid argument

As these nested options are common to both cartesian and radial scales, this argument is detailed [at the end of this section](/ipychart/user_guide/scales#grid-argument-3).

### Title argument

This argument allows us to configure the scale title of the Axis. Available options are:

```py
options = {
  'scales': {
    'x': {
      'title': {

        'display': bool # See below | Default: 'linear'
        'text': str # See below | Default: 'linear'
        'font': dict # Configure font (size, style, color, family ...)
        'padding': int or dict # Padding to apply around scale labels 
                               # ex: {'top':10, 'bottom': 20}| Default: 4
                               # Only 'top' and 'bottom' are implemented

      }
    },
    'y': {
      'title': {
        # You can use the same arguments than above to configure the y axis.
      }
    }
  }
}
```

#### Example

Here is an example of a scale with labels:

:::details Click to show the code used to generate the Chart.
<br>

``` py
dataset = {
  'labels': ['Germany','Spain', 'UK', 'Italy', 'Norway', 'France', 'Poland', 
             'Portugal', 'Sweden', 'Ireland'],
  'datasets': [{'data': [14, 106, 16, 107, 45, 133, 19, 109, 60, 107]}]}

options = {
  'scales': {
    'x': {'title': {
      'display': True, 
      'text': 'This is the x Axis', 
      'font': {'size': 20}}},
    'y': {'title': {
      'display': True, 
      'text': 'This is the y Axis', 
      'font': {'size': 20}}}
  }
}


mychart = Chart(dataset, 'bar', options=options, colorscheme='office.Median6')
mychart
```
:::

<scales-labels/>

### Ticks argument

This argument allows us to configure the scale of the Axis. Available options are:

```py
options = {
  'scales': {
    'x': {
      'ticks': {

        # Styling options
        'display': bool # Show tick labels | Default: True
        'font': dict # Configure font (size, style, color, family ...)
        'padding': int # Sets the offset of the tick labels | Default: 0
        'z': int # z-index of tick layer. Values <= 0 are
                 # drawn under datasets, > 0 on top | Default: 0
        
        # Functionnal options
        'sampleSize': int # The number of ticks to examine when deciding
                          # how many labels will fit | Default: Number of ticks
        'autoSkip': bool # If true, automatically calculates how many labels can
                         # be shown and hides labels accordingly | Default: True
        'autoSkipPadding': int # Padding between the ticks on the horizontal 
                  # axis when autoSkip is enabled. | Default: 0
        'labelOffset': int # Distance in pixels to offset the label from 
                           # the center point of the tick | Default: 0
        'maxRotation': int # Maximum rotation for tick labels | Default: 50
        'minRotation': int # Minimum rotation for tick labels | Default: 0
        'mirror': bool # Flips tick labels around axis | Default: False
        'padding': int # Padding between the tick label and the axis | Default: 0
                       # Vertical axis: this applies in the horizontal direction 
                       # Horizontal axis: this applies in the vertical direction

        # Callbacks functions
        'callback': str # Callback function (see below) | Default: ''
        
        # Only for category cartesian scales (work if 'type' is 'category')
        'labels': list of str # An array of labels to display | Default: []

        # Only for time cartesian scales (work if 'type' is 'time')
        'source': str # See below | Default: 'auto'
        
        # Only for numeric cartesian scales 
        # (work if 'type' is 'linear' or 'logarithmic')
        'maxTicksLimit': int # Maximum number of ticks and gridlines to show
                             # Default: 11
        'precision': int # If defined and stepSize is not specified, the step size
                         # is rounded to this many decimal places | Default: None
        'stepSize': int # Fixed step size for the scale | Default: None

      }
    },
    'y': {
      'ticks': {
        # You can use the same arguments than above to configure the y axis.
      }
    }
  }
}
```

#### Callback subargument (`'ticks'` option)

The ticks can be customized with a callback function. A Callback function is a Javascript function inputted into the chart to do some specific actions. To learn how to use callback functions in ipychart, you can read [the callback functions section of the documentation](/ipychart/user_guide/advanced#callback-functions). 

#### Source subargument (`'ticks'` option, only for time scales)

The `'source'` subargument controls the tick's generation **of time scales** (i.e `type` argument = `'time'`):

* `'auto'`: generates "optimal" ticks based on scale size and time options
* `'data'`: generates ticks from data (including labels from data `{t|x|y}` objects)
* `'labels'`: generates ticks from user given `labels` ONLY

#### Example

Here is an example of a scale with custom tick's options:

:::details Click to show the code used to generate the Chart.
<br>

``` py
dataset = {
  'labels': ['Data 1', 'Data 2', 'Data 3', 'Data 4', 'Data 5'],
  'datasets': [
    {'data': [500, 114, 106, 420, 107],
     'label': "Africa"}, 
    {'data': [282, 350, 411, 350, 220],
     'label': "Asia"}, 
    {'data': [168, 170, 250, 380, 480],
     'label': "Europe"}, 
    {'data': [450, 270, 10, 100, 24],
     'label': "Latin America"}, 
    {'data': [6, 40, 200, 300, 350],
     'label': "North America"}
  ]
}

options = {
  'scales': {'x': {'ticks': {'font': {'size': 15, 'style': 'italic'}}},
             'y': {'ticks': {'font': {'size': 15, 'style': 'italic'}, 
                             'stepSize': 100, 'minRotation': 45, 'padding': 20}}
  }
}

mychart = Chart(dataset, 'line', options=options, colorscheme='office.Composite6')
mychart
```
:::

<scales-ticks/>

### Time argument

::: tip
The axis data points may additionally be specified via the 't' or 'x' attribute when using the time scale:
```py
'data': [{'x': datetime or str, 'y': int}, {'t': datetime or str, 'y': int}]
```
:::

```py
options = {
  'scales': {
    'x': {
      'time': {

        'isoWeekday': bool # If True and 'unit' is 'week', then the 
                           # first day of the week is Monday. 
                           # Otherwise, it is Sunday | Default: False
        'parser': str # Custom parser for dates (see below) | Default: ''
        'round': bool # Round dates to the start of this unit | Default: False
        'tooltipFormat': str # Format string to use for the tooltip | Default: ''
        'unit': str # Force unit to be a certain type (see below) | Default: ''
        'stepSize': int # Number of units between grid lines | Default: 1
        'minUnit': str # Minimum display format to be used for 
                       # a time unit | Default: 'millisecond'

        # Nested options
        'displayFormats': dict # See below | Default: {}

      }
    },
    'y': {
      'time': {
        # You can use the same arguments than above to configure the y axis.
      }
    }
  }
}
```


#### Parser subargument (`'time'` option)

If this property is defined as a string, it is interpreted as a custom format to be used by Moment.js to parse the date. See [Moment.js](https://momentjs.com/docs/#/displaying/format/) for the allowable format strings.

If this is a function, it must return a Moment.js object given the appropriate data value.

#### DisplayFormats subargument (`'time'` option)

The following display formats are used to configure how different time units are formed into strings for the axis tick marks. See [Moment.js](https://momentjs.com/docs/#/displaying/format/) for the allowable format strings.

::: warning
You have to change the DisplayFormats dictionary key corresponding to the value of the 'unit' argument. For example, if you set 'unit' to 'week', you will need to use the 'week' key of the DisplayFormats dictionary to see an effective format change.
:::

```py
'options': {
  'scales': {
    'x': {
      'type': 'time',
      'time': {
        'displayFormats': {

          'millisecond': str # | Default: 'h:mm:ss.SSS a'	
          'second': str # | Default: 'h:mm:ss a'
          'minute': str # | Default: 'h:mm a'
          'hour': str # | Default: 'hA'
          'day': str # | Default: 'MMM D'
          'week': str # | Default: 'll'
          'month': str # | Default: 'MMM YYYY'
          'quarter': str # | Default: '[Q]Q - YYYY'
          'year': str # | Default: 'YYYY'

        }
      }
    }
  }
}
```

For example, to set the display format for the `quarter` unit to show the month and year:

```py
'displayFormats': {'quarter': 'MMM YYYY'}
```

#### Example

Here is an example of a chart with a time scale:

:::details Click to show the code used to generate the Chart.
<br>

``` py
data = {"datasets": [
  {'label': "US",
   'data': [{'x': "01/01/2019", 'y': 172},
            {'x': "04/01/2019", 'y': 173},
            {'x': "08/01/2019", 'y': 174},
            {'x': "10/01/2019", 'y': 175},
            {'x': "12/01/2019", 'y': 178},
            {'x': "04/01/2020", 'y': 182}, 
            {'x': "10/01/2020", 'y': 192},
            {'x': "12/01/2020", 'y': 200}],
   'lineTension': 0.3},
  {'label': "UK",
   'data':  [{'x': "01/01/2019", 'y': 175},
             {'x': "04/01/2019", 'y': 177},
             {'x': "08/01/2019", 'y': 182},
             {'x': "10/01/2019", 'y': 172},
             {'x': "12/01/2019", 'y': 184},
             {'x': "04/01/2020", 'y': 192}, 
             {'x': "10/01/2020", 'y': 188},
             {'x': "12/01/2020", 'y': 210}],
   'lineTension': 0.3}]
}

options = {'scales': {
  'x': {      
    'type': 'time',
    'time': {
      'tooltipFormat': 'll',
      'unit': 'week', # change unit from month to week
      'round': 'week', # print only first day of week
      'isoWeekday': True, # monday as first day of week
      'stepSize': 2,# one tick each 2 weeks
      # Change display format
      # see: https://momentjs.com/docs/#/displaying/format/
      'displayFormats': {'week': 'ddd D MMM YYYY'}
    }, # one tick each 2 weeks
      
    'title': {'display': True, 'text': 'Date'}
  },
  'y': {
    'title': {'display': True, 'text': 'Value'}
  }
}}

mychart = Chart(data, 'line', options, colorscheme='tableau.Tableau10')
mychart
```
:::

<scales-time/>

### Distribution argument (time scale)

The `'distribution'` argument controls the data distribution along the scale (**only for time scales**, i.e `type` argument = `'time'`):

* `'linear'`: data is spread according to their time (distances can vary)
* `'series'`: data is spread at the same distance from each other

When the scale is in `series` mode, the data indices are expected to be unique, sorted, and consistent across datasets.

### Bounds argument (time scale)

The `'bounds'` argument controls, **only for time scales** (i.e `type` argument = `'time'`), the scale boundary strategy (bypassed by `'min'`/`'max'` time options):

* `'data'`: makes sure data is fully visible, labels outside are removed
* `'ticks'`: makes sure ticks is fully visible, data outside are truncated

## Radial scale

::: warning
This section only applies to the following types of charts: **radar** & **polarArea**.
:::

**Radial axes are used specifically for the radar and polar area chart types**. These axes overlay the chart area, rather than being positioned on one of the edges. To configure it, you need to use the `'r'` option.

```py
options = {
  'scales': {
    'r': {
    
      # Nested options
      'angleLines': dict # See AngleLines Argument below | Default: {}
      'grid': dict # See Grid Argument below | Default: {}
      'pointLabels': dict # See PointLabels Argument below | Default: {}
      'ticks': dict # See Ticks Argument below | Default: {}

    }
  }
}
```

### AngleLines argument

The following options are used to configure angled lines that radiate from the center of the chart to the point labels. They can be found in the `'angleLines'` sub options of the `'x'` or `'y'` options.

```py
options = {
  'scales': {
    'r': {
      'angleLines': {
  
        'display': bool # Show angled lines | Default: True
        'color': str # Color of angled lines | Default: True
        'lineWidth': int # Width of angled lines | Default: 1
        'borderDash': list # Spacing of dashes on angled lines | Default: []
        'borderDashOffset': float # Offset for line dashes | Default: 0.0

      }
    }
  }
}
```

### Grid argument

As this nested options are common to both cartesian and radial scales, this argument is detailed [at the end of this section](/ipychart/user_guide/scales#grid-argument-3).

### PointLabels argument

The following options are used to configure the point labels that are shown on the perimeter of the scale. They can be found in the `'pointLabels'` sub options.

```py
options = {
  'scales': {
    'r': {
      'pointLabels': {
  
        'display': bool # Show point labels | Default: True
        'font': dict # Configure font (size, style, color, family ...)
          
        # Callbacks functions
        'callback': str # Callback function to convert data labels to point labels.
                        # Default implementation simply returns the current string.

      }
    }
  }
}
```

### Ticks argument

This argument allows us to configure the scale of the Axis. Available options are:

```py
options = {
  'scales': {
    'r': {
      'ticks': {
  
        # Styling options
        'backdropColor': str # Color of label backdrops 
                             # Default: 'rgba(255, 255, 255, 0.75)'
        'backdropPaddingX': int # Horizontal padding of label backdrop | Default: 2
        'backdropPaddingY': int # Vertical padding of label backdrop | Default: 2
        'display': bool # Show tick labels | Default: True
        'font': dict # Configure font (size, style, color, family ...)
        'reverse': bool # Reverses order of tick labels | Default: False
        'padding': int # Sets the offset of the tick labels | Default: 0
        'z': int # z-index of tick layer. Values <= 0 are
                 # drawn under datasets, > 0 on top | Default: 0
            
        # Functionnal options
        'min': int or str # Minimum value for the scale
                          # str if for category axis | Default: None
        'max': int or str # Maximum value for the scale
                          # str if for category axis | Default: None
        'maxTicksLimit': int # Maximum number of ticks and gridlines to show
                             # Default: 11
        'precision': int # If defined and stepSize is not specified, the step size 
                         # is rounded to this many decimal places | Default: None
        'stepSize': int # Fixed step size for the scale | Default: None
        'suggestedMax': int # Adjustment used when calculating the 
                            # maximum data value | Default: None
        'suggestedMin': int # Adjustment used when calculating the 
                            # minimum data value | Default: None
        'showLabelBackdrop': bool # Scale include 0 | Default: True
  
        # Callbacks functions
        'callback': str # Callback function (see below) | Default: ''

      }
    }
  }
}
```

#### Callback subargument (`'ticks'` option)

The ticks can be customized with a callback function. A Callback function is a Javascript function inputted into the chart to do some specific actions. To learn how to use callback functions in ipychart, you can read [the callback functions section of the documentation](/ipychart/user_guide/advanced#callback-functions).

### Example

Here is an example of a radial scale with custom angleLines, grid, pointLabels and ticks options:

:::details Click to show the code used to generate the Chart.
<br>

``` py
dataset = {
  'labels': ['Top', 'TopRight', 'BottomRight', 'Bottom', 
             'BottomLeft', 'TopLeft'],
  'datasets': [
    {'data': [140, 106, 160, 107, 45, 27],
     'label': 'Dataset 1',
     'borderWidth': 3,
     'lineTension': 0.3},
    {'data': [32, 160, 72, 140, 89, 112],
     'label': 'Dataset 2',
     'borderWidth': 3,
     'lineTension': 0.3}]
}

options = {
  'scales': {
    'r': {
      'display': True,
      'color': 'black',
      'lineWidth': 1.5,
      'borderDashOffset': 10,
      'angleLines': {
        'display': True,
        'color': 'black',
        'lineWidth': 1.5,
        'borderDashOffset': 10
      },
      'grid': {
        'color': 'black',
        'lineWidth': 1.5,
        'circular': True
      },
      'pointLabels': {
        'display': True,
        'font': {'size': 14, 'color': 'black', 'style': 'italic'},
      },
      'ticks': {
        'font': {'size': 18, 'color': 'black'},
        'stepSize': 30
      }
    }
  }
}

mychart = Chart(dataset, 'radar', options=options, colorscheme='brewer.DarkTwo3')
mychart
```
:::

<scales-radial/>

## Common options

### Grid argument

The grid argument is common to all scales. Therefore, for reasons of clarity and readability of the documentation, the detailed description of its options was placed here, at the end of this section.

This argument defines options for the grid lines that run perpendicular to the axis. Available options are:

```py
options = {
  # CARTESIAN AXIS
  'scales': {
    'x': {
      'grid': {

        'display': bool # Display grid lines for this axis | Default: True
        'circular': str # Circular gridlines (radar chart only) | Default: False
        'color': str # Gridlines color | Default: 'rgba(0, 0, 0, 0.1)'
        'borderDash': list # Spacing of dashes on grid lines | Default: []
        'borderDashOffset': float # Offset for line dashes | Default: 0.0
        'lineWidth': int or list # Stroke width of grid lines | Default: 1
        'drawBorder': bool # Draw border of the chart | Default: True
        'drawOnChartArea': bool # Draw lines inside the axis lines | Default: True
        'drawTicks': bool # Draw lines beside the ticks | Default: True
        'tickMarkLength': int # Length of tick marks | Default: 10
        'offsetGridLines': bool # Shift grid lines between labels | Default: False
        'z': int # z-index of gridline layer. Values <= 0 are
                 # drawn under datasets, > 0 on top | Default: 0

      }
    },
    'y': {
      'grid': {
        # You can use the same arguments than above to configure the y axis.
      }
    },
    'r': {
      'grid': {
        # You can use the same arguments than above to configure the radial axis.
      }
    }
  }
}
```

#### Example

Here is an example of a scale with custom grid options:

:::details Click to show the code used to generate the Chart.
<br>

``` py
dataset = {
  'labels': ['Germany','Spain', 'UK', 'Italy', 'Norway', 'France', 'Poland', 
             'Portugal', 'Sweden', 'Ireland'],
  'datasets': [{'data': [14, 106, 16, 107, 45, 133, 19, 109, 60, 107],
                'label': 'Dataset 1', 'fill': True},
               {'data': [95, 28, 56, 82, 37, 155, 120, 132, 74, 85],
                'label': 'Dataset 2', 'fill': True}]
}

options = {
  'scales': {
    'x': {
      'grid': {
      'display': True,
      'color': 'black',
      'z': -1}},
    'y': {
      'grid': {
      'display': True,
      'color': 'black',
      'z': -1}}
  }
}


mychart = Chart(dataset, 'line', options=options, colorscheme='tableau.JewelBright9')
mychart
```
:::

<scales-gridlines/>
