import pandas as pd
import numpy as np

from typing import Union
from pydash import set_, merge
from pandas.api.types import is_numeric_dtype
from sklearn.neighbors import KernelDensity
from sklearn.model_selection import GridSearchCV

from .chart import Chart


def _create_chart_options(kind: str,
                          x: str,
                          y: str,
                          hue: str,
                          options: dict,
                          agg: str = None) -> dict:
    """
    This function will prepare all the options to create a chart from the
    input of the user. Axes labels are automatically set to match the names
    of the columns drawn on the chart. Legend is also modified to match the
    "hue" argument.

    Args:
        kind (str): The kind of the chart.

        x (str): Column of the dataframe used as datapoints for x Axis.

        y (str): Column of the dataframe used as datapoints for y Axis.

        hue (str, optional): Grouping variable that will produce points
                                with different colors. Defaults to None.

        options (dict, optional): All options to configure the chart.
                                    This dictionary corresponds to the
                                    "options" argument of Chart.js.
                                    Defaults to None.

        agg (str, optional): The aggregator used to gather data (ex:
                                'median' or 'mean'). Defaults to None.

    Returns:
        options (dict): options dictionary ready to be inputted into a
                        Chart class (i.e. match ipychart options format).
    """

    agg_label = '' if not agg else ' (' + agg + ')'
    radials = ['radar', 'pie', 'polarArea', 'doughnut']

    if kind not in radials:

        title_cb = (
            "function(tooltipItem, data) {"
            "return '%s = ' + tooltipItem[0].xLabel;};"
        ) % x

        label_cb = (
            "function(tooltipItem, data) {"
            "return '%s = ' + tooltipItem.yLabel;};"
        ) % (y + agg_label)

        default_options = {
            'scales': {
                'xAxes': [{'scaleLabel': {'display': True,
                                          'labelString': x}}],
                'yAxes': [{'scaleLabel': {'display': True,
                                          'labelString': y + agg_label}}]
            },
            'tooltips': {
                'enabled': True,
                'callbacks': {'title': title_cb, 'label': label_cb}
            }
        }

    else:

        y_value = (
            'tooltipItem.yLabel' if kind == 'radar' else
            'data.datasets[0].data[tooltipItem.index]'
        )

        title_cb = (
            "function(tooltipItem, data) {"
            "return '%s = ' + data.labels[tooltipItem[0].index];};" % x
        )

        label_cb = (
            "function(tooltipItem, data) {"
            "return '%s = ' + %s;};" % (y + agg_label, y_value)
        )

        default_options = {
            'legend': {'display': True},
            'tooltips': {
                'enabled': True,
                'callbacks': {'title': title_cb, 'label': label_cb}
            }
        }

    # Set legend prefix if "hue" if activated
    if hue:
        hue_label_cb = (
            "function(chart) {let labels = Chart.defaults.global."
            "legend.labels.generateLabels(chart);labels.map(label "
            """=> {label['text'] = "%s" + " = " + label['text']; """
            "return label});return labels;};"
        ) % hue

        hue_title_cb = (
            "function(tooltipItem, data) {return '%s = '"
            " + tooltipItem[0].xLabel + ' & ' + '%s = '"
            " + data.datasets[tooltipItem[0].datasetIndex].label;};"
        ) % (x, hue)

        default_options = set_(default_options,
                               'legend.labels.generateLabels',
                               hue_label_cb)

        default_options = set_(default_options,
                               'tooltips.callbacks.title',
                               hue_title_cb)

    options = merge(default_options, options)

    return options


