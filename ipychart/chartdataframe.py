import pandas as pd
from pandas.api.types import is_numeric_dtype
from .chart import Chart


class ChartDataFrame():
    """
    A Jupyter - Chart.js bridge enabling interactive data visualization in the Jupyter notebook.

    Official documentation : https://nicohlr.gitlab.io/ipychart/
    Pandas Integration section : https://nicohlr.gitlab.io/ipychart/     # TODO: add link to pandas section

    This class is ipychart's Pandas API, allowing you to draw numerous interactive charts directly from a pandas dataframe.

    Args:
        df (pd.DataFrame): Your pandas data that will be used to draw the chart.
    """

    def __init__(self, df: pd.DataFrame):

        self.df = df

    def _create_chart_options(self, kind: str, x: str, y: str, hue: str,  options: dict):
        """
        This function will prepare all the options to create a chart from the input of the user.
        Axes labels are automatically set to match the names of the columns drawn on the chart.
        Legend is also modified to match the "hue" argument.

        Args:
            kind (str): The kind of the chart.
            x (str): Column of the data dataframe used as datapoints for x Axis.
            y (str): Column of the data dataframe used as datapoints for y Axis.
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

    def _create_chart_data(self, kind: str, x: str, y: str, hue: str = None, r: str = None, agg: str = None, dataset_options: [dict, list] = None):
        """
        This function will prepare all the arguments to create a chart from the input of the user.
        Data are automatically aggregated using the method specified in the "agg" argument before being send to the Chart.

        Args:
            kind (str): The kind of the chart.
            x (str): Column of the data dataframe used as datapoints for x Axis.
            y (str): Column of the data dataframe used as datapoints for y Axis.
            hue (str, optional): Grouping variable that will produce points with different colors. Defaults to None.
            r (str, optional): Column used to define the radius of the bubbles (only for bubble chart). Defaults to None.
            agg (str, optional): The aggregator used to gather data (ex: 'median' or 'mean'). Defaults to None.
            dataset_options (dict, optional): These are options directly related to the dataset object (i.e. options concerning your data). Defaults to None.
            options (dict, optional): All options to configure the chart. This dictionary corresponds to the "options" argument of Chart.js. Defaults to None.
            colorscheme (str, optional): colorscheme to use when drawing the chart. Defaults to None.

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

            if hue:
                data['labels'] = self.df[x].value_counts(ascending=True, sort=False).index.tolist()
                for v in self.df[hue].unique():
                    data['datasets'].append({'data': self.df[self.df[hue] == v].groupby(x).agg(agg)[y].round(4).tolist(), 'label': v, **dataset_options})
            else:
                data['labels'] = self.df[x].value_counts(ascending=True, sort=False).index.tolist()
                data['datasets'] = [{'data': self.df.groupby(x).agg(agg)[y].round(4).tolist(), **dataset_options}]

        elif kind == 'bubble':
            assert is_numeric_dtype(self.df[r]), 'Please input a numeric columns as r'
            pass

        else:
            pass

        return data

    def dist(self):
        raise NotImplementedError

    def count(self):
        raise NotImplementedError

    def line(self, x: str, y: str, hue: str = None, agg: str = 'mean', dataset_options: dict = {},
             options: dict = None, colorscheme: str = None):
        """
        A line chart is a way of plotting data points on a line. Often, it is used to show trend data, or the comparison of two data sets.

        Args:
            x (str): Columns of the data dataframe used as datapoints for x Axis.
            y (str): Columns of the data dataframe used as datapoints for y Axis.
            hue (str, optional): Grouping variable that will produce points with different colors. Defaults to None.
            agg (str, optional): The aggregator used to gather data (ex: 'median' or 'mean'). Defaults to None.
            dataset_options (dict, optional): These are options directly related to the dataset object (i.e. options concerning your data). Defaults to None.
            options (dict, optional): All options to configure the chart. This dictionary corresponds to the "options" argument of Chart.js. Defaults to None.
            colorscheme (str, optional): colorscheme to use when drawing the chart. Defaults to None.

        Returns:
            [ipychart.Chart]: A chart which display the data using ipychart
        """

        data = self._create_chart_data(kind='line', x=x, y=y, hue=hue, agg=agg, dataset_options=dataset_options)
        options = self._create_chart_options(kind='line', options=options, x=x, y=y, hue=hue)
        return Chart(data=data, kind='line', options=options, colorscheme=colorscheme)

    def bar(self, x: str, y: str, hue: str = None, agg: str = 'mean', dataset_options: dict = {},
            options: dict = None, colorscheme: str = None, horizontal: bool = False):
        """
        A bar chart provides a way of showing data values represented as vertical bars. It is sometimes used to show trend data, and the comparison of multiple data sets side by side.

        Args:
            x (str): Columns of the data dataframe used as datapoints for x Axis.
            y (str): Columns of the data dataframe used as datapoints for y Axis.
            hue (str, optional): Grouping variable that will produce points with different colors. Defaults to None.
            agg (str, optional): The aggregator used to gather data (ex: 'median' or 'mean'). Defaults to None.
            dataset_options (dict, optional): These are options directly related to the dataset object (i.e. options concerning your data). Defaults to None.
            options (dict, optional): All options to configure the chart. This dictionary corresponds to the "options" argument of Chart.js. Defaults to None.
            colorscheme (str, optional): colorscheme to use when drawing the chart. Defaults to None.
            horizontal (bool): draw the bar chart horizontally. Defaults to False.

        Returns:
            [ipychart.Chart]: A chart which display the data using ipychart
        """

        data = self._create_chart_data(kind='bar', x=x, y=y, hue=hue, agg=agg, dataset_options=dataset_options)
        options = self._create_chart_options(kind='bar', options=options, x=x, y=y, hue=hue)

        if horizontal:
            return Chart(data=data, kind='horizontalBar', options=options, colorscheme=colorscheme)
        else:
            return Chart(data=data, kind='bar', options=options, colorscheme=colorscheme)

    def radar(self, x: str, y: str, hue: str = None, agg: str = 'mean', dataset_options: dict = {},
              options: dict = None, colorscheme: str = None):
        """
        A radar chart is a way of showing multiple data points and the variation between them. They are often useful for comparing the points of two or more different data sets.

        Args:
            x (str, optional): Columns of the data dataframe used as datapoints for x Axis.
            y (str, optional): Columns of the data dataframe used as datapoints for y Axis.
            hue (str, optional): Grouping variable that will produce points with different colors. Defaults to None.
            agg (str, optional): The aggregator used to gather data (ex: 'median' or 'mean'). Defaults to None.
            dataset_options (dict, optional): These are options directly related to the dataset object (i.e. options concerning your data). Defaults to None.
            options (dict, optional): All options to configure the chart. This dictionary corresponds to the "options" argument of Chart.js. Defaults to None.
            colorscheme (str, optional): colorscheme to use when drawing the chart. Defaults to None.

        Returns:
            [ipychart.Chart]: A chart which display the data using ipychart
        """

        data = self._create_chart_data(kind='radar', x=x, y=y, hue=hue, agg=agg, dataset_options=dataset_options)
        options = self._create_chart_options(kind='radar', options=options, x=x, y=y, hue=hue)
        return Chart(data=data, kind='radar', options=options, colorscheme=colorscheme)

    def doughnut(self, x: str, y: str, agg: str = 'mean', dataset_options: dict = {},
                 options: dict = None, colorscheme: str = None):
        """
        Pie and doughnut charts are excellent at showing the relational proportions between data.

        Args:
            x (str, optional): Columns of the data dataframe used as datapoints for x Axis.
            y (str, optional): Columns of the data dataframe used as datapoints for y Axis.
            agg (str, optional): The aggregator used to gather data (ex: 'median' or 'mean'). Defaults to None.
            dataset_options (dict, optional): These are options directly related to the dataset object (i.e. options concerning your data). Defaults to None.
            options (dict, optional): All options to configure the chart. This dictionary corresponds to the "options" argument of Chart.js. Defaults to None.
            colorscheme (str, optional): colorscheme to use when drawing the chart. Defaults to None.

        Returns:
            [ipychart.Chart]: A chart which display the data using ipychart
        """

        data = self._create_chart_data(kind='doughnut', x=x, y=y, agg=agg, dataset_options=dataset_options)
        return Chart(data=data, kind='doughnut', options=options, colorscheme=colorscheme)

    def pie(self, x: str, y: str, agg: str = 'mean', dataset_options: dict = {},
            options: dict = None, colorscheme: str = None):
        """
        Pie and doughnut charts are excellent at showing the relational proportions between data.

        Args:
            x (str, optional): Columns of the data dataframe used as datapoints for x Axis.
            y (str, optional): Columns of the data dataframe used as datapoints for y Axis.
            agg (str, optional): The aggregator used to gather data (ex: 'median' or 'mean'). Defaults to None.
            dataset_options (dict, optional): These are options directly related to the dataset object (i.e. options concerning your data). Defaults to None.
            options (dict, optional): All options to configure the chart. This dictionary corresponds to the "options" argument of Chart.js. Defaults to None.
            colorscheme (str, optional): colorscheme to use when drawing the chart. Defaults to None.

        Returns:
            [ipychart.Chart]: A chart which display the data using ipychart
        """

        data = self._create_chart_data(kind='pie', x=x, y=y, agg=agg, dataset_options=dataset_options)
        return Chart(data=data, kind='pie', options=options, colorscheme=colorscheme)

    def polararea(self, x: str, y: str, agg: str = 'mean', dataset_options: dict = {},
                  options: dict = None, colorscheme: str = None):
        """
        Polar area charts are similar to pie charts, but each segment has the same angle - the radius of the segment differs depending on the value.

        Args:
            x (str, optional): Columns of the data dataframe used as datapoints for x Axis.
            y (str, optional): Columns of the data dataframe used as datapoints for y Axis.
            agg (str, optional): The aggregator used to gather data (ex: 'median' or 'mean'). Defaults to None.
            dataset_options (dict, optional): These are options directly related to the dataset object (i.e. options concerning your data). Defaults to None.
            options (dict, optional): All options to configure the chart. This dictionary corresponds to the "options" argument of Chart.js. Defaults to None.
            colorscheme (str, optional): colorscheme to use when drawing the chart. Defaults to None.

        Returns:
            [ipychart.Chart]: A chart which display the data using ipychart
        """

        data = self._create_chart_data(kind='polarArea', x=x, y=y, agg=agg, dataset_options=dataset_options)
        return Chart(data=data, kind='polarArea', options=options, colorscheme=colorscheme)

    def bubble(self, x: str, y: str, r: str, agg: str = 'mean', dataset_options: dict = {},
               options: dict = None, colorscheme: str = None):
        """
        A bubble chart is used to display three dimensions of data at the same time.
        The location of the bubble is determined by the first two dimensions and the corresponding horizontal and vertical axes.
        The third dimension is represented by the radius of the individual bubbles.

        Args:
            x (str, optional): Columns of the data dataframe used as datapoints for x Axis. Defaults to None.
            y (str, optional): Columns of the data dataframe used as datapoints for y Axis. Defaults to None.
            agg (str, optional): The aggregator used to gather data (ex: 'median' or 'mean'). Defaults to None.
            dataset_options (dict, optional): These are options directly related to the dataset object (i.e. options concerning your data). Defaults to None.
            options (dict, optional): All options to configure the chart. This dictionary corresponds to the "options" argument of Chart.js. Defaults to None.
            colorscheme (str, optional): colorscheme to use when drawing the chart. Defaults to None.

        Returns:
            [ipychart.Chart]: A chart which display the data using ipychart
        """

        data = self._create_chart_data(kind='bubble', x=x, y=y, agg=agg, dataset_options=dataset_options)
        return Chart(data=data, kind='bubble', options=options, colorscheme=colorscheme)

    def scatter(self, x: str, y: str, agg: str = 'mean', dataset_options: dict = {},
                options: dict = None, colorscheme: str = None):
        """
        Scatter charts are based on basic line charts with the x axis changed to a linear axis.

        Args:
            x (str, optional): Columns of the data dataframe used as datapoints for x Axis.
            y (str, optional): Columns of the data dataframe used as datapoints for y Axis.
            agg (str, optional): The aggregator used to gather data (ex: 'median' or 'mean'). Defaults to None.
            dataset_options (dict, optional): These are options directly related to the dataset object (i.e. options concerning your data). Defaults to None.
            options (dict, optional): All options to configure the chart. This dictionary corresponds to the "options" argument of Chart.js. Defaults to None.
            colorscheme (str, optional): colorscheme to use when drawing the chart. Defaults to None.

        Returns:
            [ipychart.Chart]: A chart which display the data using ipychart
        """

        data = self._create_chart_data(kind='scatter', x=x, y=y, agg=agg, dataset_options=dataset_options)
        return Chart(data=data, kind='scatter', options=options, colorscheme=colorscheme)
