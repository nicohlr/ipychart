# Scales

This section is dedicated to the `'scales'` argument of the options dict that you'll pass to your Chart. As the arguments described if the [previous section](), the scales argument is a key of the `options` dict. However, as it has a lot of possible nested configurations, a whole section of the documentation is dedicated to it. 

With the `'scales'` argument, you can completely configure the axis of your chart. For example, you can add titles to each axis, choose the axis range, hide the axis ... This configuration involves configuring the two axis of your Chart: the x axis and the y axis.

All charts doesn't have the same type of scales. There are two types of scales available in ipychart:
* **The Cartesian Axis**, used for the following types of chart: line, bar, horizontalBar, bubble.
* **The Radial Axis**, used for the following types of chart: radar, polarArea.

The other types of charts (doughnut, pie) do not use scales.

## Cartesian

Axis that follow a cartesian grid are known as 'Cartesian Axis'. **Cartesian axis are used for line, bar, and bubble charts**. You can configure the cartesian axis using the following options:

```py
options = {
  'scales': {
    'xAxes': {

      'type': str # See below | Default: ''
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
      
    }
    'yAxes': {
      # You can use the same arguments than above to configure the y axis.
    }
  }
}
```

#### Type property

The `'type'` property controls the of scale being employed. It can be one of the following cartesian scales:

* `'category'`
* `'linear'`
* `'logarithmic'`
* `'time'`

#### Distribution property

The `'distribution'` property controls the data distribution along the scale (**for time scales**):

* `'linear'`: data are spread according to their time (distances can vary)
* `'series'`: data are spread at the same distance from each other

When the scale is in `series` mode, the data indices are expected to be unique, sorted, and consistent across datasets.

#### Bounds property

The `'bounds'` property controls, **for time scales**, the scale boundary strategy (bypassed by `'min'`/`'max'` time options):

* `'data'`: makes sure data are fully visible, labels outside are removed
* `'ticks'`: makes sure ticks are fully visible, data outside are truncated

### GridLines argument

This argument defines options for the grid lines that run perpendicular to the axis. Available options are:

```py
options = {
  'scales': {
    'xAxes': {
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
    }
    'yAxes': {
      'gridLines': {
        # You can use the same arguments than above to configure the y axis.
      }
    }
  }
}
```

### ScaleLabel argument

This argument allows to configure the scale title of the Axis. Available options are:

```py
options = {
  'scales': {
    'xAxes': {
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
    }
    'yAxes': {
      'scaleLabel': {
        # You can use the same arguments than above to configure the y axis.
      }
    }
  }
}
```

### Ticks argument

This argument allows to configure the scale of the Axis. Available options are:

```py
options = {
  'scales': {
    'xAxes': {
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
    }
    'yAxes': {
      'ticks': {
        # You can use the same arguments than above to configure the y axis.
      }
    }
  }
}
```

#### Minor and Major arguments

The minor tick configuration is nested under the ticks configuration in the `'minor'` key. It defines options for the minor tick marks that are generated by the axis (omitted options are inherited from ticks configuration):

```py
options = {
  'scales': {
    'xAxes': {
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
    }
  }
}
```

The major tick configuration is nested under the ticks configuration in the `'major'` key. It defines options — these options are disabled by default — for the major tick marks that are generated by the axis (omitted options are inherited from ticks configuration): 

```py
options = {
  'scales': {
    'xAxes': {
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
    }
  }
}
```

#### Callback argument