def _create_chart_data_count(data: pd.DataFrame,
                             x: str,
                             dataset_options: Union[dict, list] = None
                             ) -> dict:
    """
    This function will prepare all the arguments to create a chart from the
    input of the user. Data are counted before being send to the Chart.

    Args:
        x (str): Column of the dataframe used as datapoints for x Axis.

        dataset_options ([dict, list], optional):
            These are options related to the dataset object
            (i.e. options concerning your data). Defaults to {}.

    Returns:
        data (dict): data dictionary ready to be inputted into a Chart
                        class (i.e. match ipychart data format).
    """

    assert x in data.columns, f'Column {x} not found in dataframe'

    if dataset_options is None:
        dataset_options = {}

    data_dict = {'datasets': []}

    if is_numeric_dtype(data[x]):

        data_dict['labels'] = (
            data[x].value_counts(sort=False)
                   .sort_index(ascending=True)
                   .index.tolist()
        )

        data_dict['datasets'].append(
            {'data': data[x].value_counts(sort=False)
                            .sort_index(ascending=True)
                            .round(4)
                            .tolist(),
                **dataset_options}
        )
    else:

        data_dict['labels'] = (
            data[x].value_counts(ascending=False, sort=True)
                   .index.tolist()
        )

        data_dict['datasets'].append(
            {'data': data[x].value_counts(ascending=False, sort=True)
                            .round(4).tolist(),
                **dataset_options}
        )

    return data_dict


