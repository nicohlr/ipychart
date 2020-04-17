import ipywidgets as widgets
from traitlets import Unicode, default, Dict
import numpy as np
import random
import colorsys
import logging
import pandas as pd


class Chart(widgets.DOMWidget):

    """Wrap Chart.js into an ipywidget"""

    _view_name = Unicode('ChartView').tag(sync=True)
    _model_name = Unicode('ChartModel').tag(sync=True)
    _view_module = Unicode('ipychart').tag(sync=True)
    _model_module = Unicode('ipychart').tag(sync=True)
    _view_module_version = Unicode('^0.1.0').tag(sync=True)
    _model_module_version = Unicode('^0.1.0').tag(sync=True)

    _data = Dict().tag(sync=True)
    _options = Dict().tag(sync=True)
    _type = Unicode().tag(sync=True)

    def __init__(self, data, kind, options=None, x=None, y=None):
        super().__init__()

        self._validate_input(data, kind, options)

        self.data = data
        self.kind = kind
        self.options = options
        self.x = x
        self.y = y
    
        if isinstance(data, pd.DataFrame):
            self.data = self._pandas_df_to_dataset(self.data, self.x, self.y)

        self.data = self._add_datasets_default_style(self.data, self.kind)
        self.options = self._create_default_chart_options(self.data, self.options, self.kind)

        self._options = self.options
        self._data = self.data
        self._type = kind


    @default('layout')
    def _default_layout(self):
        return widgets.Layout(height='auto', align_self='stretch')

    @staticmethod
    def _validate_input(data, kind, options):

        assert kind in ['line', 'bar', 'horizontalBar', 'radar', 'doughnut', 'polarArea',
                        'bubble', 'pie'], \
            'Type must be one of : line, bar, radar, doughnut, polarArea, bubble, horizontalBar, pie'

        msg_data = 'Wrong input format for data argument see https:// for more details'  # todo: link to the doc
        msg_options = 'Wrong input format for options argument see https:// for more details'  # todo: link to the doc

        assert isinstance(data, dict) or isinstance(data, pd.DataFrame), msg_data
        if isinstance(data, dict):
            assert 'datasets' in data, msg_data
            assert len(data['datasets']), msg_data
            assert ['data' in ds for ds in data['datasets']] == [True]*len(data['datasets']), msg_data
            if 'kind' == 'bubble':
                for d in data['datasets']:
                    assert all(isinstance(x, dict) for x in d['data']), "Data must contains dict with coordinates (x,y) and radius (r) for charts of type 'bubble'. Example --> data: [{'x': 5, 'y': 10, 'r': 10}, {'x': 15, 'y': 3, 'r': 15}]"
                    assert all(k in p for k in ('x', 'y', 'r') for p in data), "Data must contains dict with coordinates (x,y) and radius (r) for charts of type 'bubble'. Example --> data: [{'x': 5, 'y': 10, 'r': 10}, {'x': 15, 'y': 3, 'r': 15}]"
 

        if options:
            assert isinstance(options, dict), msg_options

    @staticmethod
    def _create_default_chart_options(data, options, kind):

        x_axis_display = True
        y_axis_display = True

        if kind in ['radar', 'doughnut', 'polarArea', 'pie']:
            x_axis_display = False
            y_axis_display = False

        default_options = {}

        if options:
            default_options = options

        # Override default options from Chart.js if option is not setted by the user
        # bug: beginAtzero does not work 
        if kind != 'radar':
            if 'scales' not in default_options:
                default_options.update({'scales': [
                    {'yAxes': [{'display': y_axis_display, 'ticks': {'beginAtZero': True, 'min': 0, 'max': 2000, 'display': y_axis_display}}]},
                    {'xAxes': [{'display': x_axis_display, 'ticks': {'beginAtZero': True, 'min': 0, 'max': 200, 'display': x_axis_display}}]}
                ]})
            if 'beginAtZero' not in default_options:
                default_options.update({'beginAtZero': True})
        else:
            if 'scales' not in default_options:
                default_options.update({'scale': {'ticks': {'beginAtZero': True}}})

        if len(data['datasets']) == 1 and kind in ['bar', 'line', 'horizontalBar', 'bubble', 'radar']:
            if 'legend' not in default_options:
                default_options.update({'legend': False})

        return default_options

    @staticmethod
    def _add_datasets_default_style(data, kind):

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
                'rgba(255, 252, 49, 0.2)'
        ]

        border_colors = [c.replace('0.2', '1') for c in background_colors]

        #todo : handle case of only 1 dataset

        for idx, ds in enumerate(data['datasets']):

            if 'backgroundColor' not in ds:
                if kind in ['radar', 'line']:
                    ds['backgroundColor'] = background_colors[:1]
                elif kind == 'bar':
                    ds['backgroundColor'] = background_colors[idx]
                else:
                    ds['backgroundColor'] = background_colors[:len(ds['data'])]

            if 'borderColor' not in ds:
                if kind in ['radar', 'line']:
                    ds['borderColor'] = border_colors[:1]
                elif kind == 'bar':
                    ds['borderColor'] = border_colors[idx]
                else:
                    ds['borderColor'] = border_colors[:len(ds['data'])]

            if 'pointBorderColor' not in ds and kind in ['radar', 'line']:
                ds['pointBorderColor'] = border_colors[:1] * len(ds['data'])

            if 'pointBackgroundColor' not in ds and kind in ['radar', 'line']:
                ds['pointBackgroundColor'] = background_colors[:1] * len(ds['data'])

            if 'borderWidth' not in ds:
                ds['borderWidth'] = 1

        return data

    @staticmethod
    def _pandas_df_to_dataset(data, x, y):
        # todo: handle the case of multiple columns passed to y and trasform it to multiple datasets
        # convert dataframe into dict dataset
        labels = data[x].tolist()
        data = data[y].tolist()
        dataset = {'labels': labels, 'datasets': [{'data': data}]}

        return dataset