The ticks can be customized with a callback function. Callback function are javascript function inputed into the chart to do some specific actions. To learn how to use callback function in ipychart, you can read [the callback functions section of the documentation](https://github.com/nicohlr/ipychart/blob/master/docs/docs/user_guide). To do this, you need to override the ticks.callback method in the axis configuration. In the following example, every label of the Y axis would be displayed with a dollar sign at the front.

```py 
'options': {
  'scales': {
    'yAxes': [{
      'ticks': {

        # The callback is a JS function in a python string
        # The function must returns the string representation 
        # of the tick value as it should be displayed on the chart.
        'callback': 
          '''
          function(value, index, values) {return '$' + value;}
          '''
          # This function will include a dollar sign in the ticks

       }
    }]
  }
}
```

#### Source property

The `'source'` property controls the ticks generation **for time scales**:

* `'auto'`: generates "optimal" ticks based on scale size and time options
* `'data'`: generates ticks from data (including labels from data `{t|x|y}` objects)
* `'labels'`: generates ticks from user given `labels` ONLY

### Time argument

::: tip
The axis data points may additionally be specified via the 't' or 'x' attribute when using the time scale:
```py
'data': [{
    'x': datetime or str,
    'y': 1
}, {
    't': datetime or str,
    'y': 10
}]
```
:::

```py
options = {
  'scales': {
    'xAxes': {
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
    }
    'yAxes': {
      'time': {
        # You can use the same arguments than above to configure the y axis.
      }
    }
  }
}
```

#### DisplayFormats argument

The following display formats are used to configure how different time units are formed into strings for the axis tick marks. See [Moment.js](https://momentjs.com/docs/#/displaying/format/) for the allowable format strings.

Name | Default | Example
--- | --- | ---
`millisecond` | `'h:mm:ss.SSS a'` | `'11:20:01.123 AM'`
`second` | `'h:mm:ss a'` | `'11:20:01 AM'`
`minute` | `'h:mm a'` | `'11:20 AM'`
`hour` | `'hA'` | `'11AM'`
`day` | `'MMM D'` | `'Sep 4'`
`week` | `'ll'` | `'Sep 4 2015'`
`month` | `'MMM YYYY'` | `'Sep 2015'`
`quarter` | `'[Q]Q - YYYY'` | `'Q3 - 2015'`
`year` | `'YYYY'` | `'2015'`

For example, to set the display format for the `quarter` unit to show the month and year, the following config would be passed to the chart constructor.

```py
'options': {
  'scales': {
    'xAxes': {
      'type': 'time',
      'time': {
        'displayFormats': {
          'quarter': 'MMM YYYY'
        }
      }
    } 
  }
}
```

## Radial

**Radial axis are used specifically for the radar and polar area chart types**. These axis overlay the chart area, rather than being positioned on one of the edges.

```py
options = {
  'scales': {
    'xAxes': {

      # Nested options
      'angleLines': dict # See AngleLines Argument below | Default: {}
      'gridLines': dict # See GridLines Argument below | Default: {}
      'pointLabels': dict # See PointLabels Argument below | Default: {}
      'ticks': dict # See Ticks Argument below | Default: {}

    }
    'yAxes': {
      # You can use the same arguments than above to configure the y axis.
    }
  }
}
```

### Tick argument

This argument allows to configure the scale of the Axis. Available options are:

```py
options = {
  'scales': {
    'xAxes': {
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
        'minor': str # See below | Default: {}
        'major': str # See below | Default: {}

        # Callbacks options
        'callback': str # Callback function (see below) | Default: ''

      }
    }
    'yAxes': {
      'ticks': {
        # You can use the same arguments than above to configure the y axis.
      }
    }
  }
}
```

### AngleLines argument

The following options are used to configure angled lines that radiate from the center of the chart to the point labels. They can be found in the `'angleLines'` sub options of the `'xAxes'` or `'yAxes'` options.

```py
options = {
  'scales': {
    'xAxes': {
      'angleLines': {

        'display': bool # Show angled lines | Default: True
        'color': str # Color of angled lines | Default: True
        'lineWidth': int # Width of angled lines | Default: 1
        'borderDash': list # Spacing of dashes on angled lines | Default: []
        'borderDashOffset': float # Offset for line dashes | Default: 0.0

      }
    }
    'yAxes': {
      'angleLines': {
        # You can use the same arguments than above to configure the y axis.
      }
    }
  }
}
```

### PointLabels argument

The following options are used to configure the point labels that are shown on the perimeter of the scale. They can be found in the `'pointLabels'` sub options.

```py
options = {
  'scales': {
    'xAxes': {
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
    'yAxes': {
      'pointLabels': {
        # You can use the same arguments than above to configure the y axis.
      }
    }
  }
}
```

## Examples

Here are examples of what you can do to with the scales options (not exhaustive):

### Custom cartesian axis

```py
```

### Custom radial axis

```py
```

### Multiple axis

```py
```
