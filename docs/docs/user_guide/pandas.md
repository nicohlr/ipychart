# Pandas Interface

## Why ?

Today, Python is one of the most popular languages for data analysis and data science. One of the reasons for Python's success in these areas is Pandas, the leading package for data manipulation with Python. This package has quickly become a must and is used by a very large number of people around the world.

It is therefore essential to be able to create visualizations directly from a pandas dataframe. This can be done for example with Seaborn, a famous Python package for data visualization. Thanks to the interface presented in this section, it is also possible to do the same thing with ipychart.

## Usage

This interface allows you to quickly create charts from a pandas dataframe, without having to use the low-level syntax of Chart.js. We will use, in the rest of this section, the famous titanic dataset. Let's start by loading this dataset with pandas:

```py
import pandas as pd

titanic = pd.read_csv('titanic.csv')
titanic.head()
```
<pandas-head/>

Concretely, to use ipychart's pandas interface, we will have to use the *ChartDataFrame* class (instead of using the *Chart* class that we saw previously). So let's start by creating an instance of this class, giving our pandas dataframe as an argument:

```py
from ipychart import ChartDataFrame

titanic_chart = ChartDataFrame(titanic)
```

We are now ready to plot all kinds of visualizations on the dataset from this instance. To do this, we need to call the methods of the *ChartDataFrame* class. Each method corresponds to a type of chart. To draw a bar chart, for example, you need to execute:

```py
titanic_chart.bar(x='Embarked', y='Age', hue='Survived')
```

<pandas-example/>

## Charts

You can find here all the methods of the *ChartDataFrame* class, each one corresponding to a type of chart. Each method returns a *Chart* object, i.e. an instance of the *Chart* class of ipychart package.

All methods have two parameters in common: `dataset_options` and `options`. The `dataset_options` parameter allows you to set the options for each dataset, as with the *Chart* class. If you don't use the `hue` parameter, the chart will have only one dataset and you will have to pass a dictionary. Otherwise, the Chart will have N datasets (each one corresponding to a distinct value of the column selected in the `hue` parameter) and you must pass a list of dict. In the same way, you can use the `options` parameter to customize the Chart, like when you use the *Chart* class.

### Count

:::tip
This chart can only be created from a single column of a pandas dataframe.
:::

The count chart shows the counts of observations in each categorical bin using bars. To draw it, you must call the *count* method:

```py
ChartDataFrame.count(x: str, orient: str = 'v', dataset_options: dict = {}, 
                     options: dict = None, colorscheme: str = None)
```

- **x : str**<br>
Column of the dataframe used as datapoints for x Axis.
- **dataset_options (optional): dict**<br>
These are options directly related to the dataset object (i.e. options concerning your data).
- **options (optional): dict**<br>
All options to configure the chart. This dictionary corresponds to the "options" argument of Chart.js.
- **colorscheme (optional): str**<br>
Colorscheme to use when drawing the chart. List of available colorscheme: link.

**Example:**

```py
titanic_chart.count(x='Embarked')
```
<pandas-count/>

### Dist

:::tip
This chart can only be created from a single column of a pandas dataframe.
:::

Fit and plot a univariate kernel density estimate on a line chart. This chart is useful to have a representation of the distribution of the data. To draw it, you must call the *dist* method:

```py
ChartDataFrame.dist(x: str, bandwidth: [float, str] = 'auto', gridsize: int = 1000, 
                    dataset_options: dict = {}, options: dict = None, 
                    colorscheme: str = None, **kwargs):
```

- **x : str**<br>
Column of the dataframe used as datapoints for x Axis.
- **bandwidth (optionnal): float, str**<br>
Parameter which affect how “smooth” the resulting curve is. If set to 'auto', the optimal bandwidth is found using gridsearch.
- **gridsize (optionnal): int**<br>
Number of discrete points in the evaluation grid.
- **dataset_options (optional): dict**<br>
These are options directly related to the dataset object (i.e. options concerning your data).
- **options (optional): dict**<br>
All options to configure the chart. This dictionary corresponds to the "options" argument of Chart.js.
- **colorscheme (optional): str**<br>
Colorscheme to use when drawing the chart. List of available colorscheme: link.
- **kwargs (optional): dict**<br>
Other keyword arguments are passed to the *KernelDensity* class of scikit-learn. 