def _create_chart_data_agg(data: pd.DataFrame,
                           kind: str,
                           x: str,
                           y: str,
                           r: str = None,
                           hue: str = None,
                           agg: str = None,
                           dataset_options: Union[dict, list] = None
                           ) -> dict:
    """
    This function will prepare all the arguments to create a chart from
    the input of the user. Data are automatically aggregated using the
    method specified in the "agg" argument before being send to the Chart.

    Args:
        kind (str): The kind of the chart.

        x (str): Column of the dataframe used as datapoints for x Axis.

        y (str): Column of the dataframe used as datapoints for y Axis.

        r (str, optional): Column used to define the radius of the bubbles
                            (only for bubble chart). Defaults to None.

        hue (str, optional): Grouping variable that will produce points
                                with different colors. Defaults to None.

        agg (str, optional): The aggregator used to gather data
                                (ex: 'median' or 'mean'). Defaults to None.

        dataset_options ([dict, list], optional):
            These are options related to the dataset object (i.e. options
            concerning your data). Defaults to {}.

    Returns:
        data (dict): data dictionary ready to be inputted into a Chart
                        class (i.e. match ipychart data format).
    """

    assert x in data.columns, f'{x} not found in dataframe'
    assert y in data.columns, f'{y} not found in dataframe'
    assert is_numeric_dtype(data[y]), 'y must be a numeric column'

    msg_kind = (
        'Chart kind must be one of : line, bar, radar, doughnut,'
        'polarArea, bubble, horizontalBar, pie, scatter. See '
        'https://nicohlr.gitlab.io/ipychart/user_guide/charts.html '
        'for more details'
    )

    kinds = ['line', 'bar', 'horizontalBar', 'radar', 'doughnut',
             'polarArea', 'bubble', 'pie', 'scatter']

    assert kind in kinds, msg_kind

    if dataset_options is None:
        dataset_options = {}

    if hue:
        assert hue in data.columns, f'{hue} not found in dataframe'
        assert data[hue].nunique() <= 20, 'Too much values in hue (>20)'

    if len(dataset_options):
        if isinstance(dataset_options, list):
            msg_hue_multiple_ds_options = (
                "For multiple dataset options, you must choose a column "
                "for hue that will create multiple datasets. Each dataset "
                "will corresponds to a unique value of the hue column."
            )

            msg_hue_number_ds_options = (
                "The number of dataset_options elements must be equal to "
                "the number of unique values in the hue column."
            )

            assert hue, msg_hue_multiple_ds_options
            df_options_check = len(dataset_options) == data[hue].nunique()
            assert df_options_check, msg_hue_number_ds_options

    data_dict = {'datasets': []}

    if kind not in ['scatter', 'bubble', 'radar']:

        data_dict['labels'] = (
            data[x].value_counts(ascending=True, sort=False)
                   .index.tolist()
        )

        if hue:
            # Create one dataset for each unique value of the hue column
            for i, v in enumerate(sorted(data[hue].unique())):

                if isinstance(dataset_options, list):
                    data_dict['datasets'].append(
                        {'data': data[data[hue] == v].groupby(x)
                                                     .agg(agg)[y]
                                                     .round(4)
                                                     .tolist(),
                         'label': v,
                         **dataset_options[i]}
                    )

                else:
                    data_dict['datasets'].append(
                        {'data': data[data[hue] == v].groupby(x)
                                                     .agg(agg)[y]
                                                     .round(4)
                                                     .tolist(),
                         'label': v,
                         **dataset_options}
                    )
        else:
            data_dict['datasets'] = [
                {'data': data.groupby(x).agg(agg)[y].round(4).tolist(),
                 'label': y, **dataset_options}
            ]

    elif kind == 'bubble':

        assert is_numeric_dtype(data[r]), 'r must be a numeric column'
        assert is_numeric_dtype(data[x]), 'x must be a numeric column'

        data_dict['labels'] = data[x].tolist()

        def row2dictxyr(row):
            return {'x': row[x], 'y': row[y], 'r': row[r]}

        if hue:

            # Create one dataset for each unique value of the hue column
            for i, v in enumerate(data[hue].unique()):

                mask = data[hue] == v
                if isinstance(dataset_options, list):
                    data_dict['datasets'].append(
                        {'data': data[mask].apply(row2dictxyr, 1).tolist(),
                         'label': v, **dataset_options[i]}
                    )

                else:
                    data_dict['datasets'].append(
                        {'data': data[mask].apply(row2dictxyr, 1).tolist(),
                         'label': v, **dataset_options}
                    )
        else:
            data_dict['datasets'] = [
                {'data': data.apply(row2dictxyr, 1).tolist(),
                 **dataset_options}
            ]

    elif kind == 'scatter':

        assert is_numeric_dtype(data[x]), 'x must be a numeric column'

        data_dict['labels'] = data[x].tolist()

        def row2dictxy(row):
            return {'x': row[x], 'y': row[y]}

        if hue:
            # Create one dataset for each unique value of the hue column
            for i, v in enumerate(data[hue].unique()):

                mask = data[hue] == v
                if isinstance(dataset_options, list):
                    data_dict['datasets'].append(
                        {'data': data[mask].apply(row2dictxy, 1).tolist(),
                         'label': v, **dataset_options[i]}
                    )

                else:
                    data_dict['datasets'].append(
                        {'data': data[mask].apply(row2dictxy, 1).tolist(),
                         'label': v, **dataset_options}
                    )
        else:
            data_dict['datasets'] = [
                {'data': data.apply(row2dictxy, 1).tolist(), **dataset_options}
            ]

    else:

        agg_label = '' if not agg else ' (' + agg + ')'
        data_dict['labels'] = data[x].value_counts(
            ascending=True, sort=False).index.tolist()

        if hue:
            # Create one dataset for each unique value of the hue column
            for i, v in enumerate(data[hue].unique()):

                mask = data[hue] == v
                if isinstance(dataset_options, list):
                    data_dict['datasets'].append(
                        {'data': data[mask].groupby(x)
                                           .agg(agg)[y]
                                           .round(4)
                                           .tolist(),
                         'label': v,
                         **dataset_options[i]}
                    )

                else:
                    data_dict['datasets'].append(
                        {'data': data[mask].groupby(x)
                                           .agg(agg)[y]
                                           .round(4)
                                           .tolist(),
                         'label': v,
                         **dataset_options}
                    )
        else:
            data_dict['datasets'] = [
                {'data': data.groupby(x).agg(agg)[y].round(4).tolist(),
                 'label': y + agg_label,
                 **dataset_options}
            ]

    return data_dict


