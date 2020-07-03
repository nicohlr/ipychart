# Scales

This section is dedicated to the `'scales'` argument of the options dict that you'll pass to your Chart. As the other arguments described if the [previous section](), the scales argument is a key of the `options` dict. However, as it has a lot of possible nested configurations, a whole section of the documentation is dedicated to it. 

With the `'scales'` argument, you can completely configure the axis of your chart. This configuration involves configuring the two axis of your Chart: the x axis and the y axis.

All charts doesn't have the same type of scales. There are two types of scales available in ipychart:
* [**The Cartesian Scale**](), used for the following types of chart: line, bar, horizontalBar, bubble, scatter. These charts have two axes positioned on one of the edges (the **x** axis and the **y** axis). You can configure them using the `'scales'` option.

* [**The Radial Scale**](), used for the following types of chart: radar, polarArea. These charts have only one axis which overlay the chart area. You can configure it using the `'scale'` option.

The other types of charts (doughnut, pie) do not use scales.

::: tip
In this part, the term **arguments** corresponds to the options of the main dictionnaries, whereas the term **subarguments** corresponds to the options of the nested dictionnaries (`'ticks'` and `'time'` sub-dictionnaries for example)
:::

## Cartesian scale

::: warning
This section only applies to the following types of charts: **line**, **bar**, **horizontalBar**, **bubble** & **scatter**.
:::

Axis that follow a cartesian grid are known as 'Cartesian Axis'. **Cartesian axis are used for line, bar, and bubble charts**. To configure your axes, you'll have to use the `'scales'` option and the `'xAxes'` and `'yAxes'` sub-options.

The following options are available:

```py
options = {
  'scales': {
    'xAxes': [{

      'type': str # Among 'category', 'linear', 'logarithmic', 'time' | Default: ''
      'position': str # Among 'top', 'left', 'bottom', 'right' | Default: ''
      'offset': bool # Add extra space to the both edges | Default: False
      'id': str # Used to link datasets and scale axis together | Default: ''

      # Nested options
      'gridLines': dict # See GridLines Argument below | Default: {}
      'scaleLabel': dict # See ScaleLabel Argument below | Default: {}
      'ticks': dict # See Ticks Argument below | Default: {}
      'time': dict # See Time Argument below | Default: {}
	
      # Only for time cartesian scales (work if type is 'time')
      'distribution': str # See below | Default: 'linear'
      'bounds': str # See below | Default: 'data'
      
    }],
    'yAxes': [{
      # You can use the same arguments than above to configure the y axis.
    }]
  }
}
```

::: tip
`'xAxes'` and `'yAxes'` are lists, each element of the list corresponds to the scale of a dataset. Therefore, the lenght of the `'xAxes'` and `'yAxes'` lists must be equal to the number of dataset passed to the chart.
:::

### GridLines argument

As this nested options are common to both cartesian and radial scales, this argument is detailed [at the end of this section]().

### ScaleLabel argument

This argument allows to configure the scale title of the Axis. Available options are:

```py
options = {
  'scales': {
    'xAxes': [{
      'scaleLabel': {

        'display': bool # See below | Default: 'linear'
        'labelString': str # See below | Default: 'linear'
        'lineHeight': int or str # Height of an individual line of text
                                 # ex: 2.4 or '100%' | Default: 1.2
        'fontColor': str # Font color for scale title | Default: '#666'
        'fontFamily': str # Font family for the scale title | Default: 'Helvetica'
        'fontSize': int # Font size for scale title | Default: 12
        'fontStyle': # Font style for the scale title ('normal', 'italic', 
                     # 'oblique', 'initial', 'inherit') | Default: 'normal'
        'padding': int or dict # Padding to apply around scale labels 
                               # ex: {'top':10, 'bottom': 20}| Default: 4
                               # Only 'top' and 'bottom' are implemented

      }
    }],
    'yAxes': [{
      'scaleLabel': {
        # You can use the same arguments than above to configure the y axis.
      }
    }]
  }
}
```

