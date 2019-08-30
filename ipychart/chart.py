import ipywidgets as widgets
from traitlets import Unicode, default, Dict
import numpy as np
import random
import colorsys


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

        self._options = self._create_default_chart_options(options, kind)
        self._data = self._add_datasets_default_style(data, kind)
        self._type = kind

        print(self._options)

    @default('layout')
    def _default_layout(self):
        return widgets.Layout(height='auto', align_self='stretch')

    @staticmethod
    def _validate_input(data, kind, options):

        assert kind in ['line', 'bar', 'horizontalBar', 'radar', 'doughnut', 'polarArea',
                        'bubble', 'pie'], \
            'Type must be one of : line, bar, radar, doughnut, polarArea, bubble, horizontalBar, pie'

        msg_data = 'wrong input format for data argument see https:// for more details'  # todo: link to the doc
        msg_options = 'wrong input format for options argument see https:// for more details'  # todo: link to the doc

        assert isinstance(data, dict), msg_data
        assert 'datasets' in data, msg_data
        assert len(data['datasets']), msg_data
        assert ['data' in ds for ds in data['datasets']] == [True]*len(data['datasets']), msg_data

        if options:
            assert isinstance(options, dict), msg_options

    @staticmethod
    def _create_default_chart_options(options, kind):

        x_axis_display = True
        y_axis_display = True
        if kind in ['radar', 'doughnut', 'polarArea', 'pie']:
            x_axis_display = False
            y_axis_display = False

        default_options = {}

        if options:
            default_options = options

        #  Override default options from Chart.js
        if kind != 'radar':
            default_options.update({'scales': [
                {'yAxes': [{'display': y_axis_display, 'ticks': {'beginAtZero': True, 'min': 0, 'max': 2000, 'display': y_axis_display}}]},
                {'xAxes': [{'display': x_axis_display, 'ticks': {'beginAtZero': True, 'min': 0, 'max': 200, 'display': x_axis_display}}]}
            ]})
            default_options.update({'beginAtZero': True})
        else:
            default_options.update({'scale': {'ticks': {'beginAtZero': True}}})

        return default_options

    @staticmethod
    def _add_datasets_default_style(data, kind):

        # todo: handle the case of more than 1 dataset separately

        background_colors = [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(74, 242, 242, 0.2)',
                'rgba(137, 252, 0, 0.2)',
                'rgba(255, 138, 222, 0.2)',
                'rgba(255,252,49, 0.2)'
        ]

        border_colors = [c.replace('0.2', '1') for c in background_colors]

        for idx, ds in enumerate(data['datasets']):

            if 'backgroundColor' not in ds:
                if kind in ['radar', 'line']:
                    ds['backgroundColor'] = background_colors[:1]
                else:
                    ds['backgroundColor'] = background_colors[:len(ds['data'])]

            if 'borderColor' not in ds:
                if kind in ['radar', 'line']:
                    ds['borderColor'] = border_colors[:1]
                else:
                    ds['borderColor'] = border_colors[:len(ds['data'])]

            if 'pointBorderColor' not in ds and kind in ['radar', 'line']:
                ds['pointBorderColor'] = border_colors[:1] * len(ds['data'])

            if 'pointBackgroundColor' not in ds and kind in ['radar', 'line']:
                ds['pointBackgroundColor'] = background_colors[:1] * len(ds['data'])

            if 'borderWidth' not in ds:
                ds['borderWidth'] = 1

        return data
