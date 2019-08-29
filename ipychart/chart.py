import ipywidgets as widgets
from traitlets import Unicode, default, List, Dict


class Chart(widgets.DOMWidget):
    """An example widget."""
    _view_name = Unicode('ChartView').tag(sync=True)
    _model_name = Unicode('ChartModel').tag(sync=True)
    _view_module = Unicode('ipychart').tag(sync=True)
    _model_module = Unicode('ipychart').tag(sync=True)
    _view_module_version = Unicode('^0.1.0').tag(sync=True)
    _model_module_version = Unicode('^0.1.0').tag(sync=True)

    _data = Dict().tag(sync=True)
    _options = Dict().tag(sync=True)
    _type = Unicode().tag(sync=True)

    def __init__(self, data, kind, options=None):

        super().__init__()

        assert kind in ['line', 'bar', 'horizontalBar', 'radar', 'doughnut', 'polarArea',
                        'bubble'], 'Type must be one of : line, bar, radar, doughnut, polarArea, bubble'

        assert isinstance(data, dict), 'Please enter data as dict of list'

        assert 'datasets' in data, 'Please input data using the key "datasets" in the data dict'

        if not options:
            self._options = self._create_default_options(kind)
        else:
            self._options = options

        self._data = data
        self._type = kind

    @default('layout')
    def _default_layout(self):
        return widgets.Layout(height='auto', align_self='stretch')

    @staticmethod
    def _create_default_options(kind):

        x_axis_display = True
        y_axis_display = True
        if kind in ['radar', 'doughnut', 'polarArea', 'pie']:
            x_axis_display = False
            y_axis_display = False

        default_options = {
            'legend': {
                'display': True,
                'position': 'top'
            },
            'tooltips': {},  # todo: handle tooltips
            'scales': {
                'xAxes': [{
                    'display': x_axis_display,
                    'ticks': {
                        'display': x_axis_display
                    }
                }],
                'yAxes': [{
                    'display': y_axis_display,
                    'ticks': {
                        'beginAtZero': True,
                        'display': y_axis_display
                    }
                }]
            }
        }

        return default_options