def countplot(data: pd.DataFrame,
              x: str,
              horizontal: bool = False,
              dataset_options: dict = None,
              options: dict = None,
              colorscheme: str = None,
              zoom: bool = True) -> Chart:
    """
    Show the counts of observations in each categorical bin using bars.

    Args:
        x (str): Column of the dataframe used as datapoints for x Axis.

        horizontal (bool): Draw the bar chart horizontally. Defaults to
                            False.
        dataset_options (dict, optional):
            These are options related to the dataset object (i.e. options
            concerning your data). Defaults to {}.

        options (dict, optional): All options to configure the chart. This
                                    dictionary corresponds to the "options"
                                    argument of Chart.js. Defaults to None.

        colorscheme (str, optional): Colorscheme to use when drawing the
                                        chart. Defaults to None.

        zoom (bool, optional): Allow the user to zoom on the Chart once it
                                is created. Defaults to True.

    Returns:
        [ipychart.Chart]: A chart which display the data using ipychart.
    """

    if dataset_options is None:
        dataset_options = {}

    data = _create_chart_data_count(
        data=data,
        x=x,
        dataset_options=dataset_options
    )

    if horizontal:
        options = _create_chart_options(
            kind='count',
            options=options,
            x='Count',
            y=x,
            hue=None
        )
    else:
        options = _create_chart_options(
            kind='count',
            options=options,
            x=x,
            y='Count',
            hue=None
        )

    kind = 'horizontalBar' if horizontal else 'bar'

    return Chart(
        data=data,
        kind=kind,
        options=options,
        colorscheme=colorscheme,
        zoom=zoom
    )


def distplot(data: pd.DataFrame,
             x: str,
             bandwidth: Union[float, str] = 'auto',
             gridsize: int = 1000,
             dataset_options: dict = None,
             options: dict = None,
             colorscheme: str = None,
             zoom: bool = True, **kwargs) -> Chart:
    """
    Fit and plot a univariate kernel density estimate on a line chart.
    This is useful to have a representation of the distribution of the
    data.

    Args:
        x (str): Column of the dataframe used as datapoints for x Axis.

        bandwidth ([float, str], optional):
            Parameter which affect how “smooth” the resulting curve is.
            If set to 'auto', the optimal bandwidth is found using
            gridsearch. Defaults to 'auto'.

        gridsize (int, optional): Number of discrete points in the
                                    evaluation grid. Defaults to 1000.

        dataset_options (dict, optional):
            These are options related to the dataset object (i.e. options
            concerning your data). Defaults to {}.

        options (dict, optional): All options to configure the chart. This
                                    dictionary corresponds to the "options"
                                    argument of Chart.js. Defaults to None.

        colorscheme (str, optional): Colorscheme to use when drawing the
                                        chart. Defaults to None.

        zoom (bool, optional): Allow the user to zoom on the Chart once it
                                is created. Defaults to True.

        kwargs (optionnal): Other keyword arguments are passed down to
                            scikit-learn's KernelDensity class.

    Returns:
        [ipychart.Chart]: A chart which display the data using ipychart.
    """

    assert is_numeric_dtype(data[x]), 'x must be a numeric column'
    if isinstance(bandwidth, str):
        assert bandwidth == 'auto', "bandwidth must be an int or 'auto'"

    if dataset_options is None:
        dataset_options = {}

    # Remove outliers to find max and min values for the x axis
    iqr = data[x].quantile(0.95) - data[x].quantile(0.05)

    data_truncated = data[x][
        ~((data[x] < (data[x].quantile(0.05) - 0.5 * iqr)) |
            (data[x] > (data[x].quantile(0.95) + 0.5 * iqr)))
    ]

    max_val, min_val = (int(data_truncated.max()) + 1,
                        int(data_truncated.min()))

    max_val, min_val = (max_val + 0.05 * (max_val + abs(min_val)),
                        min_val - 0.05 * (max_val + abs(min_val)))

    # Create grid which will be used to compute kde
    _, step = np.linspace(min_val, max_val, num=gridsize, retstep=True)
    x_grid = np.round(np.arange(min_val, max_val, step), 5)

    # If bandwidth is 'auto', find the best bandwidh using gridsearch
    if bandwidth == 'auto':
        grid = GridSearchCV(KernelDensity(),
                            {'bandwidth': np.linspace(0.1, 2, 30)}, cv=5)
        grid.fit(data[x].dropna().to_numpy()[:, None])
        bandwidth = grid.best_params_['bandwidth']

    kde_skl = KernelDensity(bandwidth=bandwidth, **kwargs)
    kde_skl.fit(data[x].dropna().to_numpy()[:, np.newaxis])
    pdf = np.exp(kde_skl.score_samples(x_grid[:, np.newaxis]))

    data = {
        'labels': x_grid.tolist(),
        'datasets': [{'data': pdf.tolist(), 'pointRadius': 0,
                      **dataset_options}]
    }

    options = _create_chart_options(
        kind='count',
        options=options,
        x=x,
        y=f'Density (bandwidth: {bandwidth.round(4)})',
        hue=None
    )

    # Add ticks formatting to options if not already set
    # This will not break because keys are created in the
    # _create_chart_options method called previouly
    maxtickslimit = 10
    ticks_format_function = (
        "function(value, index, values) {if (Math.abs(value) >= 1) {"
        "return Math.round(value);} else {return value.toFixed(3);}}"
    )

    if 'ticks' not in options['scales']['xAxes'][0]:
        options['scales']['xAxes'][0].update(
            {'ticks': {'maxTicksLimit': maxtickslimit,
                       'callback': ticks_format_function}}
        )
    else:
        ticks_options = options['scales']['xAxes'][0]['ticks']
        if 'maxTicksLimit' not in ticks_options:
            ticks_options['maxTicksLimit'] = maxtickslimit
        if 'callback' not in ticks_options:
            ticks_options['callback'] = ticks_format_function

    return Chart(
        data=data,
        kind='line',
        options=options,
        colorscheme=colorscheme,
        zoom=zoom
    )


