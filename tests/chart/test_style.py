from ipychart import Chart
from pydash import has


def test_colorscheme_overwrite_default_style():
    chart = Chart(data={'datasets': [{'data': [1, 2, 3]}]},
                  kind="bar", colorscheme='tableau.Tableau20')

    assert not has(chart.data["datasets"][0], "backgroundColor")
    assert not has(chart.data["datasets"][0], "borderColor")
    assert not has(chart.data["datasets"][0], "borderWidth")
    assert not has(chart.data["datasets"][0], "pointBackgroundColor")
    assert not has(chart.data["datasets"][0], "pointBorderColor")


def test_default_style_one_bar_dataset():
    chart = Chart(data={'datasets': [{'data': [1, 2, 3]}]},
                  kind="bar")

    assert has(chart.data["datasets"][0], "backgroundColor")
    assert has(chart.data["datasets"][0], "borderColor")
    assert has(chart.data["datasets"][0], "borderWidth")


def test_default_style_one_line_dataset():
    chart = Chart(data={'datasets': [{'data': [1, 2, 3]}]},
                  kind="line")

    assert has(chart.data["datasets"][0], "backgroundColor")
    assert has(chart.data["datasets"][0], "borderColor")
    assert has(chart.data["datasets"][0], "borderWidth")
    assert has(chart.data["datasets"][0], "pointBackgroundColor")
    assert has(chart.data["datasets"][0], "pointBorderColor")


def test_default_style_several_datasets():
    datasets = [{'data': [1, 2, 3]}, {'data': [4, 5, 6]}, {'data': [7, 8, 9]}]
    chart = Chart(data={'datasets': datasets},
                  kind="line")

    for ds in chart.data["datasets"]:
        assert has(ds, "backgroundColor")
        assert has(ds, "borderColor")
        assert has(ds, "borderWidth")
        assert has(ds, "pointBackgroundColor")
        assert has(ds, "pointBorderColor")