#### Example

Here is an example of a scale with labels:

:::details Click to show the code used to generate the Chart.
<br/>

``` py
dataset = {
    'labels': ['Germany','Spain', 'UK', 'Italy', 'Norway', 'France', 'Poland', 
               'Portugal', 'Sweden', 'Ireland'],
    'datasets': [{'data': [14, 106, 16, 107, 45, 133, 19, 109, 60, 107]}]}

options = {
  'scales': {
    'xAxes': [{'scaleLabel': {
      'display': True, 
      'labelString': 'This is the x Axis', 
      'fontSize': 20}}],
    'yAxes': [{'scaleLabel': {
      'display': True, 
      'labelString': 'This is the y Axis', 
      'fontSize': 20}}]
  }
}


mychart = Chart(dataset, 'bar', options=options, colorscheme='office.Median6')
mychart
```
:::

<scales-labels/>

### Ticks argument

This argument allows to configure the scale of the Axis. Available options are:

```py
options = {
  'scales': {
    'xAxes': [{
      'ticks': {

        # Styling options
        'display': bool # Show tick labels | Default: True
        'fontColor': str # Font color for tick labels | Default: '#666'
        'fontFamily': str # Font family for the tick labels | Default: 'Helvetica'
        'fontSize': int # Font size for the tick labels | Default: 12
        'fontStyle': str # Font style for the tick labels ('normal', 'italic', 
                         # 'oblique', 'initial', 'inherit') | Default: 'normal'
        'lineHeight': int or str # Height of an individual line of text
                                 # ex: 2.4 or '100%' | Default: 1.2
        'reverse': bool # Reverses order of tick labels | Default: False
        'padding': int # Sets the offset of the tick labels | Default: 0
        'z': int # z-index of tick layer. Values <= 0 are
                 # drawn under datasets, > 0 on top | Default: 0
        
        # Functionnal options
        'min': int or str # Minimum value for the scale
                          # str if for category axis | Default: None
        'max': int or str # Maximum value for the scale
                          # str if for category axis | Default: None
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
                
        # Nested options
        'minor': str # See below | Default: {}
        'major': str # See below | Default: {}

        # Callbacks options
        'callback': str # Callback function (see below) | Default: ''
        
        # Only for category cartesian scales (work if 'type' is 'category')
        'labels': list of str # An array of labels to display | Default: []

        # Only for time cartesian scales (work if 'type' is 'time')
        'source': str # See below | Default: 'auto'
        
        # Only for numeric cartesian scales 
        # (work if 'type' is 'linear' or 'logarithmic')
        'beginAtZero': bool # Scale include 0 | Default: True
        'maxTicksLimit': int # Maximum number of ticks and gridlines to show
                             # Default: 11
        'precision': int # If defined and stepSize is not specified, the step size
                         # is rounded to this many decimal places | Default: None
        'stepSize': int # Fixed step size for the scale | Default: None
        'suggestedMax': int # Adjustment used when calculating the 
                            # maximum data value | Default: None
        'suggestedMin': int # Adjustment used when calculating the 
                            # minimum data value | Default: None

      }
    }],
    'yAxes': [{
      'ticks': {
        # You can use the same arguments than above to configure the y axis.
      }
    }]
  }
}
```

#### Minor and Major subarguments (`'ticks'` options)

The minor and major tick configuration are nested under the ticks configuration in the respective `'minor'` and `'major'` key. As this nested options are common to both cartesian and radial scales, these options are detailed [at the end of this section]().

#### Callback subargument (`'ticks'` option)