def lineplot(data: pd.DataFrame,
             x: str,
             y: str,
             hue: str = None,
             agg: str = 'mean',
             dataset_options: Union[dict, list] = None,
             options: dict = None,
             colorscheme: str = None,
             zoom: bool = True) -> Chart:
    """
    A line chart is a way of plotting data points on a line. Often, it is
    used to show a trend in the data, or the comparison of two data sets.

    Args:
        x (str): Column of the dataframe used as datapoints for x Axis.

        y (str): Column of the dataframe used as datapoints for y Axis.

        hue (str, optional): Grouping variable that will produce points
                                with different colors. Defaults to None.

        agg (str, optional): The aggregator used to gather data (ex:
                                'median' or 'mean'). Defaults to None.

        dataset_options ([dict, list], optional):
            These are options related to the dataset object (i.e. options
            concerning your data). Defaults to {}.

        options (dict, optional): All options to configure the chart. This
                                    dictionary corresponds to the "options"
                                    argument of Chart.js. Defaults to None.

        colorscheme (str, optional): Colorscheme to use when drawing the
                                        chart. Defaults to None.

        zoom (bool, optional): Allow the user to zoom on the Chart once it
                                is created. Defaults to True.

    Returns:
        [ipychart.Chart]: A chart which display the data using ipychart.
    """

    if dataset_options is None:
        dataset_options = {}

    data = _create_chart_data_agg(
        data=data,
        kind='line',
        x=x,
        y=y,
        hue=hue,
        agg=agg,
        dataset_options=dataset_options
    )

    options = _create_chart_options(
        kind='line',
        options=options,
        x=x,
        y=y,
        hue=hue,
        agg=agg
    )

    return Chart(
        data=data,
        kind='line',
        options=options,
        colorscheme=colorscheme,
        zoom=zoom
    )


