import ipywidgets as widgets
from traitlets import Unicode, default, List


@widgets.register
class BarChart(widgets.DOMWidget):
    """An example widget."""
    _view_name = Unicode('BarChartView').tag(sync=True)
    _model_name = Unicode('BarChartModel').tag(sync=True)
    _view_module = Unicode('ipychart').tag(sync=True)
    _model_module = Unicode('ipychart').tag(sync=True)
    _view_module_version = Unicode('^0.1.0').tag(sync=True)
    _model_module_version = Unicode('^0.1.0').tag(sync=True)
    _model_data = List([]).tag(sync=True)

    @default('layout')
    def _default_layout(self):
        return widgets.Layout(height='auto', align_self='stretch')

    def set_data(self, js_data):
        self._model_data = js_data
