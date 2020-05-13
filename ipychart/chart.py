import ipywidgets as widgets
from traitlets import Unicode, default, Dict
from ipywidgets.embed import embed_minimal_html, dependency_state
import pandas as pd
from .__meta__ import __version_js__


class Chart(widgets.DOMWidget):

    """A Jupyter - Chart.js bridge enabling interactive data visualization in the Jupyter notebook."""

    _view_name = Unicode('ChartView').tag(sync=True)
    _model_name = Unicode('ChartModel').tag(sync=True)
    _view_module = Unicode('ipychart').tag(sync=True)
    _model_module = Unicode('ipychart').tag(sync=True)
    _view_module_version = Unicode('^' + __version_js__).tag(sync=True)
    _model_module_version = Unicode('^' + __version_js__).tag(sync=True)

    _data = Dict().tag(sync=True)
    _options = Dict().tag(sync=True)
    _type = Unicode().tag(sync=True)

    def __init__(self, data: dict, kind: str, options: dict = None):

        super().__init__()
        self.data = data
        self.kind = kind
        self.options = options if options else {}

        # Check user input
        self._validate_input()

        # Set default style and options
        self._set_default_style()
        self._set_default_options()

        # Set synced arguments
        self._options = self.options
        self._data = self.data
        self._type = self.kind

    @default('layout')
    def _default_layout(self):
        return widgets.Layout(height='auto', align_self='stretch')

    def _validate_input(self):
        '''
        This function checks all arguments passed when the user create an instance of the Chart class.
        To match Chart.js format, arguments must have a very specific structure.
        To see more details about this structure, please check the documentation: https://
        '''

        msg_data = 'Wrong input format for data argument. See https:// for more details'  # todo: link to the doc
        msg_kind = 'Chart kind must be one of : line, bar, radar, doughnut, polarArea, bubble, horizontalBar, pie. See https:// for more details'  # todo: link to the doc
        msg_options = 'Wrong input format for options argument. See https:// for more details'  # todo: link to the doc

        # Check data argument
        assert 'datasets' in self.data, msg_data
        assert len(self.data['datasets']), msg_data
        assert ['data' in ds for ds in self.data['datasets']] == [True] * len(self.data['datasets']), msg_data
        if 'kind' == 'bubble':
            for d in self.data['datasets']:
                assert all(isinstance(x, dict) for x in d['data']), msg_data
                assert all(k in p for k in ('x', 'y', 'r') for p in self.data), msg_data

        # Check kind argument
        assert self.kind in ['line', 'bar', 'horizontalBar', 'radar', 'doughnut', 'polarArea', 'bubble', 'pie'], msg_kind

        # Check options argument
        if self.options:
            assert isinstance(self.options, dict), msg_options
            for key in self.options:
                print(key)
                assert key in ['legend', 'title', 'tooltips', 'scales', 'layout', 'animation', 'responsive', 'hover'], msg_options

        # Pandas series handling
        for d in self.data['datasets']:
            d['data'] = d['data'].tolist() if isinstance(d['data'], pd.Series) else d['data']

        if 'labels' in self.data:
            self.data['labels'] = self.data['labels'].tolist() if isinstance(self.data['labels'], pd.Series) else self.data['labels']

    def _set_default_options(self):
        '''
        This function set some default options for the chart.
        To see more details about options in ipychart, please check the documentation: https://
        '''

        # Display axis by default only for certain types of chart
        x_axis_display, y_axis_display = (True, True)
        if self.kind in ['radar', 'doughnut', 'polarArea', 'pie']:
            x_axis_display, y_axis_display = (False, False)

        # TODO: when fill arg is false in dataset, legend color must be the background color instead of border color (for line chart)

        # Override default scales options from Chart.js if not setted by the user
        if 'scales' not in self.options:
            if self.kind != 'radar':
                self.options.update({'scales': {
                    'yAxes': [{'display': y_axis_display, 'ticks': {'beginAtZero': True, 'display': y_axis_display}}],
                    'xAxes': [{'display': x_axis_display, 'ticks': {'beginAtZero': True, 'display': x_axis_display}}]
                }})
            else:
                self.options.update({'scale': {'ticks': {'beginAtZero': True}}})

        # Override default legend options from Chart.js if not setted by the user
        if 'legend' not in self.options:
            if len(self.data['datasets']) == 1 and self.kind in ['bar', 'line', 'horizontalBar', 'bubble', 'radar']:
                self.options.update({'legend': False})

    def _set_default_style(self):
        '''
        This function set some syle for the chart.
        It allows to get a good looking chart with ipychart without having to input some styling options.
        To see more details about styling in ipychart, please check the documentation: https://
        '''

        default_background_colors = [
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

        # Override default style options from Chart.js if not setted by the user
        for idx, ds in enumerate(self.data['datasets']):

            if 'backgroundColor' not in ds:
                if self.kind in ['bar', 'horizontalBar', 'line', 'radar']:
                    ds['backgroundColor'] = default_background_colors[idx]
                else:
                    ds['backgroundColor'] = default_background_colors[:len(ds['data'])]

            if 'borderColor' not in ds:
                if isinstance(ds['backgroundColor'], str):
                    ds['borderColor'] = ds['backgroundColor'].replace('0.2', '1')
                else:
                    ds['borderColor'] = [c.replace('0.2', '1') for c in ds['backgroundColor']]

            if 'borderWidth' not in ds:
                ds['borderWidth'] = 1

    def to_html(self, path):
        '''
        This function set embed the chart widget into an HTML file dumped at the inputed path location.
        To see more details about embeding an ipywidget see: https://ipywidgets.readthedocs.io/en/latest/embedding.html
        '''
        embed_minimal_html(path, views=[self], state=dependency_state([self]))
