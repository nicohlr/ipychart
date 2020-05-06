# Create Charts

In this section, we will go though each type of chart to see what possibilities it offers to display your data. We will also detail all the properties and the structure of the **"dataset"** sub dict that you'll build in the data argument (see previous section)() of the Chart class.

::: tip
Logically, much of the content of this page is identical or very similar to that of the corresponding section of the documentation of Chart.js. You can consult it at any time by clicking [**here**](https://www.chartjs.org/docs/latest/charts/).
:::

## Line

A line chart is a way of plotting data points on a line. Often, it is used to show trend data, or the comparison of two data sets.

<charts-line/>

You can choose this type for your chart by setting the `kind` argument to **'line'**.

### Dataset properties

For each dataset, the following properties ar configurable:

``` py
data = {
    'datasets': [{
        'data': list or pd.Series # check data structure below 

        # dataset general options
        'fill': bool or str # How to fill the area under the line. | Default: True
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
    }]
}
```

You can also control the style of the points and the lines when hovering the chart by using the 'hover' prefix on some of the above options (types are the same that the option without prefix) : `hoverBackgroundColor`, `hoverBorderCapStyle`, `hoverBorderColor`, `hoverBorderDash`, `hoverBorderDashOffset`, `hoverBorderJoinStyle`, `hoverBorderWidth`, `pointHoverBackgroundColor`, `pointHoverBorderColor`, `pointHoverBorderWidth`, `pointHoverRadius`

#### clip

How to clip relative to chartArea. Positive value allows overflow, negative value clips that many pixels inside chartArea. 0 = clip at chartArea. Clipping can also be configured per side: 
`'clip': {left: 5, top: False, right: -2, bottom: 0}`

#### cubicInterpolationMode

* `'default'`: algorithm uses a custom weighted cubic interpolation, which produces pleasant curves for all types of datasets.
* `'monotone'`: algorithm is more suited to `y = f(x)` datasets : it preserves monotonicity (or piecewise monotonicity) of the dataset being interpolated, and ensures local extremums (if any) stay at input data points.

#### Stepped

* `False`: No Step Interpolation (default)
* `True`: Step-before Interpolation (eq. `'before'`)
* `'before'`: Step-before Interpolation
* `'after'`: Step-after Interpolation
* `'middle'`: Step-middle Interpolation

### Data structure

You can input your data in the data argument of the dataset using two formats :

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
You can also give a **pandas series** to the data argument. For exemple by giving a column of a **pandas dataframe** ⟶ 'data': df['column'] 
:::

## Bar 

A bar chart provides a way of showing data values represented as vertical bars. It is sometimes used to show trend data, and the comparison of multiple data sets side by side.

<charts-bar/>

You can choose this type for your chart by setting the `kind` argument to **'bar'** or **'horizontalBar'**.

### Dataset properties

For each dataset, the following properties ar configurable:

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
    }]
}
```

You can also control the style of the points and the lines when hovering the chart by using the 'hover' prefix on some of the above options (types are the same that the option without prefix) : `hoverBackgroundColor`, `hoverBorderColor`, `hoverBorderWidth`

#### borderSkipped

This setting is used to avoid drawing the bar stroke at the base of the fill. In general, this does not need to be changed except when creating chart types that derive from a bar chart.
**Note:** for negative bars in vertical chart, `top` and `bottom` are flipped. Same goes for `left` and `right` in horizontal chart.

Options are:

* `'bottom'`
* `'left'`
* `'top'`
* `'right'`
* `false`

#### barThickness

If this value is a number, it is applied to the width of each bar, in pixels. When this is enforced, `barPercentage` and `categoryPercentage` are ignored.

If set to `'flex'`, the base sample widths are calculated automatically based on the previous and following samples so that they take the full available widths without overlap. Then, bars are sized using `barPercentage` and `categoryPercentage`. There is no gap when the percentage options are 1. This mode generates bars with different widths when data are not evenly spaced.

If not set (default), the base sample widths are calculated using the smallest interval that prevents bar overlapping, and bars are sized using `barPercentage` and `categoryPercentage`. This mode always generates bars equally sized.

### Data structure


You can also specify the dataset as x/y coordinates when using the time scale.

data: [{x:'2016-12-25', y:20}, {x:'2016-12-26', y:10}]
You can also specify the dataset for a bar chart as arrays of two numbers. This will force rendering of bars with gaps between them (floating-bars). First and second numbers in array will correspond the start and the end point of a bar respectively.

data: [[5,6], [-3,-6]]

You can input your data in the data argument of the dataset using two formats :

#### Number

``` py
data = {
    'datasets': [{'data': [20, 10]}]
}
```

#### Coordinates

``` py
data = {
    'datasets': [{'data': [{'x': '2016-12-25', 'y': 20}, {'x': '2016-12-26', 'y': 10}]}]
}
```

#### Array

You can also specify the dataset for a bar chart as arrays of two numbers. This will force rendering of bars with gaps between them (floating-bars). First and second numbers in array will correspond the start and the end point of a bar respectively.

``` py
data = {
    'datasets': [{'data': [[5,6], [-3,-6]]}]
}
```

::: tip
You can also give a **pandas series** to the data argument. For exemple by giving a column of a **pandas dataframe** ⟶ 'data': df['column'] 
:::

### Horizontal Bar chart

You can transpose your bar chart by setting the **kind** argument of your chart to **'horizontalBar'**:

<charts-bar/>

## Radar

## Doughnut

## Pie

## Polar Area

## Bubble

## Scatter

## Other

### Stacked

### Area

### Mixed

