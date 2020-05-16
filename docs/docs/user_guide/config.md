# Configuration

The options argument of the chart allows you to configure the chart as you want. In this section, we will go through each arguments of the options dict that you'll pass to your chart instance. Each of them allows you to configure a specific aspect of your chart.

## Scales

### Scales options

With this argument, you can configure the scales of your chart. For example, you can add titles to each axis, choose the scale range, hide the scales ... To do that, you'll have to feed a dict to the scales argument of the options dict. This dict can have many properties, detailed below:

``` py
options = {
  'scales': {

    'xAxes': {
      ##############################TODO######################################
      'display': bool # Show the legend | Default: True (if multiple datasets)
      'position': str # Position ('top', 'left', 'right', 'bottom') | Default: 'top'
      'align': str # Alignment ('start', 'center', 'end') | Default: 'center'
      'fullWidth': bool # Use full width of container | Default: True
      'onClick': str # Callback function (see below) | Default: ''
      'onHover': str # Callback function (see below) | Default: ''
      'onLeave': str # Callback function (see below) | Default: ''
      'reverse': bool #  Show datasets in reverse order | Default: False
      'rtl': bool # Rendering the legends from right to left | Default: True
    }

    'yAxes': {
      # You can use te same arguments than above to configure the y axis.
    }
  }
}
```

### Example of a chart with custom scales

Here is a example of what you can do to with the scales options (not exhaustive):

``` py

```

And the output:

<options-scales/>

## Title

### Title options

With this argument, you can configure the scales of your chart. For example, you can add titles to each axis, choose the scale range, hide the scales ... To do that, you'll have to feed a dict to the scales argument of the options dict. This dict can have many properties, detailed below:

``` py
options = {
  'title': {   
    
    'text': str or list # Title text | Default: ''
                        # If list, text is written on multiple lines 
    'display': bool # Show the legend | Default: True (if multiple datasets)
    'position': str # Position ('top', 'left', 'right', 'bottom') | Default: 'top'
    'fontSize': int # Font size of text | Default: 12'
    'fontStyle': str # Font style of text (ex: 'bold') | Default: 'normal'
    'fontColor': str # Font style of text | Default: '#666'
    'fontFamily': str # Font style of text (ex: 'Arial') | Default: 'Helvetica'
    'padding': int # Padding between rows of colored boxes | Default: 10

  }
}
```

#### Callbacks functions

Some of the arguments can be filled with callback functions. Callback function are javascript function inputed into the chart to do some specific actions. To learn how to use callback function in ipychart, you can read [the callback functions section of the documentation]().

### Example of a chart with a title

Here is a example of what you can do to with the scales options (not exhaustive):

``` py

```

And the output:

<options-title/>

## Legend

::: tip
Unlike Chart.js, ipychart will display a legend only for Charts containing more than one dataset.
:::

### Legend options

With this argument, you can configure the scales of your chart. For example, you can add titles to each axis, choose the scale range, hide the scales ... To do that, you'll have to feed a dict to the scales argument of the options dict. This dict can have many properties, detailed below:

``` py
options = {
  'legend': {   

    'display': bool # Show the legend | Default: True (if multiple datasets)
    'position': str # Position ('top', 'left', 'right', 'bottom') | Default: 'top'
    'align': str # Alignment ('start', 'center', 'end') | Default: 'center'
    'fullWidth': bool # Use full width of container | Default: True
    'onClick': str # Callback function (see below) | Default: ''
    'onHover': str # Callback function (see below) | Default: ''
    'onLeave': str # Callback function (see below) | Default: ''
    'reverse': bool # Show datasets in reverse order | Default: False
    'rtl': bool # Rendering the legends from right to left | Default: True
    
    # Nested options
    'labels': dict # See below | Default: {}

  }
}
```

#### Callbacks functions

Some of the arguments can be filled with callback functions. Callback function are javascript function inputed into the chart to do some specific actions. To learn how to use callback function in ipychart, you can read [the callback functions section of the documentation]().

#### Labels argument

The legend label configuration is nested below the legend configuration using the labels key. It is a dict that can contains the followings arguments:

``` py
options = {
  'legend': {   
    'labels': {

      'boxWidth': int # Width of coloured box | Default: 40   
      'fontSize': int # Font size of text | Default: 12'
      'fontStyle': str # Font style of text (ex: 'bold') | Default: 'normal'
      'fontColor': str # Font style of text | Default: '#666'
      'fontFamily': str # Font style of text (ex: 'Arial') | Default: 'Helvetica'
      'padding': int # Padding between rows of colored boxes | Default: 10
      'generateLabels': str # Callback function (see below) | Default: ''
      'filter': str #  Callback function (see below) | Default: ''
      'usePointStyle': bool # Use style of point in legend | Default: False

    }
  }
}
```

