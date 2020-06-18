import random
import json
import numpy as np
import pandas as pd
import ipywidgets as widgets
from traitlets import Unicode, default, Dict
from ipywidgets.embed import embed_minimal_html, dependency_state, embed_data
from ._version import __version__


class Chart(widgets.DOMWidget):
    """
    A Jupyter - Chart.js bridge enabling interactive data visualization in the Jupyter notebook.

    Official documentation : https://nicohlr.gitlab.io/ipychart/

    Args:
        data (dict): Data to draw. This dictionary corresponds to the "data" argument of Chart.js.
        kind (str): Type of chart. This string corresponds to the "type" argument of Chart.js.
        options (dict, optional): All options to configure the chart. This dictionary corresponds to the "options" argument of Chart.js. Defaults to None.
    """

    _view_name = Unicode('ChartView').tag(sync=True)
    _model_name = Unicode('ChartModel').tag(sync=True)
    _view_module = Unicode('ipychart').tag(sync=True)
    _model_module = Unicode('ipychart').tag(sync=True)
    _view_module_version = Unicode('^' + __version__).tag(sync=True)
    _model_module_version = Unicode('^' + __version__).tag(sync=True)

    _data = Dict().tag(sync=True)
    _options = Dict().tag(sync=True)
    _type = Unicode().tag(sync=True)

    def __init__(self, data: dict, kind: str, options: dict = None, colorscheme: str = None):

        super().__init__()
        self.data = data
        self.kind = kind
        self.options = options if options else {}
        self.colorscheme = colorscheme

        # Check user input
        self._validate_input()

        # Set default style and options
        self._set_default_options()
        if not colorscheme:
            self._set_default_style()

        # Set synced arguments
        self._options = self.options
        self._data = self.data
        self._type = self.kind

    @default('layout')
    def _default_layout(self):
        return widgets.Layout(height='auto', align_self='stretch')

    def _validate_input(self):
        """
        This function checks all arguments passed when the user create an instance of the Chart class.
        To match Chart.js format, arguments must have a very specific structure.
        To see more details about this structure, please check the documentation: https://
        """

        msg_data = 'Wrong input format for data argument. See https:// for more details'  # TODO: link to the doc
        msg_kind = 'Chart kind must be one of : line, bar, radar, doughnut, polarArea, bubble, horizontalBar, pie. See https:// for more details'  # TODO: link to the doc
        msg_options = 'Wrong input format for options argument. See https:// for more details'  # TODO: link to the doc
        msg_colorscheme = 'Wrong input format for colorscheme argument. See https:// for more details'  # TODO: link to the doc

        # Check data argument
        assert 'datasets' in self.data, msg_data
        assert len(self.data['datasets']), msg_data
        assert ['data' in ds for ds in self.data['datasets']] == [True] * len(self.data['datasets']), msg_data
        if 'kind' in ['bubble', 'scatter']:
            for d in self.data['datasets']:
                assert all(isinstance(x, dict) for x in d['data']), msg_data
                assert all(k in p for k in ('x', 'y', 'r') for p in self.data), msg_data
        for d in self.data['datasets']:
            if 'datalabels' in d:
                assert isinstance(d['datalabels'], dict), msg_data

        # Check kind argument
        assert self.kind in ['line', 'bar', 'horizontalBar', 'radar', 'doughnut', 'polarArea', 'bubble', 'pie', 'scatter'], msg_kind

        # Check options argument
        if self.options:
            assert isinstance(self.options, dict), msg_options
            for key in self.options:
                assert key in ['legend', 'title', 'tooltips', 'scales', 'scale', 'layout', 'animation', 'hover'], msg_options

        # Check colorscheme argument
        if self.colorscheme:
            assert isinstance(self.colorscheme, str), msg_colorscheme
            if self.options:
                self.options.update({'plugins': {'colorschemes': {'scheme': self.colorscheme}}})
            else:
                self.options = {'plugins': {'colorschemes': {'scheme': self.colorscheme}}}

        # Pandas series handling
        for d in self.data['datasets']:
            d['data'] = d['data'].tolist() if isinstance(d['data'], pd.Series) else d['data']
        if 'labels' in self.data:
            self.data['labels'] = self.data['labels'].tolist() if isinstance(self.data['labels'], pd.Series) else self.data['labels']

    def _set_default_options(self):
        """
        This function set some default options for the chart.
        To see more details about options in ipychart, please check the documentation: https://  # TODO: link to the doc
        """

        # Display axis by default only for certain types of chart
        x_axis_display, y_axis_display = (True, True)
        if self.kind in ['radar', 'doughnut', 'polarArea', 'pie']:
            x_axis_display, y_axis_display = (False, False)

        # Override default scales options from Chart.js if not setted by the user
        if 'scales' not in self.options and 'scale' not in self.options:
            if self.kind not in ['radar', 'polarArea']:
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

        # Do not display datalabels by default
        for d in self.data['datasets']:
            if 'datalabels' not in d:
                d['datalabels'] = {'display': False}

    def _set_default_style(self):
        """
        This function set a default style for the chart.
        It allows to get a good looking chart with ipychart without having to input some styling options.
        To see more details about styling in ipychart, please check the documentation: https://  # TODO: link to the doc
        """

        random_colors = ['rgba({}, {}, {}, 0.2)'.format(*random.sample(
            list(np.random.choice(range(256), size=2)) + list(
                np.random.choice(range(200, 256), size=1)), 3)) for _ in range(100)]

        # Chart.js main colors for one dataset
        default_colors_one = ['rgba(54, 163, 235, 0.2)', 'rgba(254, 119, 124, 0.2)', 'rgba(255, 206, 87, 0.2)']

        # Chosen colors for the six fist datasets then random colors
        default_colors_all = ['rgba(54, 163, 235, 0.2)', 'rgba(254, 119, 124, 0.2)', 'rgba(255, 206, 87, 0.2)',
                              'rgba(11, 255, 238, 0.2)', 'rgba(153, 102, 255, 0.2)', 'rgba(255, 159, 64, 0.2)',
                              'rgba(5, 169, 69, 0.2)', 'rgba(230, 120, 199, 0.2)', 'rgba(35, 120, 206, 0.2)',
                              'rgba(211, 216, 214, 0.2)'] + random_colors

        # Override default style options from Chart.js if not setted by the user
        if len(self.data['datasets']) == 1:
            if 'backgroundColor' not in self.data['datasets'][0]:
                if self.kind in ['line', 'radar']:
                    self.data['datasets'][0]['backgroundColor'] = default_colors_one[0]
                elif self.kind in ['bar', 'horizontalBar']:
                    self.data['datasets'][0]['backgroundColor'] = default_colors_one * (int(len(self.data['datasets'][0]['data'])) + 1)
                else:
                    self.data['datasets'][0]['backgroundColor'] = default_colors_all[:len(self.data['datasets'][0]['data'])]
            if 'borderColor' not in self.data['datasets'][0]:
                if self.kind in ['line', 'radar']:
                    self.data['datasets'][0]['borderColor'] = self.data['datasets'][0]['backgroundColor'].replace('0.2', '1')
                else:
                    self.data['datasets'][0]['borderColor'] = [c.replace('0.2', '1') for c in self.data['datasets'][0]['backgroundColor']]
            if 'borderWidth' not in self.data['datasets'][0]:
                self.data['datasets'][0]['borderWidth'] = 1
            if 'datalabels' in self.data['datasets'][0]:
                if 'borderWidth' in self.data['datasets'][0]['datalabels']:
                    if 'backgroundColor' not in self.data['datasets'][0]['datalabels']:
                        self.data['datasets'][0]['datalabels']['backgroundColor'] = self.data['datasets'][0]['backgroundColor']
                    if 'borderColor' not in self.data['datasets'][0]['datalabels']:
                        self.data['datasets'][0]['datalabels']['borderColor'] = self.data['datasets'][0]['borderColor']
            if self.kind in ['line', 'radar']:
                if 'pointBackgroundColor' not in self.data['datasets'][0]:
                    self.data['datasets'][0]['pointBackgroundColor'] = self.data['datasets'][0]['backgroundColor']
                if 'pointBorderColor' not in self.data['datasets'][0]:
                    self.data['datasets'][0]['pointBorderColor'] = self.data['datasets'][0]['borderColor']

        else:
            for idx, ds in enumerate(self.data['datasets']):
                if 'backgroundColor' not in ds:
                    if self.kind in ['bar', 'horizontalBar', 'line', 'radar']:
                        ds['backgroundColor'] = default_colors_all[idx]
                    else:
                        ds['backgroundColor'] = default_colors_all[:len(ds['data'])]
                if 'borderColor' not in ds:
                    if self.kind in ['bar', 'horizontalBar', 'line', 'radar']:
                        ds['borderColor'] = ds['backgroundColor'].replace('0.2', '1')
                    else:
                        ds['borderColor'] = [c.replace('0.2', '1') for c in ds['backgroundColor']]
                if 'borderWidth' not in ds:
                    ds['borderWidth'] = 1
                if 'datalabels' in ds:
                    if 'borderWidth' in ds['datalabels']:
                        if 'backgroundColor' not in ds['datalabels']:
                            ds['datalabels']['backgroundColor'] = ds['backgroundColor']
                        if 'borderColor' not in ds['datalabels']:
                            ds['datalabels']['borderColor'] = ds['borderColor']
                if self.kind in ['line', 'radar']:
                    if 'pointBackgroundColor' not in ds:
                        ds['pointBackgroundColor'] = ds['backgroundColor']
                    if 'pointBorderColor' not in ds:
                        ds['pointBorderColor'] = ds['borderColor']

    def to_html(self, path):
        """
        This function embed the chart widget into an HTML file dumped at the inputed path location.
        To see more details about embeding an ipywidget see: https://ipywidgets.readthedocs.io/en/latest/embedding.html
        """

        embed_minimal_html(path, views=[self], state=dependency_state([self]))

    def get_html_template(self):
        """
        This function gives HTML code to embed the chart widget.
        To see more details about embeding an ipywidget see: https://ipywidgets.readthedocs.io/en/latest/embedding.html

        Returns:
            widget_html (str): HTML code to embed the chart.
        """

        html_template = """
                <!-- Load require.js. Delete this if your page already loads require.js -->
                <script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js" integrity="sha256-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=" crossorigin="anonymous"></script>
                <script src="https://unpkg.com/@jupyter-widgets/html-manager@^0.18.0/dist/embed-amd.js" crossorigin="anonymous"></script>

                <script type="application/vnd.jupyter.widget-state+json">
                    {manager_state}
                </script>

                <script type="application/vnd.jupyter.widget-state+json">

                </script>
                <script type="application/vnd.jupyter.widget-view+json">
                    {widget_views[0]}
                </script>
            """

        data = embed_data(views=[self])
        manager_state = json.dumps(data['manager_state'])
        widget_views = [json.dumps(view) for view in data['view_specs']]
        rendered_template = html_template.format(manager_state=manager_state, widget_views=widget_views)

        return rendered_template
