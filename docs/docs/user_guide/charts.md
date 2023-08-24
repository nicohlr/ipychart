# Charts

In this section, we will go through each type of chart to see what possibilities it offers to display your data. We will also detail all the properties and the structure of the `'dataset'` sub dictionary that you'll build in the data argument ([see previous section](/ipychart/user_guide/usage)) of the *Chart* class.

::: tip
Logically, much of the content of this page is identical or very similar to that of the corresponding section of the documentation of Chart.js. You can consult it at any time by clicking [**here**](https://www.chartjs.org/docs/latest/charts/).
:::

## Line

A line chart is a way of plotting data points on a line. Often, it is used to show a trend in the data, or the comparison of two data sets.

:::details Click to show the code used to generate the Chart.
<br>

``` py
dataset = {
  'labels': ['Germany','Spain', 'UK', 'Italy', 'Norway', 'France', 'Poland', 
             'Portugal', 'Sweden', 'Ireland'],
  'datasets': [{'data': [14, 106, 16, 107, 45, 133, 19, 109, 60, 107],
                'lineTension': 0.3}]
}

mychart = Chart(dataset, 'line')
mychart
```
:::

<charts-line/>

You can choose this type of chart by setting the `kind` argument to `'line'`.

<p style="font-size:1.35rem;font-weight:600;line-height:1.25!important;margin-bottom:0;padding-top:4.6rem;margin-top:-3.1rem">Dataset properties</p>

For each dataset, the following properties are configurable:

``` py
data = {
  'datasets': [{
    'data': list or pd.Series # check data structure below 

    # dataset general options
    'fill': bool or str or int # How to fill the area under the line. | Default: True
    'label': bool or str # Label of the dataset | Default: ''
    'lineTension': int # Bezier curve tension of the line. | Default: 0.4
    'order': int # Drawing order of dataset | Default: 0
    'showLine': bool # Draw the line for this dataset | Default: True
    'spanGaps': bool or int # Draw lines between points with no data | Default: False
    'stepped': bool or string # See below | Default: False
    'clip': int or dict # See below | Default: borderWidth / 2
    'cubicInterpolationMode': str # See below | Default: 'default'

    # points and lines styling options
    'backgroundColor': str # Line fill color | Default: 'rgba(255, 99, 132, 0.2)'
    'borderCapStyle': str # Cap style of the line | Default: 'butt'
    'borderColor': str # Line color | Default: 'rgba(255, 99, 132, 1)'
    'borderDash': list # Length and spacing of dashes | Default: []
    'borderDashOffset': float # Offset for line dashes | Default: 0.0
    'borderJoinStyle': str # Line joint style | Default: 'miter'
    'borderWidth': int # Line width (in pixels) | Default: 3
    'pointBackgroundColor': str # Point fill color | Default: 'rgba(255, 99, 132, 0.2)'
    'pointBorderColor': str # Point border color | Default: 'rgba(255, 99, 132, 1)'
    'pointBorderWidth': int # Width of the point border in pixels | Default: 1
    'pointHitRadius': int # Size of the point (mouse events) | Default: 1
    'pointRadius': int # Radius of the point (0: point not rendered) | Default: 3
    'pointRotation': int # Rotation of the point in degrees | Default: 0 
    'pointStyle': str # Style of the point | Default: 'circle'

    # datalabels options (see datalabels documentation section)
    'datalabels': dict # Datalabels options | Default: None
  }]
}
```

You can also control the style of the points and the lines when hovering the chart by using the 'hover' prefix on some of the above options: `hoverBackgroundColor`, `hoverBorderCapStyle`, `hoverBorderColor`, `hoverBorderDash`, `hoverBorderDashOffset`, `hoverBorderJoinStyle`, `hoverBorderWidth`, `pointHoverBackgroundColor`, `pointHoverBorderColor`, `pointHoverBorderWidth`, `pointHoverRadius`

#### clip

How to clip relative to chartArea. Positive value allows overflow, negative value clips that many pixels inside chartArea. 0 = clip at chartArea. Clipping can also be configured per side: 
`'clip': {left: 5, top: False, right: -2, bottom: 0}`

#### cubicInterpolationMode

* `'default'`: algorithm that uses a custom weighted cubic interpolation, which produces pleasant curves for all types of datasets.
* `'monotone'`: this algorithm is more suited to `y = f(x)` datasets : it preserves monotonicity (or piecewise monotonicity) of the dataset being interpolated, and ensures local extremums (if any) stay at input data points.

#### Stepped

* `False`: No Step Interpolation (default)
* `True`: Step-before Interpolation (eq. `'before'`)
* `'before'`: Step-before Interpolation
* `'after'`: Step-after Interpolation
* `'middle'`: Step-middle Interpolation

<p style="font-size:1.35rem;font-weight:600;line-height:1.25!important;margin-bottom:0;padding-top:4.6rem;margin-top:-3.1rem">Data structures</p>

You can input your data in the data argument of the dataset using two different formats :

#### Number

``` py
data = {
  'datasets': [{'data': [20, 10]}]
}
```

#### Point

``` py
data = {
  'datasets': [{'data': [{'x': 10, 'y': 20}, {'x': 15, 'y': 10}]}]
}
```

::: tip
For all types of chart, you can also give a **Pandas series** to the data argument. For example by giving a column of a **Pandas dataframe** ⟶ 'data': df['column'] 
:::

## Bar 

A bar chart provides a way of showing data values represented as vertical or horizontal bars. It is sometimes used to show a trend in the data, and the comparison of multiple data sets side by side.

:::details Click to show the code used to generate the Chart.
<br>

``` py
dataset = {
  'labels': ['Germany','Spain', 'UK', 'Italy', 'Norway', 'France', 'Poland', 
             'Portugal', 'Sweden', 'Ireland'],
  'datasets': [{'data': [14, 106, 16, 107, 45, 133, 19, 109, 60, 107]}]}

mychart = Chart(dataset, 'bar')
mychart
```
:::

<charts-bar/>

You can choose this type of chart by setting the `kind` argument to `'bar'`.

<p style="font-size:1.35rem;font-weight:600;line-height:1.25!important;margin-bottom:0;padding-top:4.6rem;margin-top:-3.1rem">Dataset properties</p>

For each dataset, the following properties are configurable:

``` py
data = {
  'datasets': [{
    'data': list or pd.Series # check data structure below

    # dataset general options
    'label': bool or str # Label of the dataset | Default: ''
    'order': int # Drawing order of dataset | Default: 0

    # bars styling options
    'backgroundColor': str # Line fill color | Default: 'rgba(255, 99, 132, 0.2)'
    'borderColor': str # Line color | Default: 'rgba(255, 99, 132, 1)'
    'borderSkipped': str # See below | Default: 'bottom'
    'borderWidth': int # Line width (in pixels) | Default: 3
    'barThickness': str # See below | Default: None
    'maxBarThickness': str # Maximum bars thickness in pixels | Default: None
    'minBarLength': int # Minimum bars length in pixels | Default: None

    # datalabels options (see datalabels documentation section)
    'datalabels': dict # Datalabels options | Default: None
  }]
}
```

You can also control the style of the points and the lines when hovering the chart by using the 'hover' prefix on some of the above options: `hoverBackgroundColor`, `hoverBorderColor`, `hoverBorderWidth`

#### borderSkipped

This setting is used to avoid drawing the bar stroke at the base of the fill. In general, this does not need to be changed except when creating chart types that derive from a bar chart.
**Note:** for negative bars in vertical charts, `top` and `bottom` are flipped. Same goes for `left` and `right` in horizontal charts.

Options are:

* `'bottom'`
* `'left'`
* `'top'`
* `'right'`
* `false`

#### barThickness

If this value is a number, it is applied to the width of each bar, in pixels. When this is enforced, `barPercentage` and `categoryPercentage` are ignored.

If set to `'flex'`, the base sample widths are calculated automatically based on the previous and following samples so that they take the full available widths without overlapping. Then, bars are sized using `barPercentage` and `categoryPercentage`. There is no gap when the percentage options are 1. This mode generates bars with different widths when data is not evenly spaced.

If not set (default), the base sample widths are calculated using the smallest interval that prevents bars from overlapping, and bars are sized using `barPercentage` and `categoryPercentage`. This mode always generates bars equally sized.

<p style="font-size:1.35rem;font-weight:600;line-height:1.25!important;margin-bottom:0;padding-top:4.6rem;margin-top:-3.1rem">Data structures</p>

You can input your data in the data argument of the dataset using three different formats :

#### Number

``` py
data = {
  'datasets': [{'data': [20, 10]}]
}
```

#### Coordinates

You can specify the dataset as x/y coordinates when using the time scale.

``` py
data = {
  'datasets': [{'data': [{'x': '2016-12-25', 'y': 20}, {'x': '2016-12-26', 'y': 10}]}]
}
```

#### Array

You can also specify the dataset for a bar chart as arrays of two numbers. This will force rendering of bars with gaps between them (floating-bars). First and second numbers in array will correspond to the start and the end point of a bar respectively.

``` py
data = {
  'datasets': [{'data': [[5, 6], [-3, -6]]}]
}
```

<p style="font-size:1.35rem;font-weight:600;line-height:1.25!important;margin-bottom:0;padding-top:4.6rem;margin-top:-3.1rem">Horizontal Bar chart</p>

You can rotate your bar chart by setting the `indexAxis` key to `'y'` in the options of your chart:

:::details Click to show the code used to generate the Chart.
<br>

``` py
dataset = {
  'labels': ['Germany','Spain', 'UK', 'Italy', 'Norway', 'France', 'Poland', 
             'Portugal', 'Sweden', 'Ireland'],
  'datasets': [{'data': [14, 106, 16, 107, 45, 133, 19, 109, 60, 107]}]}

mychart = Chart(dataset, 'bar', options={'indexAxis': "y"})
mychart
```
:::

<charts-bar-horizontal/>

## Radar

A radar chart is a way of showing multiple data points and the variation between them. They are often useful for comparing the points of two or more different data sets.

:::details Click to show the code used to generate the Chart.
<br>

``` py
dataset = {
  'labels': ['Top','TopRight', 'BottomRight', 'BottomLeft', 'TopLeft'],
  'datasets': [{'data': [140, 106, 160, 107, 45],
                'label': 'Dataset1',
                'borderWidth': 3},
               {'data': [32, 160, 72, 140, 89],
                'label': 'Dataset2',
                'borderWidth': 3}]
}

mychart = Chart(dataset, 'radar')
mychart
```
:::

<charts-radar/>

You can choose this type of chart by setting the `kind` argument to `'radar'`.

<p style="font-size:1.35rem;font-weight:600;line-height:1.25!important;margin-bottom:0;padding-top:4.6rem;margin-top:-3.1rem">Dataset properties</p>

For each dataset, the following properties are configurable:

``` py
data = {
  'datasets': [{
    'data': list or pd.Series # check data structure below 

    # dataset general options
    'fill': bool or str or int # How to fill the area under the line. | Default: True
    'label': bool or str # Label of the dataset | Default: ''
    'lineTension': int # Bezier curve tension of the line. | Default: 0
    'order': int # Drawing order of dataset | Default: 0
    'spanGaps': bool or int # Draw lines between points with no data | Default: False

    # points and lines styling options
    'backgroundColor': str # Line fill color | Default: 'rgba(255, 99, 132, 0.2)'
    'borderCapStyle': str # Cap style of the line | Default: 'butt'
    'borderColor': str # Line color | Default: 'rgba(255, 99, 132, 1)'
    'borderDash': list # Length and spacing of dashes | Default: []
    'borderDashOffset': float # Offset for line dashes | Default: 0.0
    'borderJoinStyle': str # Line joint style | Default: 'miter'
    'borderWidth': int # Line width (in pixels) | Default: 3
    'pointBackgroundColor': str # Point fill color | Default: 'rgba(255, 99, 132, 0.2)'
    'pointBorderColor': str # Point border color | Default: 'rgba(255, 99, 132, 1)'
    'pointBorderWidth': int # Width of the point border in pixels | Default: 1
    'pointHitRadius': int # Size of the point (mouse events) | Default: 1
    'pointRadius': int # Radius of the point (0: point not rendered) | Default: 3
    'pointRotation': int # Rotation of the point in degrees | Default: 0 
    'pointStyle': str # Style of the point | Default: 'circle'

    # datalabels options (see datalabels documentation section)
    'datalabels': dict # Datalabels options | Default: None
  }]
}
```

You can also control the style of the points and the lines when hovering the chart by using the 'hover' prefix on some of the above options: `hoverBackgroundColor`, `hoverBorderCapStyle`, `hoverBorderColor`, `hoverBorderDash`, `hoverBorderDashOffset`, `hoverBorderJoinStyle`, `hoverBorderWidth`, `pointHoverBackgroundColor`, `pointHoverBorderColor`, `pointHoverBorderWidth`, `pointHoverRadius`

<p style="font-size:1.35rem;font-weight:600;line-height:1.25!important;margin-bottom:0;padding-top:4.6rem;margin-top:-3.1rem">Data structures</p>

You can input your data in the data argument of the dataset using the **number** format :

``` py
data = {
  'datasets': [{'data': [20, 10]}]
}
```

## Doughnut & Pie

Pie and doughnut charts are probably the most commonly used charts. They are divided into segments, the arc of each segment shows the proportional value of each piece of data.

They are excellent at showing the relational proportions between data.

:::details Click to show the code used to generate the Chart.
<br>

``` py
dataset = {
  'labels': ['Red','Blue', 'Yellow', 'Green', 'Purple'],
  'datasets': [{'data': [140, 106, 160, 107, 45],
                'backgroundColor': ['rgba(255, 99, 132, 1)', 
                                    'rgba(54, 162, 235, 1)',
                                    'rgba(255, 206, 86, 1)',
                                    'rgba(75, 192, 192, 1)',
                                    'rgba(153, 102, 255, 1)']
}]}

mychart = Chart(dataset, 'doughnut')
mychart
```
:::

<charts-doughnut/>

:::details Click to show the code used to generate the Chart.
<br>

``` py
dataset = {
  'labels': ['Red','Blue', 'Yellow', 'Green', 'Purple'],
  'datasets': [{'data': [140, 106, 160, 107, 45],
                'backgroundColor': ['rgba(255, 99, 132, 1)', 
                                    'rgba(54, 162, 235, 1)',
                                    'rgba(255, 206, 86, 1)',
                                    'rgba(75, 192, 192, 1)',
                                    'rgba(153, 102, 255, 1)']
}]}

mychart = Chart(dataset, 'pie')
mychart
```
:::

<charts-pie/>

You can choose this type of chart by setting the `kind` argument to either `'doughnut'` or `'pie'`.

<p style="font-size:1.35rem;font-weight:600;line-height:1.25!important;margin-bottom:0;padding-top:4.6rem;margin-top:-3.1rem">Dataset properties</p>

For each dataset, the following properties are configurable:

``` py
data = {
  'datasets': [{
    'data': list or pd.Series # check data structure below

    # dataset general options
    'weight': int # Relative thickness of the dataset. Setting a value for weight
                        # will cause the dataset to be drawn with a thickness relative
                        # to the sum of all the dataset weight values. | Default: 1

    # bars styling options
    'backgroundColor': str # Line fill color | Default: 'rgba(255, 99, 132, 0.2)'
    'borderAlign': str # Border aligment | Default: 'center'
    'borderColor': str # Line color | Default: 'rgba(255, 99, 132, 1)'
    'borderWidth': int # Line width (in pixels) | Default: 3

    # datalabels options (see datalabels documentation section)
    'datalabels': dict # Datalabels options | Default: None
  }]
}
```

You can also control the style of the points and the lines when hovering the chart by using the 'hover' prefix on some of the above options: `hoverBackgroundColor`, `hoverBorderColor`, `hoverBorderWidth`

#### Border Alignment

The following values are supported for `'borderAlign'`.
* `'center'` (default)
* `'inner'`

When `'center'` is set, the borders of arcs next to each other will overlap. When `'inner'` is set, it is guaranteed that all borders will not overlap.

<p style="font-size:1.35rem;font-weight:600;line-height:1.25!important;margin-bottom:0;padding-top:4.6rem;margin-top:-3.1rem">Data structures</p>

You can input your data in the data argument of the dataset using the **number** format :

``` py
data = {
  'datasets': [{'data': [20, 10]}]
}
```

## Polar Area

Polar area charts are similar to pie charts, but each segment has the same angle - the radius of the segment differs depending on the value. This type of chart is often useful when we want to show a comparison data similar to a pie chart, but also show a scale of values for context.

:::details Click to show the code used to generate the Chart.
<br>

``` py
dataset = {
  'labels': ['Red','Blue', 'Yellow', 'Green', 'Purple'],
  'datasets': [{'data': [140, 106, 160, 107, 45],
                'backgroundColor': ['rgba(255, 99, 132, 1)', 
                                    'rgba(54, 162, 235, 1)',
                                    'rgba(255, 206, 86, 1)',
                                    'rgba(75, 192, 192, 1)',
                                    'rgba(153, 102, 255, 1)'],
                'borderColor': ['#fff']*5,
                'borderWidth': 2.5
}]}

mychart = Chart(dataset, 'polarArea')
mychart
```
:::

<charts-polar/>

You can choose this type of chart by setting the `kind` argument to `'polarArea'`.

<p style="font-size:1.35rem;font-weight:600;line-height:1.25!important;margin-bottom:0;padding-top:4.6rem;margin-top:-3.1rem">Dataset properties</p>


For each dataset, the following properties are configurable:

``` py
data = {
  'datasets': [{
    'data': list or pd.Series # check data structure below

    # bars styling options
    'backgroundColor': str # Line fill color | Default: 'rgba(255, 99, 132, 0.2)'
    'borderAlign': str # Border aligment | Default: 'center'
    'borderColor': str # Line color | Default: 'rgba(255, 99, 132, 1)'
    'borderWidth': int # Line width (in pixels) | Default: 3

    # datalabels options (see datalabels documentation section)
    'datalabels': dict # Datalabels options | Default: None
  }]
}
```

You can also control the style of the points and the lines when hovering the chart by using the 'hover' prefix on some of the above options: `hoverBackgroundColor`, `hoverBorderColor`, `hoverBorderWidth`

#### Border Alignment

The following values are supported for `'borderAlign'`.
* `'center'` (default)
* `'inner'`

When `'center'` is set, the borders of arcs next to each other will overlap. When `'inner'` is set, it is guaranteed that all borders will not overlap.

<p style="font-size:1.35rem;font-weight:600;line-height:1.25!important;margin-bottom:0;padding-top:4.6rem;margin-top:-3.1rem">Data structures</p>

You can input your data in the data argument of the dataset using the **number** format :

``` py
data = {
  'datasets': [{'data': [20, 10]}]
}
```

## Scatter

Scatter charts are based on basic line charts with the x axis changed to a linear axis.

:::details Click to show the code used to generate the Chart.
<br>

``` py
dataset = {
  'datasets': [{'data': [
    {'x': random.randint(0, 100), 
     'y': random.randint(0, 100)} for _ in range(100)
  ]}]
}

mychart = Chart(dataset, 'scatter')
mychart
```
:::

<charts-scatter/>

You can choose this type of chart by setting the `kind` argument to `'scatter

<p style="font-size:1.35rem;font-weight:600;line-height:1.25!important;margin-bottom:0;padding-top:4.6rem;margin-top:-3.1rem">Dataset properties</p>

The scatter chart supports all of the same properties as the [line chart](/ipychart/user_guide/charts#line).

<p style="font-size:1.35rem;font-weight:600;line-height:1.25!important;margin-bottom:0;padding-top:4.6rem;margin-top:-3.1rem">Data structures</p>

You can input your data in the data argument of the dataset using the **point** format:

``` py
data = {
  'datasets': [{'data': [
    {'x': 10, 'y': 20} # This is the data for one point
    {'x': 15, 'y': 10} # This is the data for another point
  ]}]
}
```

## Bubble

A bubble chart is used to display three-dimension data. The location of the bubble is determined by the first two dimensions and the corresponding horizontal and vertical axes. The third dimension is represented by the radius of the individual bubbles.

:::details Click to show the code used to generate the Chart.
<br>

``` py
dataset = {
  'datasets': [{'data': [{'x': 20, 'y': 30, 'r': 5}, 
                         {'x': 10, 'y': 20, 'r': 50}, 
                         {'x': 15, 'y': 40, 'r': 20}, 
                         {'x': 5, 'y': 10, 'r': 10}],
                'borderWidth': 4}]
}

options = {
  'scales': {'x': {'min': 0, 'max': 25},
             'y': {'min': 0, 'max': 60}}
}

mychart = Chart(dataset, 'bubble', options=options)
mychart
```
:::

<charts-bubble/>

You can choose this type of chart by setting the `kind` argument to `'bubble'`

<p style="font-size:1.35rem;font-weight:600;line-height:1.25!important;margin-bottom:0;padding-top:4.6rem;margin-top:-3.1rem">Dataset properties</p>

For each dataset, the following properties are configurable:

``` py
data = {
  'datasets': [{
    'data': list or pd.Series # check data structure below

    # dataset general options
    'label': bool or str # Label of the dataset | Default: ''
    'order': int # Drawing order of dataset | Default: 0
    'radius': int # bubble radius (pixels) | Default: 3
    'rotation': int # bubble rotation (degrees) | Default: 0

    # bars styling options
    'backgroundColor': str # Line fill color | Default: 'rgba(255, 99, 132, 0.2)'
    'borderColor': str # Line color | Default: 'rgba(255, 99, 132, 1)'
    'borderSkipped': str # See below | Default: 'bottom'
    'borderWidth': int # Line width (in pixels) | Default: 3
    'pointStyle' : str # Style of the bubble | Default: 'circle'

    # datalabels options (see datalabels documentation section)
    'datalabels': dict # Datalabels options | Default: None
  }]
}
```

You can also control the style of the points and the lines when hovering the chart by using the 'hover' prefix on some of the above options: `hoverBackgroundColor`, `hoverBorderColor`, `hoverBorderWidth`, `hoverRadius`, `hitRadius`


<p style="font-size:1.35rem;font-weight:600;line-height:1.25!important;margin-bottom:0;padding-top:4.6rem;margin-top:-3.1rem">Data structures</p>

You can input your data in the data argument of the dataset using the following **point** format:

``` py
data = {
  'datasets': [{'data': [
    {'x': 10, 'y': 20, 'r': 5} # This is the data for one bubble
    {'x': 15, 'y': 10, 'r': 2} # This is the data for another bubble
  ]}]
}
```

## Other

### Stacked

Stacked bar charts can be used to show how one data series is made up of a number of smaller pieces.
Bar charts can be configured into stacked bar charts by changing the settings on the X and Y axes to enable stacking. To do this, you only must set the `'stacked'` options of the Axes to `True`.

Here is an example of a stacked bar chart :

:::details Click to show the code used to generate the Chart.
<br>

``` py
dataset = {
  'labels': ['Label 1', 'Label 2', 'Label 3'],
  'datasets': [
    {'data': [221, 783, 2478], 'label': "Africa",
    'fill': False}, 
    {'data': [1402, 3700, 5267], 'label': "Asia",
     'fill': False}, 
    {'data': [547, 675, 734], 'label': "Europe",
     'fill': False}, 
    {'data': [167, 508, 784], 'label': "Latin America",
     'fill': False}, 
    {'data': [172, 312, 433], 'label': "North America",
     'fill': False}
  ]
}

options = {
  'scales': {'x': {'stacked': True}, 'y': {'stacked': True}}
}

mychart = Chart(dataset, 'bar', options=options,
                colorscheme='tableau.Tableau20')
mychart
```
:::

<charts-stacked/>

### Area

Both [line](/ipychart/user_guide/charts#line) and [radar](/ipychart/user_guide/charts#radar) charts support a `'fill'` option on the dataset object which can be used to create an area between two datasets

``` py
data = {
  'datasets': [
    {'fill': 'origin' or True},  # fill to 'origin'
    {'fill': '+2'},  # fill to dataset 3
    {'fill': 1},  # fill to dataset 1
    {'fill': False},  # no fill
    {'fill': '-2'}  # fill to dataset 2
  ]
}
```

Here is an example of an area chart made using the `'fill'` option:

:::details Click to show the code used to generate the Chart.
<br>

``` py
dataset = {
  'labels': ['Germany','Spain', 'UK', 'Italy', 'Norway', 'France', 'Poland', 
             'Portugal', 'Sweden', 'Ireland'],
  'datasets': [{ 
    'data': [14, 106, 16, 107, 45, 133, 109, 109, 108, 107],
    'fill': True, 'lineTension': 0.3
}]}

mychart = Chart(dataset, 'line', colorscheme='brewer.PuOr3')
mychart
```
:::

<charts-area/>

### Mixed

With ipychart, it is possible to create mixed charts that are a combination of two or more different chart types. A common example is a bar chart that also includes a line dataset:

:::details Click to show the code used to generate the Chart.
<br>

``` py
dataset = {
  'labels': ['Dataset 1', 'Dataset 2', 'Dataset 3', 'Dataset 4',
             'Dataset 5', 'Dataset 6', 'Dataset 7', 'Dataset 8',
             'Dataset 9','Dataset 10'],
  'datasets': [{ 
    'data': [86, 114, 106, 106, 107, 111, 133, 221, 121, 142],
    'label': "Africa", 'fill': False, 'type': 'line', # Change the type
    'pointRadius': 5, 'pointHoverRadius': 10, 'lineTension': 0.3
    }, { 
    'data': [99, 130, 64, 100, 73, 22, 88, 198, 144, 64],
    'label': "Asia"
    }, { 
    'data': [168, 170, 178, 190, 203, 200, 164, 100, 72, 85],
    'label': "Europe", 'fill': False, 'type': 'line', # Change the type
    'pointRadius': 5, 'pointHoverRadius': 10, 'lineTension': 0.3
    }, {
    'data': [40, 20, 10, 16, 24, 38, 74, 167, 80, 150],
    'label': "Latin America"
    }, { 
    'data': [56, 95, 44, 112, 215, 35, 95, 74, 64, 78],
    'label': "North America"
    }
  ]
}

mychart = Chart(dataset, 'bar', colorscheme='tableau.ClassicLight10') # Base type
mychart
```
:::

<charts-mixed/>