The ticks can be customized with a callback function. Callback function are javascript function inputed into the chart to do some specific actions. To learn how to use callback function in ipychart, you can read [the callback functions section of the documentation](https://github.com/nicohlr/ipychart/blob/master/docs/docs/user_guide). 

#### Source subargument (`'ticks'` option, only for time scales)

The `'source'` subargument controls the ticks generation **for time scales** (i.e `type` argument = `'time'`):

* `'auto'`: generates "optimal" ticks based on scale size and time options
* `'data'`: generates ticks from data (including labels from data `{t|x|y}` objects)
* `'labels'`: generates ticks from user given `labels` ONLY

#### Example

Here is an example of a scale with custom ticks options:

:::details Click to show the code used to generate the Chart.
<br/>

``` py
dataset = {
    'labels': ['Dataset 1', 'Dataset 2', 'Dataset 3', 'Dataset 4',
               'Dataset 5'],
    'datasets': [{ 
        'data': [500, 114, 106, 420, 107],
        'label': "Africa",
        'fill': False
      }, { 
        'data': [282, 350, 411, 350, 220],
        'label': "Asia",
        'fill': False
      }, { 
        'data': [168, 170, 250, 380, 480],
        'label': "Europe",
        'fill': False
      }, { 
        'data': [450, 270, 10, 100, 24],
        'label': "Latin America",
        'fill': False
      }, { 
        'data': [6, 40, 200, 300, 350],
        'label': "North America",
        'fill': False
      }
    ]
  }

options = {
    'scales': {'xAxes': [{'ticks': {
                   'min': 0, 'max': 500, 'fontSize': 15, 'fontStyle': 'italic', 'stepSize': 0.5,'maxTicksLimit': 100}}],
               'yAxes': [{'ticks': {
                   'min': 0, 'max': 500, 'fontSize': 15, 'fontStyle': 'italic', 'stepSize': 50, 'minRotation': 45, 'padding': 20,}}]}
}

mychart = chart.Chart(dataset, 'line', options=options)
mychart
```
:::

<scales-ticks-cartesian/>

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
    'xAxes': [{
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
    }],
    'yAxes': [{
      'time': {
        # You can use the same arguments than above to configure the y axis.
      }
    }]
  }
}
```

#### DisplayFormats subargument (`'time'` option)

The following display formats are used to configure how different time units are formed into strings for the axis tick marks. See [Moment.js](https://momentjs.com/docs/#/displaying/format/) for the allowable format strings.

```py
'options': {
  'scales': {
    'xAxes': [{
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
    }]
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
<br/>

``` py

```
:::

<scales-time/>

### Distribution argument (only for time scales)

The `'distribution'` argument controls the data distribution along the scale (**only for time scales**, i.e `type` argument = `'time'`):

* `'linear'`: data are spread according to their time (distances can vary)
* `'series'`: data are spread at the same distance from each other

When the scale is in `series` mode, the data indices are expected to be unique, sorted, and consistent across datasets.

### Bounds argument (only for time scales)

The `'bounds'` argument controls, **only for time scales** (i.e `type` argument = `'time'`), the scale boundary strategy (bypassed by `'min'`/`'max'` time options):

* `'data'`: makes sure data are fully visible, labels outside are removed
* `'ticks'`: makes sure ticks are fully visible, data outside are truncated

## Radial scale

::: warning
This section only applies to the following types of charts: **radar** & **polarArea**.
:::

**Radial axis are used specifically for the radar and polar area chart types**. These axis overlay the chart area, rather than being positioned on one of the edges. To configure it, you need to use the `'scale'` option (without 's', as radar and polarArea charts only have one axis).

```py
options = {
  'scale': {
  
    # Nested options
    'angleLines': dict # See AngleLines Argument below | Default: {}
    'gridLines': dict # See GridLines Argument below | Default: {}
    'pointLabels': dict # See PointLabels Argument below | Default: {}
    'ticks': dict # See Ticks Argument below | Default: {}
    
  }
}
```

### AngleLines argument

The following options are used to configure angled lines that radiate from the center of the chart to the point labels. They can be found in the `'angleLines'` sub options of the `'xAxes'` or `'yAxes'` options.

```py
options = {
  'scale': {
    'angleLines': {

      'display': bool # Show angled lines | Default: True
      'color': str # Color of angled lines | Default: True
      'lineWidth': int # Width of angled lines | Default: 1
      'borderDash': list # Spacing of dashes on angled lines | Default: []
      'borderDashOffset': float # Offset for line dashes | Default: 0.0
      
    }
  }
}
```

#### Example

Here is an example of a scale with custom angleLines options:

:::details Click to show the code used to generate the Chart.
<br/>

``` py

```
:::

<scales-anglelines/>

### GridLines argument

As this nested options are common to both cartesian and radial scales, this argument is detailed [at the end of this section]().

### PointLabels argument

The following options are used to configure the point labels that are shown on the perimeter of the scale. They can be found in the `'pointLabels'` sub options.

```py
options = {
  'scale': {
    'pointLabels': {

      'display': bool # Show point labels | Default: True
      'fontColor': str # Font color for point labels | Default: '#666'
      'fontFamily': str # Font family for the point labels | Default: 'Helvetica'
      'fontSize': int # Font size for the point labels | Default: 12
      'fontStyle': str # Font style for the point labels ('normal', 'italic', 
                       # 'oblique', 'initial', 'inherit') | Default: 'normal'
      'lineHeight': int or str # Height of an individual line of text
                               # ex: 2.4 or '100%' | Default: 1.2
        
      # Callbacks options
      'callback': str # Callback function to convert data labels to point labels.
                      # Default implementation simply returns the current string.

    }
  }
}
```

#### Example

Here is an example of a scale with custom pointLabels options:

:::details Click to show the code used to generate the Chart.
<br/>

``` py

```
:::

<scales-pointlabels/>

### Ticks argument

This argument allows to configure the scale of the Axis. Available options are:

```py
options = {
  'scale': {
    'ticks': {

      # Styling options
      'backdropColor': str # Color of label backdrops 
                           # Default: 'rgba(255, 255, 255, 0.75)'
      'backdropPaddingX': int # Horizontal padding of label backdrop | Default: 2
      'backdropPaddingY': int # Vertical padding of label backdrop | Default: 2
      'display': bool # Show tick labels | Default: True
      'fontColor': str # Font color for tick labels | Default: '#666'
      'fontFamily': str # Font family for the tick labels | Default: 'Helvetica'
      'fontSize': int # Font size for the tick labels | Default: 12
      'fontStyle': str # Font style for the tick labels ('normal', 'italic', 
                       # 'oblique', 'initial', 'inherit') | Default: 'normal'
      'lineHeight': int or str # Height of an individual line of text
                               # ex: 2.4 or '100%' | Default: 1.2
      'reverse': bool # Reverses order of tick labels | Default: False
      'padding': int # Sets the offset of the tick labels | Default: 0
      'z': int # z-index of tick layer. Values <= 0 are
               # drawn under datasets, > 0 on top | Default: 0
          
      # Functionnal options
      'beginAtZero': bool # Scale include 0 | Default: True
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
        
      # Nested options
      'minor': str # Same as for cartesion scale, see above | Default: {}
      'major': str # Same as for cartesion scale, see above | Default: {}

      # Callbacks options
      'callback': str # Callback function (see below) | Default: ''
      
    }
  }
}
```

#### Minor and Major subarguments (`'ticks'` options)

The minor and major tick configuration are nested under the ticks configuration in the respective `'minor'` and `'major'` key. As this nested options are common to both cartesian and radial scales, these options are detailed [at the end of this section]().

#### Callback subargument (`'ticks'` option)

The ticks can be customized with a callback function. Callback function are javascript function inputed into the chart to do some specific actions. To learn how to use callback function in ipychart, you can read [the callback functions section of the documentation](https://github.com/nicohlr/ipychart/blob/master/docs/docs/user_guide).

#### Example

Here is an example of a scale with custom ticks options:

:::details Click to show the code used to generate the Chart.
<br/>

``` py

```
:::

<scales-ticks-radial/>

## Common options

### GridLines argument

The gridLines argument is common to both scales. Therefore, for reasons of clarity and readability of the documentation, the detailed description of its options was placed here, at the end of this section. The only difference is where to input the gridlines configuration:

- For the cartesian axis, you can use the `'scales'` option
- For the radial axis, you can use the `'scale'` option

This argument defines options for the grid lines that run perpendicular to the axis. Available options are:

```py
options = {
  # CARTESIAN AXIS
  'scales': {
    'xAxes': [{
      'gridLines': {

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
        'zeroLineWidth': int # Stroke width of the first grid line | Default: 1
        'zeroLineColor': str # Color of the first grid line
                             # Default: 'rgba(0, 0, 0, 0.25)'
        'zeroLineBorderDash': list # Spacing of dash of the first grid line
                                   # Default: []
        'zeroLineBorderDashOffset': float # Offset of the first grid line dash
                                          # Default: 0.0
        'offsetGridLines': bool # Shift grid lines between labels | Default: False
        'z': int # z-index of gridline layer. Values <= 0 are
                 # drawn under datasets, > 0 on top | Default: 0

      }
    }],
    'yAxes': {
      'gridLines': {
        # You can use the same arguments than above to configure the y axis.
      }
    }
  }
  # RADIAL AXIS
  'scale': {
    'gridLines': {
	  # For radial axis, use the 'scale' option instead of 'scales' to configure gridlines
    }
  }
}
```

#### Example

Here is an example of a scale with custom gridLines options:

:::details Click to show the code used to generate the Chart.
<br/>

``` py

```
:::

<scales-gridlines/>

### Ticks argument

The minor and major ticks options are common to both scales. Therefore, for reasons of clarity and readability of the documentation, the detailed description of these options was placed here, at the end of this section.

#### Minor subarguments (`'ticks'` options)

The minor tick configuration is nested under the ticks configuration in the `'minor'` key. It defines options for the minor tick marks that are generated by the axis (omitted options are inherited from ticks configuration):

```py
options = {
  'scales': {
    'xAxes': [{
      'ticks': {
        'minor': {

          'fontColor': str # Font color for tick labels | Default: '#666'
          'fontFamily': str # Font family for the tick labels | Default: 'Helvetica'
          'fontSize': int # Font size for the tick labels | Default: 12
          'fontStyle': str # Font style for the tick labels ('normal', 'italic', 
                           # 'oblique', 'initial', 'inherit') | Default: 'normal'
          'lineHeight': int or str # Height of an individual line of text
                                   # ex: 2.4 or '100%' | Default: 1.2
                
          # Callbacks options
          'callback': str # Callback function which returns the string 
                          # representation of the tick value as it should 
                          # be displayed on the chart. | Default: ''

        }
      }
    }]
  }
}
```

#### Major subarguments (`'ticks'` options)

The major tick configuration is nested under the ticks configuration in the `'major'` key. It defines options — these options are disabled by default — for the major tick marks that are generated by the axis (omitted options are inherited from ticks configuration): 

```py
options = {
  'scales': {
    'xAxes': [{
      'ticks': {
        'major': {

          'enabled': bool # If True, major tick options are used
                          # to show major ticks | Default: False
          'fontColor': str # Font color for tick labels | Default: '#666'
          'fontFamily': str # Font family for the tick labels | Default: 'Helvetica'
          'fontSize': int # Font size for the tick labels | Default: 12
          'fontStyle': str # Font style for the tick labels ('normal', 'italic', 
                           # 'oblique', 'initial', 'inherit') | Default: 'normal'
          'lineHeight': int or str # Height of an individual line of text
                                   # ex: 2.4 or '100%' | Default: 1.2
                
          # Callbacks options
          'callback': str # Callback function which returns the string 
                          # representation of the tick value as it should 
                          # be displayed on the chart. | Default: ''

        }
      }
    }]
  }
}
```