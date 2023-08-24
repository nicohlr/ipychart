import pandas as pd
import numpy as np

from typing import Union
from pandas.api.types import is_numeric_dtype
from sklearn.neighbors import KernelDensity
from sklearn.model_selection import GridSearchCV

from .chart import Chart
from .utils.plots_utils import (
    _create_chart_options,
    _create_chart_data_agg,
    _create_chart_data_count,
)


def countplot(
    data: pd.DataFrame,
    x: str,
    hue: Union[str, None] = None,
    dataset_options: Union[dict, None] = None,
    options: Union[dict, None] = None,
    colorscheme: Union[str, None] = None,
    zoom: bool = True,
) -> Chart:
    """
    Show the counts of observations in each categorical bin using bars.

    Args:
        data (pd.DataFrame): The dataframe used to draw the chart.

        x (str): Column of the dataframe used as datapoints for x Axis.

        hue (str, optional): Grouping variable that will produce points
            with different colors. Defaults to None.

        dataset_options (dict, optional): Options related to the dataset
            object (i.e. options concerning your data). Defaults to {}.

        options (dict, optional): Options to configure the chart. This
            dictionary corresponds to the "options" argument of Chart.js.
            Defaults to None.

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
        data=data, x=x, hue=hue, dataset_options=dataset_options
    )

    options = _create_chart_options(
        kind="count", options=options, x=x, y="Count", hue=hue
    )

    return Chart(
        data=data,
        kind="bar",
        options=options,
        colorscheme=colorscheme,
        zoom=zoom,
    )


def distplot(
    data: pd.DataFrame,
    x: str,
    bandwidth: Union[float, str] = "auto",
    gridsize: int = 1000,
    dataset_options: Union[dict, None] = None,
    options: Union[dict, None] = None,
    colorscheme: Union[str, None] = None,
    zoom: bool = True,
    **kwargs,
) -> Chart:
    """
    Fit and plot a univariate kernel density estimate on a line chart.

    This is useful to have a representation of the distribution of the
    data.

    Args:
        data (pd.DataFrame): The dataframe used to draw the chart.

        x (str): Column of the dataframe used as datapoints for x Axis.

        bandwidth ([float, str], optional): Parameter which affect how
        “smooth” the resulting curve is. If set to 'auto', the optimal
        bandwidth is found using gridsearch. Defaults to 'auto'.

        gridsize (int, optional): Number of discrete points in the
            evaluation grid. Defaults to 1000.

        dataset_options (dict, optional): Options related to the dataset
            object (i.e. options concerning your data). Defaults to {}.

        options (dict, optional): Options to configure the chart. This
            dictionary corresponds to the "options" argument of Chart.js.
            Defaults to None.

        colorscheme (str, optional): Colorscheme to use when drawing the chart.
            Defaults to None.

        zoom (bool, optional): Allow the user to zoom on the Chart once it
            is created. Defaults to True.

        kwargs (optionnal): Other keyword arguments are passed down to
            scikit-learn's KernelDensity class.

    Returns:
        [ipychart.Chart]: A chart which display the data using ipychart.
    """
    assert is_numeric_dtype(data[x]), "x must be a numeric column"
    if isinstance(bandwidth, str):
        assert bandwidth == "auto", "bandwidth must be an int or 'auto'"

    if dataset_options is None:
        dataset_options = {}

    # Remove outliers to find max and min values for the x axis
    iqr = data[x].quantile(0.95) - data[x].quantile(0.05)

    data_truncated = data[x][
        ~(
            (data[x] < (data[x].quantile(0.05) - 0.5 * iqr))
            | (data[x] > (data[x].quantile(0.95) + 0.5 * iqr))
        )
    ]

    max_val, min_val = (
        int(data_truncated.max()) + 1,
        int(data_truncated.min()),
    )

    max_val, min_val = (
        max_val + 0.05 * (max_val + abs(min_val)),
        min_val - 0.05 * (max_val + abs(min_val)),
    )

    # Create grid which will be used to compute kde
    _, step = np.linspace(min_val, max_val, num=gridsize, retstep=True)
    x_grid = np.round(np.arange(min_val, max_val, step), 5)

    # If bandwidth is 'auto', find the best bandwidh using gridsearch
    if bandwidth == "auto":
        grid = GridSearchCV(
            KernelDensity(), {"bandwidth": np.linspace(0.1, 2, 30)}, cv=5
        )
        grid.fit(data[x].dropna().to_numpy()[:, None])
        bandwidth = grid.best_params_["bandwidth"]

    kde_skl = KernelDensity(bandwidth=bandwidth, **kwargs)
    kde_skl.fit(data[x].dropna().to_numpy()[:, np.newaxis])
    pdf = np.exp(kde_skl.score_samples(x_grid[:, np.newaxis]))

    data = {
        "labels": x_grid.tolist(),
        "datasets": [
            {"data": pdf.tolist(), "pointRadius": 0, **dataset_options}
        ],
    }

    options = _create_chart_options(
        kind="count",
        options=options,
        x=x,
        y=f"Density (bandwidth: {bandwidth.round(4)})",
        hue=None,
    )

    # Add ticks formatting to options if not already set
    # This will not break because keys are created in the
    # _create_chart_options method called previouly
    maxtickslimit = 10
    ticks_format_function = (
        "function(value, index, ticks) {if (Math.abs(value) >= 1) {"
        "return Math.round(value);} else {return value.toFixed(3);}}"
    )

    if "ticks" not in options["scales"]["x"]:
        options["scales"]["x"].update(
            {
                "ticks": {
                    "maxTicksLimit": maxtickslimit,
                    "callback": ticks_format_function,
                }
            }
        )
    else:
        ticks_options = options["scales"]["x"]["ticks"]
        if "maxTicksLimit" not in ticks_options:
            ticks_options["maxTicksLimit"] = maxtickslimit
        if "callback" not in ticks_options:
            ticks_options["callback"] = ticks_format_function

    return Chart(
        data=data,
        kind="line",
        options=options,
        colorscheme=colorscheme,
        zoom=zoom,
    )


def lineplot(
    data: pd.DataFrame,
    x: str,
    y: str,
    hue: Union[str, None] = None,
    agg: str = "mean",
    dataset_options: Union[dict, list, None] = None,
    options: Union[dict, None] = None,
    colorscheme: Union[str, None] = None,
    zoom: bool = True,
) -> Chart:
    """
    Plot a line chart.

    A line chart is a way of plotting data points on a line. Often, it is
    used to show a trend in the data, or the comparison of two data sets.

    Args:
        data (pd.DataFrame): The dataframe used to draw the chart.

        x (str): Column of the dataframe used as datapoints for x Axis.

        y (str): Column of the dataframe used as datapoints for y Axis.

        hue (str, optional): Grouping variable that will produce points with
            different colors. Defaults to None.

        agg (str, optional): The aggregator used to gather data (ex: 'median'
            or 'mean'). Defaults to None.

        dataset_options ([dict, list], optional): Options related to the
            dataset object (i.e. options concerning your data). Defaults to {}.

        options (dict, optional): Options to configure the chart. This
            dictionary corresponds to the "options" argument of Chart.js.
            Defaults to None.

        colorscheme (str, optional): Colorscheme to use when drawing the chart.
            Defaults to None.

        zoom (bool, optional): Allow the user to zoom on the Chart once it is
            created. Defaults to True.

    Returns:
        [ipychart.Chart]: A chart which display the data using ipychart.
    """
    if dataset_options is None:
        dataset_options = {}

    data = _create_chart_data_agg(
        data=data,
        kind="line",
        x=x,
        y=y,
        hue=hue,
        agg=agg,
        dataset_options=dataset_options,
    )

    options = _create_chart_options(
        kind="line", options=options, x=x, y=y, hue=hue, agg=agg
    )

    return Chart(
        data=data,
        kind="line",
        options=options,
        colorscheme=colorscheme,
        zoom=zoom,
    )


def barplot(
    data: pd.DataFrame,
    x: str,
    y: str,
    hue: Union[str, None] = None,
    agg: str = "mean",
    dataset_options: Union[dict, list, None] = None,
    options: Union[dict, None] = None,
    colorscheme: Union[str, None] = None,
    zoom: bool = True,
) -> Chart:
    """
    Plot a bar chart.

    A bar chart provides a way of showing data values represented as
    vertical bars. It is sometimes used to show a trend in the data,
    and the comparison of multiple data sets side by side.

    Args:
        data (pd.DataFrame): The dataframe used to draw the chart.

        x (str): Column of the dataframe used as datapoints for x Axis.

        y (str): Column of the dataframe used as datapoints for y Axis.

        hue (str, optional): Grouping variable that will produce points with
            different colors. Defaults to None.

        agg (str, optional): The aggregator used to gather data (ex: 'median'
            or 'mean'). Defaults to None.

        dataset_options ([dict, list], optional): Options related to the
            dataset object (i.e. options concerning your data). Defaults to {}.

        options (dict, optional): Options to configure the chart. This
            dictionary corresponds to the "options" argument of Chart.js.
            Defaults to None.

        colorscheme (str, optional): Colorscheme to use when drawing the chart.
            Defaults to None.

        zoom (bool, optional): Allow the user to zoom on the Chart once it is
            created. Defaults to True.

    Returns:
        [ipychart.Chart]: A chart which display the data using ipychart.
    """
    if dataset_options is None:
        dataset_options = {}

    data = _create_chart_data_agg(
        data=data,
        kind="bar",
        x=x,
        y=y,
        hue=hue,
        agg=agg,
        dataset_options=dataset_options,
    )

    options = _create_chart_options(
        kind="bar", options=options, x=x, y=y, hue=hue, agg=agg
    )

    return Chart(
        data=data,
        kind="bar",
        options=options,
        colorscheme=colorscheme,
        zoom=zoom,
    )


def radarplot(
    data: pd.DataFrame,
    x: str,
    y: str,
    hue: Union[str, None] = None,
    agg: str = "mean",
    dataset_options: Union[dict, list, None] = None,
    options: Union[dict, None] = None,
    colorscheme: Union[str, None] = None,
) -> Chart:
    """
    Plot a radar chart.

    A radar chart is a way of showing multiple data points and the
    variation between them. They are often useful for comparing the
    points of two or more different data sets.

    Args:
        data (pd.DataFrame): The dataframe used to draw the chart.

        x (str): Column of the dataframe used as datapoints for x Axis.

        y (str): Column of the dataframe used as datapoints for y Axis.

        hue (str, optional): Grouping variable that will produce points with
            different colors. Defaults to None.

        agg (str, optional): The aggregator used to gather data (ex: 'median'
            or 'mean'). Defaults to None.

        dataset_options ([dict, list], optional): Options related to the
            dataset object (i.e. options concerning your data). Defaults to {}.

        options (dict, optional): Options to configure the chart. This
            dictionary corresponds to the "options" argument of Chart.js.
            Defaults to None.

        colorscheme (str, optional): Colorscheme to use when drawing the chart.
            Defaults to None.

    Returns:
        [ipychart.Chart]: A chart which display the data using ipychart.
    """
    if dataset_options is None:
        dataset_options = {}

    data = _create_chart_data_agg(
        data=data,
        kind="radar",
        x=x,
        y=y,
        hue=hue,
        agg=agg,
        dataset_options=dataset_options,
    )

    options = _create_chart_options(
        kind="radar", options=options, x=x, y=y, hue=hue, agg=agg
    )

    return Chart(
        data=data, kind="radar", options=options, colorscheme=colorscheme
    )


def doughnutplot(
    data: pd.DataFrame,
    x: str,
    y: str,
    agg: str = "mean",
    dataset_options: Union[dict, None] = None,
    options: Union[dict, None] = None,
    colorscheme: Union[str, None] = None,
) -> Chart:
    """
    Plot a doughnut chart.

    Pie and doughnut charts are excellent at showing the relational
    proportions between data.

    Args:
        data (pd.DataFrame): The dataframe used to draw the chart.

        x (str): Column of the dataframe used as datapoints for x Axis.

        y (str): Column of the dataframe used as datapoints for y Axis.

        agg (str, optional): The aggregator used to gather data (ex: 'median'
            or 'mean'). Defaults to None.

        dataset_options (dict, optional): Options related to the dataset
            object (i.e. options concerning your data). Defaults to {}.

        options (dict, optional): Options to configure the chart. This
            dictionary corresponds to the "options" argument of Chart.js.
            Defaults to None.

        colorscheme (str, optional): Colorscheme to use when drawing the chart.
            Defaults to None.

    Returns:
        [ipychart.Chart]: A chart which display the data using ipychart.
    """
    if dataset_options is None:
        dataset_options = {}

    if y:
        data = _create_chart_data_agg(
            data=data,
            kind="doughnut",
            x=x,
            y=y,
            agg=agg,
            dataset_options=dataset_options,
        )

    else:
        data = _create_chart_data_count(
            data=data, x=x, dataset_options=dataset_options
        )

    options = _create_chart_options(
        kind="doughnut", options=options, x=x, y=y, hue=None, agg=agg
    )

    return Chart(
        data=data, kind="doughnut", options=options, colorscheme=colorscheme
    )


def pieplot(
    data: pd.DataFrame,
    x: str,
    y: str = None,
    agg: str = "mean",
    dataset_options: Union[dict, None] = None,
    options: Union[dict, None] = None,
    colorscheme: Union[str, None] = None,
) -> Chart:
    """
    Plot a pie chart.

    Pie and doughnut charts are excellent at showing the relational
    proportions between data.

    Args:
        data (pd.DataFrame): The dataframe used to draw the chart.

        x (str): Column of the dataframe used as datapoints for x Axis.

        y (str): Column of the dataframe used as datapoints for y Axis.

        agg (str, optional): The aggregator used to gather data (ex: 'median'
            or 'mean'). Defaults to None.

        dataset_options (dict, optional):
            Options related to the dataset object (i.e. options
            concerning your data). Defaults to {}.

        options (dict, optional): Options to configure the chart. This
            dictionary corresponds to the "options" argument of Chart.js.
            Defaults to None.

        colorscheme (str, optional): Colorscheme to use when drawing the chart.
            Defaults to None.

    Returns:
        [ipychart.Chart]: A chart which display the data using ipychart.
    """
    if dataset_options is None:
        dataset_options = {}

    if y:
        data = _create_chart_data_agg(
            data=data,
            kind="pie",
            x=x,
            y=y,
            agg=agg,
            dataset_options=dataset_options,
        )

    else:
        data = _create_chart_data_count(
            data=data, x=x, dataset_options=dataset_options
        )

    options = _create_chart_options(
        kind="pie", options=options, x=x, y=y, hue=None, agg=agg
    )

    return Chart(
        data=data, kind="pie", options=options, colorscheme=colorscheme
    )


def polarplot(
    data: pd.DataFrame,
    x: str,
    y: str = None,
    agg: str = "mean",
    dataset_options: Union[dict, None] = None,
    options: Union[dict, None] = None,
    colorscheme: Union[str, None] = None,
) -> Chart:
    """
    Plot a polar area chart.

    Polar area charts are similar to pie charts, but each segment has the
    same angle - the radius of the segment differs depending on the value.

    Args:
        data (pd.DataFrame): The dataframe used to draw the chart.

        x (str): Column of the dataframe used as datapoints for x Axis.

        y (str): Column of the dataframe used as datapoints for y Axis.

        agg (str, optional): The aggregator used to gather data (ex: 'median'
            or 'mean'). Defaults to None.

        dataset_options (dict, optional): Options related to the dataset
            object (i.e. options concerning your data). Defaults to {}.

        options (dict, optional): Options to configure the chart. This
            dictionary corresponds to the "options" argument of Chart.js.
            Defaults to None.

        colorscheme (str, optional): Colorscheme to use when drawing the chart.
            Defaults to None.

    Returns:
        [ipychart.Chart]: A chart which display the data using ipychart.
    """
    if dataset_options is None:
        dataset_options = {}

    if y:
        data = _create_chart_data_agg(
            data=data,
            kind="polarArea",
            x=x,
            y=y,
            agg=agg,
            dataset_options=dataset_options,
        )

    else:
        data = _create_chart_data_count(
            data=data, x=x, dataset_options=dataset_options
        )

    options = _create_chart_options(
        kind="polarArea", options=options, x=x, y=y, hue=None, agg=agg
    )

    return Chart(
        data=data, kind="polarArea", options=options, colorscheme=colorscheme
    )


def scatterplot(
    data: pd.DataFrame,
    x: str,
    y: str,
    hue: Union[str, None] = None,
    dataset_options: Union[dict, list, None] = None,
    options: Union[dict, None] = None,
    colorscheme: Union[str, None] = None,
    zoom: bool = True,
) -> Chart:
    """
    Plot a scatter chart.

    Scatter charts are based on basic line charts with the x axis changed
    to a linear axis.

    Args:
        data (pd.DataFrame): The dataframe used to draw the chart.

        x (str): Column of the dataframe used as datapoints for x Axis.

        y (str): Column of the dataframe used as datapoints for y Axis.

        hue (str, optional): Grouping variable that will produce points with
            different colors. Defaults to None.

        dataset_options ([dict, list], optional): Options related to the
            dataset object (i.e. options concerning your data). Defaults to {}.

        options (dict, optional): Options to configure the chart. This
            dictionary corresponds to the "options" argument of Chart.js.
            Defaults to None.

        colorscheme (str, optional): Colorscheme to use when drawing the chart.
            Defaults to None.

        zoom (bool, optional): Allow the user to zoom on the Chart once it is
            created. Defaults to True.

    Returns:
        [ipychart.Chart]: A chart which display the data using ipychart.
    """
    if dataset_options is None:
        dataset_options = {}

    data = _create_chart_data_agg(
        data=data,
        kind="scatter",
        x=x,
        y=y,
        hue=hue,
        dataset_options=dataset_options,
    )

    options = _create_chart_options(
        kind="scatter", options=options, x=x, y=y, hue=hue
    )

    return Chart(
        data=data,
        kind="scatter",
        options=options,
        colorscheme=colorscheme,
        zoom=zoom,
    )


def bubbleplot(
    data: pd.DataFrame,
    x: str,
    y: str,
    r: str,
    hue: Union[str, None] = None,
    dataset_options: Union[dict, list, None] = None,
    options: Union[dict, None] = None,
    colorscheme: Union[str, None] = None,
    zoom: bool = True,
) -> Chart:
    """
    Plot a bubble chart.

    A bubble chart is used to display three-dimension data.

    The location of the bubble is determined by the first two dimensions
    and the corresponding horizontal and vertical axes.

    The third dimension is represented by the radius of the individual
    bubbles.

    Args:
        data (pd.DataFrame): The dataframe used to draw the chart.

        x (str): Column of the dataframe used as datapoints for x Axis.

        y (str): Column of the dataframe used as datapoints for y Axis.

        r (str, optional): Column of the dataframe used as radius for bubbles.

        hue (str, optional): Grouping variable that will produce points with
            different colors. Defaults to None.

        dataset_options ([dict, list], optional): Options related to the
            dataset object (i.e. options concerning your data). Defaults to {}.

        options (dict, optional): Options to configure the chart. This
            dictionary corresponds to the "options" argument of Chart.js.
            Defaults to None.

        colorscheme (str, optional): Colorscheme to use when drawing the chart.
            Defaults to None.

        zoom (bool, optional): Allow the user to zoom on the Chart once it is
            created. Defaults to True.

    Returns:
        [ipychart.Chart]: A chart which display the data using ipychart.
    """
    if dataset_options is None:
        dataset_options = {}

    data = _create_chart_data_agg(
        data=data,
        kind="bubble",
        x=x,
        y=y,
        r=r,
        hue=hue,
        dataset_options=dataset_options,
    )

    options = _create_chart_options(
        kind="bubble", options=options, x=x, y=y, hue=hue
    )

    return Chart(
        data=data,
        kind="bubble",
        options=options,
        colorscheme=colorscheme,
        zoom=zoom,
    )