### Example of a chart with a legend

Here is a example of what you can do to with the scales options (not exhaustive):

``` py

```

And the output:

<options-legend/>

## Tooltips

### Tooltips options

With this argument, you can configure the scales of your chart. For example, you can add titles to each axis, choose the scale range, hide the scales ... To do that, you'll have to feed a dict to the scales argument of the options dict. This dict can have many properties, detailed below:

``` py
options = {
  'tooltips': {  
     
    # General options
    'enabled': bool # Are tooltips enabled | Default: True
    'mode': str # Which elements appear in the tooltip | Default: 'nearest'
    'intersect': bool # If true, the tooltip mode applies only when the mouse
                      # position intersects with an element | Default: True
    'position': str # See below) | Default: 'average'
    'backgroundColor': str # Background color | Default: 'rgba(0, 0, 0, 0.8)'
    'xPadding': int # Padding on left and right of tooltip | Default: 6
    'yPadding': int # Padding on top and bottom of tooltip | Default: 6
    'caretPadding': int # Extra distance to move the end of the tooltip
                        # arrow away from the tooltip point | Default: 2
    'caretSize': int # Size, in px, of the tooltip arrow | Default: 5
    'cornerRadius': int # Radius of tooltip corner curves | Default: 6
    'multiKeyBackground': str # Color to draw behind the colored boxes when
                              # multiple items are in the tooltip | Default: '#fff'
    'displayColors': bool # Show color boxes in the tooltip | Default: True
    'borderColor': str # Color of the border | Default: 'rgba(0, 0, 0, 0)'
    'borderWidth': int # Size of the border | Default: 0
    'rtl': bool # Rendering the legends from right to left | Default: True   

    # Title options
    'titleFontFamily': str # Title font | Default: 'Helvetica'
    'titleFontSize': int # Title font size | Default: 12
    'titleFontStyle': str # Title font style | Default: 'bold'
    'titleFontColor': str # Title font color | Default: '#fff'
    'titleAlign': str # Horizontal alignment of the title | Default: 'left'
    'titleSpacing': int # Spacing on top and bottom of title lines | Default: 2
    'titleMarginBottom': int # Margin on bottom of title section | Default: 6

    # Body options
    'bodyFontFamily': str # Body line font | Default: 'Helvetica'
    'bodyFontSize': int # Body font size | Default: 12
    'bodyFontStyle': str # Body font style | Default: 'normal'
    'bodyFontColor': str # Body font color | Default: '#fff'
    'bodyAlign': str # Horizontal alignment of the body | Default: 'left'
    'bodySpacing': int # Spacing on top and bottom of tooltip items | Default: 2

    # Footer options
    'footerFontFamily': str # Footer font | Default: 'Helvetica'
    'footerFontSize': int # Footer font size | Default: 12
    'footerFontStyle': str # Footer font style | Default: 'bold'
    'footerFontColor': str # Footer font color | Default: '#fff'
    'footerAlign': str # Horizontal alignment of the footer | Default: 'left'
    'footerSpacing': int # Spacing on top and bottom of footer lines | Default: 2
    'footerMarginTop': int # Margin on bottom of footer section | Default: 6
    
    # Callbacks options
    'custom': str # Callback function (see below) | Default: ''
    'itemSort': str # Callback function (see below) | Default: ''
    'filter': str # Callback function (see below) | Default: ''
    'callbacks': dict # See below | Default: {}

  }
}
```

#### Position argument

Possible modes are:
* `'average'`: place the tooltip at the average position of the items displayed in the tooltip.
* `'nearest'`: place the tooltip at the position of the element closest to the event position.

#### Alignment

The `titleAlign`, `bodyAlign` and `footerAlign` options define the horizontal position of the text lines with respect to the tooltip box. The following values are supported:

* `'left'` (default)
* `'right'`
* `'center'`

These options are only applied to text lines. Color boxes are always aligned to the left edge.

#### Callbacks argument

The tooltips can be customized with callback functions. Callback function are javascript function inputed into the chart to do some specific actions. To learn how to use callback function in ipychart, you can read [the callback functions section of the documentation]().

All tootltips functions are called with the same arguments: a `tooltip` item and the `data` object passed to the chart. Therefore, you can render tooltips using your data. All functions must return either a string or an array of strings. Arrays of strings are treated as multiple lines of text.

