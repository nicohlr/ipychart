import pandas as pd
import numpy as np
from pandas.api.types import is_numeric_dtype
from sklearn.neighbors import KernelDensity
from sklearn.model_selection import GridSearchCV
from .chart import Chart


class ChartDataFrame():
    """
    A Jupyter - Chart.js bridge enabling interactive data visualization in the Jupyter notebook.

    Official documentation : https://nicohlr.gitlab.io/ipychart/
    Pandas Interface section : https://nicohlr.gitlab.io/ipychart/     # TODO: add link to pandas section

    This class is ipychart's Pandas API, allowing you to draw numerous interactive charts directly from a pandas dataframe.

    Args:
        df (pd.DataFrame): Your pandas dataframe that will be used to draw the chart.
    """

    def __init__(self, df: pd.DataFrame):

        self.df = df

    def _create_chart_options(self, kind: str, x: str, y: str, hue: str, options: dict):
        """
        This function will prepare all the options to create a chart from the input of the user.
        Axes labels are automatically set to match the names of the columns drawn on the chart.
        Legend is also modified to match the "hue" argument.

        Args:
            kind (str): The kind of the chart.
            x (str): Column of the dataframe used as datapoints for x Axis.
            y (str): Column of the dataframe used as datapoints for y Axis.
            hue (str, optional): Grouping variable that will produce points with different colors. Defaults to None.
            options (dict, optional): All options to configure the chart. This dictionary corresponds to the "options" argument of Chart.js. Defaults to None.

        Returns:
            options (dict): options dict ready to be inputed into a Chart class (i.e. match ipychart options format)
        """

        # Set axes labels corresponding to dataframe cols when option is not already set
        if kind != 'radar':
            if options:
                if 'scales' in options.keys():
                    if 'xAxes' in options['scales'].keys():
                        if 'scaleLabel' not in options['scales']['xAxes'][0]:
                            options['scales']['xAxes'][0].update({'scaleLabel': {'display': True, 'labelString': x}})
                        else:
                            if 'labelString' not in options['scales']['xAxes'][0]['scaleLabel']:
                                options['scales']['xAxes'][0]['scaleLabel']['labelString'] = x
                    else:
                        options['scales'].update({'xAxes': [{'scaleLabel': {'display': True, 'labelString': x}}]})
                    if 'yAxes' in options['scales'].keys():
                        if 'scaleLabel' not in options['scales']['yAxes'][0]:
                            options['scales']['yAxes'][0].update({'scaleLabel': {'display': True, 'labelString': y}})
                        else:
                            if 'labelString' not in options['scales']['yAxes'][0]['scaleLabel']:
                                options['scales']['yAxes'][0]['scaleLabel']['labelString'] = y
                    else:
                        options['scales'].update({'yAxes': [{'scaleLabel': {'display': True, 'labelString': y}}]})
                else:
                    options['scales'] = {'xAxes': [{'scaleLabel': {'display': True, 'labelString': x}}],
                                         'yAxes': [{'scaleLabel': {'display': True, 'labelString': y}}]}
            else:
                options = {'scales': {'xAxes': [{'scaleLabel': {'display': True, 'labelString': x}}],
                                      'yAxes': [{'scaleLabel': {'display': True, 'labelString': y}}]}}

        # Set legend prefix if "hue" if activated
        if hue:
            if options:
                skip_legend = False
                if 'legend' in options.keys():
                    if 'labels' in options['legend'].keys():
                        if 'generateLabels' in options['legend']['labels']:
                            skip_legend = True
                    else:
                        options['legend'].update({'labels': {}})
                else:
                    options['legend'] = {'labels': {}}
            else:
                options = {'legend': {}}

            if not skip_legend:
                # Callback function to add preficx before legend labels
                options['legend']['labels']['generateLabels'] = """function(chart) {
                        let labels = Chart.defaults.global.legend.labels.generateLabels(chart);
                        labels.map(label => {label['text'] = "%s" + " = " + label['text']; return label});
                        return labels;};""" % hue

        return options

    def _create_chart_data_count(self, x: str, dataset_options: [dict, list] = {}):
        """
        This function will prepare all the arguments to create a chart from the input of the user.
        Data are counted before being send to the Chart.

        Args:
            x (str): Column of the dataframe used as datapoints for x Axis.
            dataset_options ([dict, list], optional): These are options directly related to the dataset object (i.e. options concerning your data). Defaults to {}.

        Returns:
            data (dict): data dict ready to be inputed into a Chart class (i.e. match ipychart data format)
        """

        assert x in self.df.columns

        data = {'datasets': []}

        if is_numeric_dtype(self.df[x]):
            data['labels'] = self.df[x].value_counts(sort=False).sort_index(ascending=True).index.tolist()
            data['datasets'].append({'data': self.df[x].value_counts(sort=False).sort_index(ascending=True).round(4).tolist(), **dataset_options})
        else:
            data['labels'] = self.df[x].value_counts(ascending=False, sort=True).index.tolist()
            data['datasets'].append({'data': self.df[x].value_counts(ascending=False, sort=True).round(4).tolist(), **dataset_options})

        return data

    def _create_chart_data_agg(self, kind: str, x: str, y: str, hue: str = None, r: str = None, agg: str = None, dataset_options: [dict, list] = {}):
        """
        This function will prepare all the arguments to create a chart from the input of the user.
        Data are automatically aggregated using the method specified in the "agg" argument before being send to the Chart.

        Args:
            kind (str): The kind of the chart.
            x (str): Column of the dataframe used as datapoints for x Axis.
            y (str): Column of the dataframe used as datapoints for y Axis.
            hue (str, optional): Grouping variable that will produce points with different colors. Defaults to None.
            r (str, optional): Column used to define the radius of the bubbles (only for bubble chart). Defaults to None.
            agg (str, optional): The aggregator used to gather data (ex: 'median' or 'mean'). Defaults to None.
            dataset_options ([dict, list], optional): These are options directly related to the dataset object (i.e. options concerning your data). Defaults to {}.

        Returns:
            data (dict): data dict ready to be inputed into a Chart class (i.e. match ipychart data format)
        """

        assert x in self.df.columns
        assert y in self.df.columns
        assert is_numeric_dtype(self.df[y]), 'Please input a numeric columns as y'
        assert kind in ['line', 'bar', 'horizontalBar', 'radar', 'doughnut', 'polarArea', 'bubble', 'pie', 'scatter']

        if hue:
            assert hue in self.df.columns
            assert self.df[hue].nunique() <= 10, 'Too much values for the hue column'

        if isinstance(dataset_options, list):
            assert hue, 'For multiple dataset options, you must choose a column for hue that will create multiple datasets. Each dataset will corresponds to a unique value of the hue column'
            assert len(dataset_options) == self.df[hue].nunique(), 'The number of dataset options must be equal to the number of unique values in the hue column'

        data = {'datasets': []}

        if kind not in ['scatter', 'bubble']:

            data['labels'] = self.df[x].value_counts(ascending=True, sort=False).index.tolist()

            if hue:
                # Create one dataset for each unique value of the hue column
                for v in self.df[hue].unique():
                    data['datasets'].append({'data': self.df[self.df[hue] == v].groupby(x).agg(agg)[y].round(4).tolist(), 'label': v, **dataset_options})
            else:
                data['datasets'] = [{'data': self.df.groupby(x).agg(agg)[y].round(4).tolist(), **dataset_options}]

        elif kind == 'bubble':
            assert is_numeric_dtype(self.df[r]), 'Please input a numeric columns as r'
            assert is_numeric_dtype(self.df[x]), 'Please input a numeric columns as x'
            data['labels'] = self.df[x].tolist()

            if hue:
                # Create one dataset for each unique value of the hue column
                for v in self.df[hue].unique():
                    data['datasets'].append({'data': self.df[self.df[hue] == v].apply(lambda row: {'x': row[x], 'y': row[y], 'r': row[r]}, 1).tolist(), 'label': v, **dataset_options})
            else:
                data['datasets'] = [{'data': self.df.apply(lambda row: {'x': row[x], 'y': row[y], 'r': row[r]}, 1).tolist(), **dataset_options}]

        elif kind == 'scatter':

            assert is_numeric_dtype(self.df[x]), 'Please input a numeric columns as x'
            data['labels'] = self.df[x].tolist()

            if hue:
                # Create one dataset for each unique value of the hue column
                for v in self.df[hue].unique():
                    data['datasets'].append({'data': self.df[self.df[hue] == v].apply(lambda row: {'x': row[x], 'y': row[y]}, 1).tolist(), 'label': v, **dataset_options})
            else:
                data['datasets'] = [{'data': self.df.apply(lambda row: {'x': row[x], 'y': row[y]}, 1).tolist(), **dataset_options}]

        else:
            pass

        return data

    def count(self, x: str, orient: str = 'v', dataset_options: dict = {}, options: dict = None, colorscheme: str = None):
        """
        Show the counts of observations in each categorical bin using bars.

        Args:
            x (str): Column of the dataframe used as datapoints for x Axis.
            dataset_options (dict, optional): These are options directly related to the dataset object (i.e. options concerning your data). Defaults to {}.
            options (dict, optional): All options to configure the chart. This dictionary corresponds to the "options" argument of Chart.js. Defaults to None.
            colorscheme (str, optional): Colorscheme to use when drawing the chart. Defaults to None. Defaults to None.

        Returns:
            [ipychart.Chart]: A chart which display the data using ipychart
        """

        assert orient in ['v', 'h'], "orient argument must be either 'v' (vertical) or 'h' (horizontal)"

        data = self._create_chart_data_count(x=x, dataset_options=dataset_options)

        if orient == 'v':
            options = self._create_chart_options(kind='count', options=options, x=x, y='Count', hue=None)
        else:
            options = self._create_chart_options(kind='count', options=options, x='Count', y=x, hue=None)

        kind = 'bar' if orient == 'v' else 'horizontalBar'

        return Chart(data=data, kind=kind, options=options, colorscheme=colorscheme)

    def dist(self, x: str, bandwidth: [float, str] = 'auto', gridsize: int = 1000, dataset_options: dict = {}, options: dict = None, colorscheme: str = None, **kwargs):
        """
        Fit and plot a univariate kernel density estimate on a line chart. This is useful to have a representation of the distribution of the data.

        Args:
            x (str): Column of the dataframe used as datapoints for x Axis.
            bandwidth ([float, str], optional): Parameter which affect how “smooth” the resulting curve is. If set to 'auto', the optimal bandwidth is found using gridsearch. Defaults to 'auto'.
            gridsize (int, optional): Number of discrete points in the evaluation grid. Defaults to 1000.
            dataset_options (dict, optional): These are options directly related to the dataset object (i.e. options concerning your data). Defaults to {}.
            options (dict, optional): All options to configure the chart. This dictionary corresponds to the "options" argument of Chart.js. Defaults to None.
            colorscheme (str, optional): Colorscheme to use when drawing the chart. Defaults to None. Defaults to None.

        Returns:
            [ipychart.Chart]: A chart which display the data using ipychart
        """

        assert is_numeric_dtype(self.df[x]), 'Please input a numeric columns as x'
        if isinstance(bandwidth, str):
            assert bandwidth == 'auto', "The bandwidth must be either an int or 'auto'"

        # Remove outliers to find max and min values for the x axis
        iqr = self.df[x].quantile(0.95) - self.df[x].quantile(0.05)
        data_truncated = self.df[x][~((self.df[x] < (self.df[x].quantile(0.05) - 0.5 * iqr)) | (self.df[x] > (self.df[x].quantile(0.95) + 0.5 * iqr)))]
        max_val, min_val = (int(data_truncated.max()) + 1, int(data_truncated.min()))
        max_val, min_val = (max_val + 0.05 * (max_val + abs(min_val)), min_val - 0.05 * (max_val + abs(min_val)))

        # Create grid which will be used to compute kde
        _, step = np.linspace(min_val, max_val, num=gridsize, retstep=True)
        x_grid = np.round(np.arange(min_val, max_val, step), 5)

        # If bandwidth is 'auto', find the best bandwidh using gridsearch
        if bandwidth == 'auto':
            grid = GridSearchCV(KernelDensity(), {'bandwidth': np.linspace(0.1, 2, 30)}, cv=5)
            grid.fit(self.df[x].dropna()[:, None])
            bandwidth = grid.best_params_['bandwidth']

        kde_skl = KernelDensity(bandwidth=bandwidth, **kwargs)
        kde_skl.fit(self.df[x].dropna()[:, np.newaxis])
        pdf = np.exp(kde_skl.score_samples(x_grid[:, np.newaxis]))

        data = {'labels': x_grid.tolist(), 'datasets': [{'data': pdf.tolist(), 'pointRadius': 0}]}

        options = self._create_chart_options(kind='count', options=options, x=x, y=f'Density (bandwidth: {bandwidth.round(4)})', hue=None)

        # Add ticks formatting to options if not already set
        # This will not break because keys are created in the _create_chart_options method called previouly
        maxtickslimit = 10
        ticks_format_function = """function(value, index, values) {if (Math.abs(value) >= 1) {return Math.round(value);} else {return value.toFixed(3);}}"""

        if 'ticks' not in options['scales']['xAxes'][0]:
            options['scales']['xAxes'][0].update({'ticks': {'maxTicksLimit': maxtickslimit, 'callback': ticks_format_function}})
        else:
            if 'maxTicksLimit' not in options['scales']['xAxes'][0]['ticks']:
                options['scales']['xAxes'][0]['ticks']['maxTicksLimit'] = maxtickslimit
            if 'callback' not in options['scales']['xAxes'][0]['ticks']:
                options['scales']['xAxes'][0]['ticks']['callback'] = ticks_format_function

        return Chart(data, 'line', options=options)

    def line(self, x: str, y: str, hue: str = None, agg: str = 'mean', dataset_options: [dict, list] = {},
             options: dict = None, colorscheme: str = None):
        """
        A line chart is a way of plotting data points on a line. Often, it is used to show trend data, or the comparison of two data sets.

        Args:
            x (str): Column of the dataframe used as datapoints for x Axis.
            y (str): Column of the dataframe used as datapoints for y Axis.
            hue (str, optional): Grouping variable that will produce points with different colors. Defaults to None.
            agg (str, optional): The aggregator used to gather data (ex: 'median' or 'mean'). Defaults to None.
            dataset_options ([dict, list], optional): These are options directly related to the dataset object (i.e. options concerning your data). Defaults to {}.
            options (dict, optional): All options to configure the chart. This dictionary corresponds to the "options" argument of Chart.js. Defaults to None.
            colorscheme (str, optional): Colorscheme to use when drawing the chart. Defaults to None.

        Returns:
            [ipychart.Chart]: A chart which display the data using ipychart
        """

        data = self._create_chart_data_agg(kind='line', x=x, y=y, hue=hue, agg=agg, dataset_options=dataset_options)
        options = self._create_chart_options(kind='line', options=options, x=x, y=y, hue=hue)

        return Chart(data=data, kind='line', options=options, colorscheme=colorscheme)

    def bar(self, x: str, y: str, hue: str = None, agg: str = 'mean', dataset_options: [dict, list] = {},
            options: dict = None, colorscheme: str = None, horizontal: bool = False):
        """
        A bar chart provides a way of showing data values represented as vertical bars. It is sometimes used to show trend data, and the comparison of multiple data sets side by side.

        Args:
            x (str): Column of the dataframe used as datapoints for x Axis.
            y (str): Column of the dataframe used as datapoints for y Axis.
            hue (str, optional): Grouping variable that will produce points with different colors. Defaults to None.
            agg (str, optional): The aggregator used to gather data (ex: 'median' or 'mean'). Defaults to None.
            dataset_options ([dict, list], optional): These are options directly related to the dataset object (i.e. options concerning your data). Defaults to {}.
            options (dict, optional): All options to configure the chart. This dictionary corresponds to the "options" argument of Chart.js. Defaults to None.
            colorscheme (str, optional): Colorscheme to use when drawing the chart. Defaults to None.
            horizontal (bool): draw the bar chart horizontally. Defaults to False.

        Returns:
            [ipychart.Chart]: A chart which display the data using ipychart
        """

        data = self._create_chart_data_agg(kind='bar', x=x, y=y, hue=hue, agg=agg, dataset_options=dataset_options)
        options = self._create_chart_options(kind='bar', options=options, x=x, y=y, hue=hue)

        if horizontal:
            return Chart(data=data, kind='horizontalBar', options=options, colorscheme=colorscheme)
        else:
            return Chart(data=data, kind='bar', options=options, colorscheme=colorscheme)

    def radar(self, x: str, y: str, hue: str = None, agg: str = 'mean', dataset_options: [dict, list] = {},
              options: dict = None, colorscheme: str = None):
        """
        A radar chart is a way of showing multiple data points and the variation between them. They are often useful for comparing the points of two or more different data sets.

        Args:
            x (str): Column of the dataframe used as datapoints for x Axis.
            y (str): Column of the dataframe used as datapoints for y Axis.
            hue (str, optional): Grouping variable that will produce points with different colors. Defaults to None.
            agg (str, optional): The aggregator used to gather data (ex: 'median' or 'mean'). Defaults to None.
            dataset_options ([dict, list], optional): These are options directly related to the dataset object (i.e. options concerning your data). Defaults to {}.
            options (dict, optional): All options to configure the chart. This dictionary corresponds to the "options" argument of Chart.js. Defaults to None.
            colorscheme (str, optional): Colorscheme to use when drawing the chart. Defaults to None.

        Returns:
            [ipychart.Chart]: A chart which display the data using ipychart
        """

        data = self._create_chart_data_agg(kind='radar', x=x, y=y, hue=hue, agg=agg, dataset_options=dataset_options)
        options = self._create_chart_options(kind='radar', options=options, x=x, y=y, hue=hue)

        return Chart(data=data, kind='radar', options=options, colorscheme=colorscheme)

    def doughnut(self, x: str, y: str = None, agg: str = 'mean', dataset_options: dict = {},
                 options: dict = None, colorscheme: str = None):
        """
        Pie and doughnut charts are excellent at showing the relational proportions between data.

        Args:
            x (str): Column of the dataframe used as datapoints for x Axis.
            y (str, optional): Column of the dataframe used as datapoints for y Axis. Defaults to None.
            agg (str, optional): The aggregator used to gather data (ex: 'median' or 'mean'). Defaults to None.
            dataset_options (dict, optional): These are options directly related to the dataset object (i.e. options concerning your data). Defaults to {}.
            options (dict, optional): All options to configure the chart. This dictionary corresponds to the "options" argument of Chart.js. Defaults to None.
            colorscheme (str, optional): Colorscheme to use when drawing the chart. Defaults to None.

        Returns:
            [ipychart.Chart]: A chart which display the data using ipychart
        """
        if y:
            data = self._create_chart_data_agg(kind='doughnut', x=x, y=y, agg=agg, dataset_options=dataset_options)
        else:
            data = self._create_chart_data_count(x=x, dataset_options=dataset_options)

        return Chart(data=data, kind='doughnut', options=options, colorscheme=colorscheme)

    def pie(self, x: str, y: str = None, agg: str = 'mean', dataset_options: dict = {},
            options: dict = None, colorscheme: str = None):
        """
        Pie and doughnut charts are excellent at showing the relational proportions between data.

        Args:
            x (str): Column of the dataframe used as datapoints for x Axis.
            y (str, optional): Column of the dataframe used as datapoints for y Axis. Defaults to None.
            agg (str, optional): The aggregator used to gather data (ex: 'median' or 'mean'). Defaults to None.
            dataset_options (dict, optional): These are options directly related to the dataset object (i.e. options concerning your data). Defaults to {}.
            options (dict, optional): All options to configure the chart. This dictionary corresponds to the "options" argument of Chart.js. Defaults to None.
            colorscheme (str, optional): Colorscheme to use when drawing the chart. Defaults to None.

        Returns:
            [ipychart.Chart]: A chart which display the data using ipychart
        """

        if y:
            data = self._create_chart_data_agg(kind='pie', x=x, y=y, agg=agg, dataset_options=dataset_options)
        else:
            data = self._create_chart_data_count(x=x, dataset_options=dataset_options)

        return Chart(data=data, kind='pie', options=options, colorscheme=colorscheme)

    def polararea(self, x: str, y: str = None, agg: str = 'mean', dataset_options: dict = {},
                  options: dict = None, colorscheme: str = None):
        """
        Polar area charts are similar to pie charts, but each segment has the same angle - the radius of the segment differs depending on the value.

        Args:
            x (str): Column of the dataframe used as datapoints for x Axis.
            y (str, optional): Column of the dataframe used as datapoints for y Axis. Defaults to None.
            agg (str, optional): The aggregator used to gather data (ex: 'median' or 'mean'). Defaults to None.
            dataset_options (dict, optional): These are options directly related to the dataset object (i.e. options concerning your data). Defaults to {}.
            options (dict, optional): All options to configure the chart. This dictionary corresponds to the "options" argument of Chart.js. Defaults to None.
            colorscheme (str, optional): Colorscheme to use when drawing the chart. Defaults to None.

        Returns:
            [ipychart.Chart]: A chart which display the data using ipychart
        """
        if y:
            data = self._create_chart_data_agg(kind='polarArea', x=x, y=y, agg=agg, dataset_options=dataset_options)
        else:
            data = self._create_chart_data_count(x=x, dataset_options=dataset_options)

        return Chart(data=data, kind='polarArea', options=options, colorscheme=colorscheme)

    def scatter(self, x: str, y: str, hue: str = None, agg: str = 'mean', dataset_options: [dict, list] = {},
                options: dict = None, colorscheme: str = None):
        """
        Scatter charts are based on basic line charts with the x axis changed to a linear axis.

        Args:
            x (str): Column of the dataframe used as datapoints for x Axis.
            y (str): Column of the dataframe used as datapoints for y Axis.
            hue (str, optional): Grouping variable that will produce points with different colors. Defaults to None.
            agg (str, optional): The aggregator used to gather data (ex: 'median' or 'mean'). Defaults to None.
            dataset_options ([dict, list], optional): These are options directly related to the dataset object (i.e. options concerning your data). Defaults to {}.
            options (dict, optional): All options to configure the chart. This dictionary corresponds to the "options" argument of Chart.js. Defaults to None.
            colorscheme (str, optional): Colorscheme to use when drawing the chart. Defaults to None.

        Returns:
            [ipychart.Chart]: A chart which display the data using ipychart
        """

        data = self._create_chart_data_agg(kind='scatter', x=x, y=y, hue=hue, agg=agg, dataset_options=dataset_options)
        options = self._create_chart_options(kind='scatter', options=options, x=x, y=y, hue=hue)

        return Chart(data=data, kind='scatter', options=options, colorscheme=colorscheme)

    def bubble(self, x: str, y: str, r: str, hue: str = None, agg: str = 'mean', dataset_options: [dict, list] = {},
               options: dict = None, colorscheme: str = None):
        """
        A bubble chart is used to display three dimensions of data at the same time.
        The location of the bubble is determined by the first two dimensions and the corresponding horizontal and vertical axes.
        The third dimension is represented by the radius of the individual bubbles.

        Args:
            x (str): Column of the dataframe used as datapoints for x Axis.
            y (str): Column of the dataframe used as datapoints for y Axis.
            r (str, optional): Column of the dataframe used as radius for bubbles.
            hue (str, optional): Grouping variable that will produce points with different colors. Defaults to None.
            agg (str, optional): The aggregator used to gather data (ex: 'median' or 'mean'). Defaults to None.
            dataset_options ([dict, list], optional): These are options directly related to the dataset object (i.e. options concerning your data). Defaults to {}.
            options (dict, optional): All options to configure the chart. This dictionary corresponds to the "options" argument of Chart.js. Defaults to None.
            colorscheme (str, optional): Colorscheme to use when drawing the chart. Defaults to None.

        Returns:
            [ipychart.Chart]: A chart which display the data using ipychart
        """

        data = self._create_chart_data_agg(kind='bubble', x=x, y=y, r=r, hue=hue, agg=agg, dataset_options=dataset_options)
        options = self._create_chart_options(kind='bubble', options=options, x=x, y=y, hue=hue)

        return Chart(data=data, kind='bubble', options=options, colorscheme=colorscheme)