def barplot(data: pd.DataFrame,
            x: str,
            y: str,
            hue: str = None,
            horizontal: bool = False,
            agg: str = 'mean',
            dataset_options: Union[dict, list] = None,
            options: dict = None,
            colorscheme: str = None,
            zoom: bool = True) -> Chart:
    """
    A bar chart provides a way of showing data values represented as
    vertical bars. It is sometimes used to show a trend in the data,
    and the comparison of multiple data sets side by side.

    Args:
        x (str): Column of the dataframe used as datapoints for x Axis.

        y (str): Column of the dataframe used as datapoints for y Axis.

        hue (str, optional): Grouping variable that will produce points
                                with different colors. Defaults to None.

        horizontal (bool): Draw the bar chart horizontally.
                            Defaults to False.

        agg (str, optional): The aggregator used to gather data (ex:
                                'median' or 'mean'). Defaults to None.

        dataset_options ([dict, list], optional):
            These are options related to the dataset object (i.e. options
            concerning your data). Defaults to {}.

        options (dict, optional): All options to configure the chart. This
                                    dictionary corresponds to the "options"
                                    argument of Chart.js. Defaults to None.

        colorscheme (str, optional): Colorscheme to use when drawing the
                                        chart. Defaults to None.

        zoom (bool, optional): Allow the user to zoom on the Chart once it
                                is created. Defaults to True.

    Returns:
        [ipychart.Chart]: A chart which display the data using ipychart.
    """

    if dataset_options is None:
        dataset_options = {}

    data = _create_chart_data_agg(
        data=data,
        kind='bar',
        x=x,
        y=y,
        hue=hue,
        agg=agg,
        dataset_options=dataset_options
    )

    options = _create_chart_options(
        kind='bar',
        options=options,
        x=x,
        y=y,
        hue=hue,
        agg=agg
    )

    kind = 'horizontalBar' if horizontal else 'bar'

    return Chart(
        data=data,
        kind=kind,
        options=options,
        colorscheme=colorscheme,
        zoom=zoom
    )


def radarplot(data: pd.DataFrame,
              x: str,
              y: str,
              hue: str = None,
              agg: str = 'mean',
              dataset_options: Union[dict, list] = None,
              options: dict = None,
              colorscheme: str = None) -> Chart:
    """
    A radar chart is a way of showing multiple data points and the
    variation between them. They are often useful for comparing the
    points of two or more different data sets.

    Args:
        x (str): Column of the dataframe used as datapoints for x Axis.

        y (str): Column of the dataframe used as datapoints for y Axis.

        hue (str, optional): Grouping variable that will produce points
                                with different colors. Defaults to None.

        agg (str, optional): The aggregator used to gather data (ex:
                                'median' or 'mean'). Defaults to None.

        dataset_options ([dict, list], optional):
            These are options related to the dataset object (i.e. options
            concerning your data). Defaults to {}.

        options (dict, optional): All options to configure the chart. This
                                    dictionary corresponds to the "options"
                                    argument of Chart.js. Defaults to None.

        colorscheme (str, optional): Colorscheme to use when drawing the
                                        chart. Defaults to None.

    Returns:
        [ipychart.Chart]: A chart which display the data using ipychart.
    """

    if dataset_options is None:
        dataset_options = {}

    data = _create_chart_data_agg(
        data=data,
        kind='radar',
        x=x,
        y=y,
        hue=hue,
        agg=agg,
        dataset_options=dataset_options
    )

    options = _create_chart_options(
        kind='radar',
        options=options,
        x=x,
        y=y,
        hue=hue,
        agg=agg
    )

    return Chart(
        data=data,
        kind='radar',
        options=options,
        colorscheme=colorscheme
    )


