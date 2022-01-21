import pytest
from ipychart import Chart


def test_type_setter():
    chart = Chart(data={'datasets': [{'data': [1, 2, 3]}]},
                  kind="bar")
    chart.kind = "line"
    assert chart.kind == "line"


def test_kind_setter_with_invalid_value():
    chart = Chart(data={'datasets': [{'data': [1, 2, 3]}]},
                  kind="bar")
    with pytest.raises(ValueError):
        chart.kind = "foo"


def test_data_setter_with_invalid_value():
    chart = Chart(data={'datasets': [{'data': [1, 2, 3]}]},
                  kind="bar")
    with pytest.raises(ValueError):
        chart.data = {"a": 1, "b": 2}