``` py
options = {
  'tooltips': {   
    'callbacks': {

      # All of the following arguments must be filled with 
      # a callback functions (i.e. JS functions). The description
      # of each arg corresponds to what the function must return.

      'beforeTitle': str # Text to render before the title | Default: ''
      'title': str # Text to render as the title of the tooltip | Default: ''
      'afterTitle': str # Text to render after the title | Default: ''
      'beforeBody': str # Text to render before the body section | Default: ''
      'beforeLabel': str # Text to render before an individual label. | Default: ''
                         # This will be called for each item in the tooltip
      'label': str # Text to render for an individual item in the tooltip | Default: ''
      'labelColor': str # The colors to render for the tooltip item | Default: ''
      'labelTextColor': str # The colors for the text of the label for the tooltip item | Default: ''
      'afterLabel': str # Text to render after an individual label | Default: ''
      'afterBody': str # Text to render after the body section | Default: ''
      'beforeFooter': str # Text to render before the footer section | Default: ''
      'footer': str # Text to render as the footer of the tooltip | Default: ''
      'afterFooter': str # Text to render after the footer section | Default: ''

    }
  }
}
```

### Example of a chart with custom tooltips

#### Simple example

Here is a example of what you can do to with the scales options (not exhaustive):

``` py

```

And the output:

<options-tooltips-simple/>

#### Example using callback functions

Here is a example of what you can do to with the scales options (not exhaustive):

``` py

```

<options-tooltips-callback/>

## Layout

### Layout options

With this argument, you can configure the scales of your chart. For example, you can add titles to each axis, choose the scale range, hide the scales ... To do that, you'll have to feed a dict to the scales argument of the options dict. This dict can have many properties, detailed below:

``` py
options = {
  'layout': {
    'padding': int or dict # The padding to add inside the chart | Default: 0
  }
}
```

You can spcify padding on each side of the chart if you use a dict:

``` py
options = {
  'layout': {
    'padding': {
      'left': 50,
      'right': 10,
      'top': 10,
      'bottom': 10
    }
  }
}
```


### Example of a chart with custom layout

Here is a example of what you can do to with the scales options (not exhaustive):

``` py

```

And the output:

<options-layout/>

## Hover

### Hover options

With this argument, you can configure the scales of your chart. For example, you can add titles to each axis, choose the scale range, hide the scales ... To do that, you'll have to feed a dict to the scales argument of the options dict. This dict can have many properties, detailed below:

``` py
options = {
  'hover': {   

    'mode': str # Sets which elements appear in the tooltip | Default: 'nearest'
    'intersect': bool # if True, the hover mode only applies when the mouse 
                      # position intersects an item on the chart | Default: True
    'axis': str # Can be set to 'x', 'y', or 'xy' to define which directions
                # are used in calculating distances | Default: 'x'
    'animationDuration': int # Duration in milliseconds it takes to animate hover 
                             # style changes. | Default: 400

  }
}
```

## Animations

### Animations options

With this argument, you can configure the scales of your chart. For example, you can add titles to each axis, choose the scale range, hide the scales ... To do that, you'll have to feed a dict to the scales argument of the options dict. This dict can have many properties, detailed below:

``` py
options = {
  'animations': {   

    'duration': number # Number of milliseconds for animations | Default: 1000
    'easing': str # Easing function to use | Default: 'easeOutQuart'
    'onProgress': str # Callback function (see below) | Default: ''
    'onComplete': str # Callback function (see below) | Default: ''

  }
}
```

#### Callbacks functions

Some of the arguments can be filled with callback functions. Callback function are javascript function inputed into the chart to do some specific actions. To learn how to use callback function in ipychart, you can read [the callback functions section of the documentation]().

#### Easing

Available options are:

``` py
options = {
  'animations': {
    'easing': {

      'linear'
      'easeInQuad'
      'easeOutQuad'
      'easeInOutQuad'
      'easeInCubic'
      'easeOutCubic'
      'easeInOutCubic'
      'easeInQuart'
      'easeOutQuart'
      'easeInOutQuart'
      'easeInQuint'
      'easeOutQuint'
      'easeInOutQuint'
      'easeInSine'
      'easeOutSine'
      'easeInOutSine'
      'easeInExpo'
      'easeOutExpo'
      'easeInOutExpo'
      'easeInCirc'
      'easeOutCirc'
      'easeInOutCirc'
      'easeInElastic'
      'easeOutElastic'
      'easeInOutElastic'
      'easeInBack'
      'easeOutBack'
      'easeInOutBack'
      'easeInBounce'
      'easeOutBounce'
      'easeInOutBounce'

    }
  }
}
```

### Example of a chart with custom animations

Here is a example of what you can do to with the scales options (not exhaustive):

``` py

```

And the output:

<options-animations/>