def doughnutplot(data: pd.DataFrame,
                 x: str,
                 y: str = None,
                 agg: str = 'mean',
                 dataset_options: dict = None,
                 options: dict = None,
                 colorscheme: str = None) -> Chart:
    """
    Pie and doughnut charts are excellent at showing the relational
    proportions between data.

    Args:
        x (str): Column of the dataframe used as datapoints for x Axis.

        y (str, optional): Column of the dataframe used as datapoints for
                            y Axis. Defaults to None.

        agg (str, optional): The aggregator used to gather data (ex:
                                'median' or 'mean'). Defaults to None.

        dataset_options (dict, optional):
            These are options related to the dataset object (i.e. options
            concerning your data). Defaults to {}.

        options (dict, optional): All options to configure the chart. This
                                    dictionary corresponds to the "options"
                                    argument of Chart.js. Defaults to None.

        colorscheme (str, optional): Colorscheme to use when drawing the
                                        chart. Defaults to None.

    Returns:
        [ipychart.Chart]: A chart which display the data using ipychart.
    """

    if dataset_options is None:
        dataset_options = {}

    if y:
        data = _create_chart_data_agg(
            data=data,
            kind='doughnut',
            x=x,
            y=y,
            agg=agg,
            dataset_options=dataset_options
        )

    else:
        data = _create_chart_data_count(
            data=data,
            x=x,
            dataset_options=dataset_options
        )

    options = _create_chart_options(
        kind='doughnut',
        options=options,
        x=x,
        y=y,
        hue=None,
        agg=agg
    )

    return Chart(
        data=data,
        kind='doughnut',
        options=options,
        colorscheme=colorscheme
    )


def pieplot(data: pd.DataFrame,
            x: str,
            y: str = None,
            agg: str = 'mean',
            dataset_options: dict = None,
            options: dict = None,
            colorscheme: str = None) -> Chart:
    """
    Pie and doughnut charts are excellent at showing the relational
    proportions between data.

    Args:
        x (str): Column of the dataframe used as datapoints for x Axis.

        y (str, optional): Column of the dataframe used as datapoints for
                            y Axis. Defaults to None.

        agg (str, optional): The aggregator used to gather data (ex:
                                'median' or 'mean'). Defaults to None.

        dataset_options (dict, optional):
            These are options related to the dataset object (i.e. options
            concerning your data). Defaults to {}.

        options (dict, optional): All options to configure the chart. This
                                    dictionary corresponds to the "options"
                                    argument of Chart.js. Defaults to None.

        colorscheme (str, optional): Colorscheme to use when drawing the
                                        chart. Defaults to None.

    Returns:
        [ipychart.Chart]: A chart which display the data using ipychart.
    """

    if dataset_options is None:
        dataset_options = {}

    if y:
        data = _create_chart_data_agg(
            data=data,
            kind='pie',
            x=x,
            y=y,
            agg=agg,
            dataset_options=dataset_options
        )

    else:
        data = _create_chart_data_count(
            data=data,
            x=x,
            dataset_options=dataset_options
        )

    options = _create_chart_options(
        kind='pie',
        options=options,
        x=x,
        y=y,
        hue=None,
        agg=agg
    )

    return Chart(
        data=data,
        kind='pie',
        options=options,
        colorscheme=colorscheme
    )


def polarplot(data: pd.DataFrame,
              x: str,
              y: str = None,
              agg: str = 'mean',
              dataset_options: dict = None,
              options: dict = None,
              colorscheme: str = None) -> Chart:
    """
    Polar area charts are similar to pie charts, but each segment has the
    same angle - the radius of the segment differs depending on the value.

    Args:
        x (str): Column of the dataframe used as datapoints for x Axis.

        y (str, optional): Column of the dataframe used as datapoints for
                            y Axis. Defaults to None.

        agg (str, optional): The aggregator used to gather data (ex:
                                'median' or 'mean'). Defaults to None.

        dataset_options (dict, optional):
            These are options related to the dataset object (i.e. options
            concerning your data). Defaults to {}.

        options (dict, optional): All options to configure the chart. This
                                    dictionary corresponds to the "options"
                                    argument of Chart.js. Defaults to None.

        colorscheme (str, optional): Colorscheme to use when drawing the
                                        chart. Defaults to None.

    Returns:
        [ipychart.Chart]: A chart which display the data using ipychart.
    """

    if dataset_options is None:
        dataset_options = {}

    if y:
        data = _create_chart_data_agg(
            data=data,
            kind='polarArea',
            x=x,
            y=y,
            agg=agg,
            dataset_options=dataset_options
        )

    else:
        data = _create_chart_data_count(
            data=data,
            x=x,
            dataset_options=dataset_options
        )

    options = _create_chart_options(
        kind='polarArea',
        options=options,
        x=x,
        y=y,
        hue=None,
        agg=agg
    )

    return Chart(
        data=data,
        kind='polarArea',
        options=options,
        colorscheme=colorscheme
    )