**Example:**

```py
titanic_chart.dist(x='Age')
```
<pandas-dist/>

### Line

A line chart is a way of plotting data points on a line. Often, it is used to show trend data, or the comparison of two data sets. To draw it, you must call the *line* method:

```py
ChartDataFrame.line(x: str, y: str, hue: str = None, agg: str = 'mean', 
                    dataset_options: [dict, list] = {},
                    options: dict = None, colorscheme: str = None):
```

- **x : str**<br>
Column of the dataframe used as datapoints for x Axis.
- **y : str**<br>
Column of the dataframe used as datapoints for y Axis.
- **hue (optionnal): str**<br>
Grouping variable that will produce points with different colors.
- **agg (optionnal): str**<br>
The aggregator used to gather data (ex: 'median' or 'mean').
- **dataset_options (optional): dict**<br>
These are options directly related to the dataset object (i.e. options concerning your data).
- **options (optional): dict**<br>
All options to configure the chart. This dictionary corresponds to the "options" argument of Chart.js.
- **colorscheme (optional): str**<br>
Colorscheme to use when drawing the chart. List of available colorscheme: link.

**Example:**

```py
datalabels_arguments = {'display': True, 'borderWidth': 1, 'anchor': 'end', 
                        'align': 'end', 'borderRadius': 5, 'color': '#fff'}

titanic_chart.line(x='Pclass', y='Age', hue='Sex', 
                   dataset_options={'fill': False, 'datalabels': datalabels_arguments}, 
                   colorscheme='office.Parallax6')
```

<pandas-line/>

### Bar

A bar chart provides a way of showing data values represented as vertical bars. It is sometimes used to show trend data, and the comparison of multiple data sets side by side. To draw it, you must call the *bar* method:

```py
ChartDataFrame.bar(x: str, y: str, hue: str = None, agg: str = 'mean', 
                   dataset_options: [dict, list] = {},
                   options: dict = None, colorscheme: str = None):
```

- **x : str**<br>
Column of the dataframe used as datapoints for x Axis.
- **y : str**<br>
Column of the dataframe used as datapoints for y Axis.
- **hue (optionnal): str**<br>
Grouping variable that will produce points with different colors.
- **agg (optionnal): str**<br>
The aggregator used to gather data (ex: 'median' or 'mean').
- **dataset_options (optional): dict**<br>
These are options directly related to the dataset object (i.e. options concerning your data).
- **options (optional): dict**<br>
All options to configure the chart. This dictionary corresponds to the "options" argument of Chart.js.
- **colorscheme (optional): str**<br>
Colorscheme to use when drawing the chart. List of available colorscheme: link.
- **horizontal (optional): bool**<br>
Draw the bar chart horizontally.

**Example:**

```py
titanic_chart.bar(x='Pclass', y='Fare', hue='Sex', colorscheme='office.Parallax6')
```

<pandas-bar/>

### Radar

A radar chart is a way of showing multiple data points and the variation between them. They are often useful for comparing the points of two or more different data sets. To draw it, you must call the *radar* method:

```py
ChartDataFrame.radar(x: str, y: str, hue: str = None, agg: str = 'mean', 
                     dataset_options: [dict, list] = {},
                     options: dict = None, colorscheme: str = None):
```

- **x : str**<br>
Column of the dataframe used as datapoints for x Axis.
- **y : str**<br>
Column of the dataframe used as datapoints for y Axis.
- **hue (optionnal): str**<br>
Grouping variable that will produce points with different colors.
- **agg (optionnal): str**<br>
The aggregator used to gather data (ex: 'median' or 'mean').
- **dataset_options (optional): dict**<br>
These are options directly related to the dataset object (i.e. options concerning your data).
- **options (optional): dict**<br>
All options to configure the chart. This dictionary corresponds to the "options" argument of Chart.js.
- **colorscheme (optional): str**<br>
Colorscheme to use when drawing the chart. List of available colorscheme: link.

**Example:**

```py
data_chart.radar(x='Title', y='Fare', colorscheme='office.Yellow6')
```

<pandas-radar/>

### Pie, Doughnut & Polar Area

