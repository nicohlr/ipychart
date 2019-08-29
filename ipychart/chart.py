import ipywidgets as widgets
from traitlets import Unicode, default, Dict


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

        if not options:
            self._options = self._create_default_options(data=data, kind=kind)
        else:
            self._options = options

        self._data = data
        self._type = kind

    @default('layout')
    def _default_layout(self):
        return widgets.Layout(height='auto', align_self='stretch')

    @staticmethod
    def _validate_input(data, kind, options):

        assert kind in ['line', 'bar', 'horizontalBar', 'radar', 'doughnut', 'polarArea',
                        'bubble', 'pie'], 'Type must be one of : line, bar, radar, doughnut, polarArea, bubble, horizontalBar, pie'

        msg_data = 'wrong input format for data argument see https:// for more details'
        msg_options = 'wrong input format for options argument see https:// for more details'

        assert isinstance(data, dict), msg_data
        assert 'datasets' in data, msg_data
        assert len(data['datasets']), msg_data
        assert ['data' in ds for ds in data['datasets']] == [True]*len(data['datasets']), msg_data

        if options:
            assert isinstance(options, dict), msg_options

    @staticmethod
    def _create_default_options(data, kind):

        x_axis_display = True
        y_axis_display = True
        if kind in ['radar', 'doughnut', 'polarArea', 'pie']:
            x_axis_display = False
            y_axis_display = False

        for ds in data['datasets']:
            if 'backgroundColor' not in ds:
                ds['backgroundColor'] = ['rgba(255, 99, 132, 0.2)'] * len(ds['data'])
            if 'borderColor' not in ds:
                ds['borderColor'] = ['rgba(255, 99, 132, 1)'] * len(ds['data'])
            if 'borderWidth' not in ds:
                ds['borderWidth'] = 1

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
