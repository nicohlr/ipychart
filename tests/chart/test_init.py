import pytest
from ipychart import Chart


def test_chart_init():
    chart = Chart(data={'datasets': [{'data': [1, 2, 3]}]},
                  kind="bar")
    assert chart.__class__.__name__ == "Chart"


def test_chart_init_with_data():
    chart = Chart(data={'datasets': [{'data': [1, 2, 3]}]}, kind="bar")
    assert chart.kind == "bar"


def test_chart_init_with_data_and_options():
    options = {'title': {'display': True, 'text': 'Bar Chart', 'fontSize': 24}}
    chart = Chart(data={'datasets': [{'data': [1, 2, 3]}]},
                  kind="bar",
                  options=options,
                  colorscheme='tableau.Tableau20')
    assert chart.kind == "bar"


def test_chart_init_with_invalid_data():
    with pytest.raises(ValueError):
        Chart(data={"a": 1, "b": 2}, kind="bar")


def test_chart_init_with_invalid_kind():
    with pytest.raises(ValueError):
        Chart(data={'datasets': [{'data': [1, 2, 3]}]}, kind="foo")


def test_chart_init_with_invalid_options():
    with pytest.raises(ValueError):
        Chart(data={'datasets': [{'data': [1, 2, 3]}]},
              kind="bar",
              options={"a": 1, "b": 2})


def test_chart_init_with_invalid_colorscheme():
    with pytest.raises(ValueError):
        Chart(data={'datasets': [{'data': [1, 2, 3]}]},
              kind="bar",
              colorscheme="foo")


def test_chart_init_with_invalid_zoom():
    with pytest.raises(ValueError):
        Chart(data={'datasets': [{'data': [1, 2, 3]}]},
              kind="bar",
              zoom="foo")
