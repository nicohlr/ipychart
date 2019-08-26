import ipywidgets as widgets
from traitlets import Unicode, default, List


class Chart(widgets.DOMWidget):
    """An example widget."""
    _view_name = Unicode('ChartView').tag(sync=True)
    _model_name = Unicode('ChartModel').tag(sync=True)
    _view_module = Unicode('ipychart').tag(sync=True)
    _model_module = Unicode('ipychart').tag(sync=True)
    _view_module_version = Unicode('^0.1.0').tag(sync=True)
    _model_module_version = Unicode('^0.1.0').tag(sync=True)
    _model_data = List([]).tag(sync=True)
    _type = Unicode().tag(sync=True)

    def __init__(self, data, kind):
        super().__init__()
        assert kind in ['line', 'bar', 'radar', 'doughnut', 'polarArea',
                        'bubble'], 'Type must be one of : line, bar, radar, doughnut, polarArea, bubble'
        assert isinstance(data, (list, dict)), 'Please enter data as dict of list'

        self._model_data = data
        self._type = kind

    @default('layout')
    def _default_layout(self):
        return widgets.Layout(height='auto', align_self='stretch')