Pie and doughnut charts are excellent at showing the relational proportions between data. Polar Area charts are similar to pie and doughnut charts, but each segment has the same angle - the radius of the segment differs depending on the value. 
To draw one of these charts, you must call the *pie* method, the *doughnut* method or the *polararea* method:

```py
ChartDataFrame.doughnut(x: str, y: str, agg: str = 'mean', 
                        dataset_options: [dict, list] = {},
                        options: dict = None, colorscheme: str = None):
                        
ChartDataFrame.pie(x: str, y: str, agg: str = 'mean', 
                   dataset_options: [dict, list] = {},
                   options: dict = None, colorscheme: str = None):
                        
ChartDataFrame.polararea(x: str, y: str, agg: str = 'mean', 
                         dataset_options: [dict, list] = {},
                         options: dict = None, colorscheme: str = None):
```

- **x : str**<br>
Column of the dataframe used as datapoints for x Axis.
- **y : str**<br>
Column of the dataframe used as datapoints for y Axis.
- **agg (optionnal): str**<br>
The aggregator used to gather data (ex: 'median' or 'mean').
- **dataset_options (optional): dict**<br>
These are options directly related to the dataset object (i.e. options concerning your data).
- **options (optional): dict**<br>
All options to configure the chart. This dictionary corresponds to the "options" argument of Chart.js.
- **colorscheme (optional): str**<br>
Colorscheme to use when drawing the chart. List of available colorscheme: link.

**Example:**

```py
titanic_chart.polararea(x='Title', y='Fare', colorscheme='brewer.SetThree5')
```

<pandas-polararea/>

### Scatter

Scatter charts are based on basic line charts with the x axis changed to a linear axis. To draw it, you must call the *scatter* method:

```py
ChartDataFrame.scatter(x: str, y: str, hue: str = None, agg: str = 'mean', 
                       dataset_options: [dict, list] = {},
                       options: dict = None, colorscheme: str = None):
```

- **x : str**<br>
Column of the dataframe used as datapoints for x Axis.
- **y : str**<br>
Column of the dataframe used as datapoints for y Axis.
- **hue (optionnal): str**<br>
Grouping variable that will produce points with different colors.
- **agg (optionnal): str**<br>
The aggregator used to gather data (ex: 'median' or 'mean').
- **dataset_options (optional): dict**<br>
These are options directly related to the dataset object (i.e. options concerning your data).
- **options (optional): dict**<br>
All options to configure the chart. This dictionary corresponds to the "options" argument of Chart.js.
- **colorscheme (optional): str**<br>
Colorscheme to use when drawing the chart. List of available colorscheme: link.

**Example:**

```py
titanic_chart.scatter(x='Age', y='Fare', hue='Survived', 
                      colorscheme='tableau.ColorBlind10')
```

<pandas-scatter/>

### Bubble

A bubble chart is used to display three dimensions of data at the same time. The location of the bubble is determined by the first two dimensions and the corresponding horizontal and vertical axes. The third dimension is represented by the radius of the individual bubbles. To draw it, you must call the *bubble* method:

```py
ChartDataFrame.bubble(x: str, y: str, r: str = None, hue: str = None, 
                      agg: str = 'mean', dataset_options: [dict, list] = {},
                      options: dict = None, colorscheme: str = None):
```

- **x : str**<br>
Column of the dataframe used as datapoints for x Axis.
- **y : str**<br>
Column of the dataframe used as datapoints for y Axis.
- **r : str**<br>
Column of the dataframe used as radius for bubbles.
- **hue (optionnal): str**<br>
Grouping variable that will produce points with different colors.
- **agg (optionnal): str**<br>
The aggregator used to gather data (ex: 'median' or 'mean').
- **dataset_options (optional): dict**<br>
These are options directly related to the dataset object (i.e. options concerning your data).
- **options (optional): dict**<br>
All options to configure the chart. This dictionary corresponds to the "options" argument of Chart.js.
- **colorscheme (optional): str**<br>
Colorscheme to use when drawing the chart. List of available colorscheme: link.

**Example:**

```py
titanic_chart.bubble(x='Age', y='Fare', r='Pclass', hue='Survived', 
                     colorscheme='office.Headlines6')
```

<pandas-bubble/>