def scatterplot(data: pd.DataFrame,
                x: str,
                y: str,
                hue: str = None,
                dataset_options: Union[dict, list] = None,
                options: dict = None,
                colorscheme: str = None,
                zoom: bool = True) -> Chart:
    """
    Scatter charts are based on basic line charts with the x axis changed
    to a linear axis.

    Args:
        x (str): Column of the dataframe used as datapoints for x Axis.

        y (str): Column of the dataframe used as datapoints for y Axis.

        hue (str, optional): Grouping variable that will produce points
                                with different colors. Defaults to None.

        dataset_options ([dict, list], optional):
            These are options related to the dataset object (i.e. options
            concerning your data). Defaults to {}.

        options (dict, optional): All options to configure the chart. This
                                    dictionary corresponds to the "options"
                                    argument of Chart.js. Defaults to None.

        colorscheme (str, optional): Colorscheme to use when drawing the
                                        chart. Defaults to None.

        zoom (bool, optional): Allow the user to zoom on the Chart once it
                                is created. Defaults to True.

    Returns:
        [ipychart.Chart]: A chart which display the data using ipychart.
    """

    if dataset_options is None:
        dataset_options = {}

    data = _create_chart_data_agg(
        data=data,
        kind='scatter',
        x=x,
        y=y,
        hue=hue,
        dataset_options=dataset_options
    )

    options = _create_chart_options(
        kind='scatter',
        options=options,
        x=x,
        y=y,
        hue=hue
    )

    return Chart(
        data=data,
        kind='scatter',
        options=options,
        colorscheme=colorscheme,
        zoom=zoom
    )


def bubbleplot(data: pd.DataFrame,
               x: str,
               y: str,
               r: str,
               hue: str = None,
               dataset_options: Union[dict, list] = None,
               options: dict = None,
               colorscheme: str = None,
               zoom: bool = True) -> Chart:
    """
    A bubble chart is used to display three-dimension data.

    The location of the bubble is determined by the first two dimensions
    and the corresponding horizontal and vertical axes.

    The third dimension is represented by the radius of the individual
    bubbles.

    Args:
        x (str): Column of the dataframe used as datapoints for x Axis.

        y (str): Column of the dataframe used as datapoints for y Axis.

        r (str, optional): Column of the dataframe used as radius for
                            bubbles.

        hue (str, optional): Grouping variable that will produce points
                                with different colors. Defaults to None.

        dataset_options ([dict, list], optional):
            These are options related to the dataset object (i.e. options
            concerning your data). Defaults to {}.

        options (dict, optional): All options to configure the chart. This
                                    dictionary corresponds to the "options"
                                    argument of Chart.js. Defaults to None.

        colorscheme (str, optional): Colorscheme to use when drawing the
                                        chart. Defaults to None.

        zoom (bool, optional): Allow the user to zoom on the Chart once it
                                is created. Defaults to True.

    Returns:
        [ipychart.Chart]: A chart which display the data using ipychart.
    """

    if dataset_options is None:
        dataset_options = {}

    data = _create_chart_data_agg(
        data=data,
        kind='bubble',
        x=x,
        y=y,
        r=r,
        hue=hue,
        dataset_options=dataset_options
    )

    options = _create_chart_options(
        kind='bubble',
        options=options,
        x=x,
        y=y,
        hue=hue
    )

    return Chart(
        data=data,
        kind='bubble',
        options=options,
        colorscheme=colorscheme,
        zoom=zoom
    )
