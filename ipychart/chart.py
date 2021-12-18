import random
import json
import copy

import numpy as np
import pandas as pd
import ipywidgets as widgets

from pydash import has, set_, merge
from traitlets import Unicode, default, Dict, Bool
from ipywidgets.embed import embed_minimal_html, dependency_state, embed_data

from ._version import __version__


@widgets.register
class Chart(widgets.DOMWidget):
    """
    A Jupyter - Chart.js bridge enabling interactive data visualization in
    the Jupyter notebook.

    Official documentation : https://nicohlr.gitlab.io/ipychart/

    Args:
        data (dict): Data to draw. This dictionary corresponds to the "data"
                     argument of Chart.js.

        kind (str): Type of chart. This string corresponds to the "type"
                    argument of Chart.js.

        options (dict, optional): All options to configure the chart. This
                                  dictionary corresponds to the "options"
                                  argument of Chart.js. Defaults to None.

        colorscheme (str, optional): Choose a predefined color scheme to your
                                     chart. Defaults to None.
                                     A list of all possible colorschemes can
                                     be found at:
            https://nagix.github.io/chartjs-plugin-colorschemes/colorchart.html.

        zoom (bool, optional): Allow the user to zoom on the Chart once it is
                               created. Disabled for Doughnut, Pie, PolarArea
                               and Radar Charts. Defaults to True.
    """

    _view_name = Unicode('ChartView').tag(sync=True)
    _model_name = Unicode('ChartModel').tag(sync=True)
    _view_module = Unicode('ipychart').tag(sync=True)
    _model_module = Unicode('ipychart').tag(sync=True)
    _view_module_version = Unicode('^' + __version__).tag(sync=True)
    _model_module_version = Unicode('^' + __version__).tag(sync=True)

    _data_sync = Dict().tag(sync=True)
    _options_sync = Dict().tag(sync=True)
    _kind_sync = Unicode().tag(sync=True)
    _colorscheme_sync = Unicode(allow_none=True).tag(sync=True)
    _zoom_sync = Bool().tag(sync=True)

    def __init__(self,
                 data: dict,
                 kind: str,
                 options: dict = None,
                 colorscheme: str = None,
                 zoom: bool = True):

        super().__init__()

        self._data_in = data
        self._kind_in = kind
        self._options_in = options if options else {}
        self._colorscheme_in = colorscheme
        self._zoom_in = zoom

        self._data = None
        self._kind = None
        self._options = None
        self._colorscheme = None
        self._zoom = None

        # Set default values in inputs
        self._set_default_inputs()

        # Set synced attributes for JS
        self._set_synced_attributes()

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_value):
        self._data_in = new_value
        self._set_default_inputs()
        self._set_synced_attributes()

    @property
    def kind(self):
        return self._kind

    @kind.setter
    def kind(self, new_value):
        self._kind_in = new_value
        self._set_default_inputs()
        self._set_synced_attributes()

    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, new_value):
        self._options_in = new_value
        self._set_default_inputs()
        self._set_synced_attributes()

    @property
    def colorscheme(self):
        return self._colorscheme

    @colorscheme.setter
    def colorscheme(self, new_value):
        self._colorscheme_in = new_value
        self._set_default_inputs()
        self._set_synced_attributes()

    @property
    def zoom(self):
        return self._zoom

    @zoom.setter
    def zoom(self, new_value):
        self._zoom_in = new_value
        self._set_default_inputs()
        self._set_synced_attributes()

    @default('layout')
    def _default_layout(self):
        return widgets.Layout(height='auto', align_self='stretch')

    def _set_synced_attributes(self):
        self._options_sync = self._options
        self._data_sync = self._data
        self._kind_sync = self._kind
        self._colorscheme_sync = self._colorscheme
        self._zoom_sync = self._zoom

    def _validate_inputs(self):
        """
        This function checks all arguments passed when the user create an
        instance of the Chart class.

        To match Chart.js format, arguments must have a specific structure.

        To see more details about this structure, please check the
        documentation: https://nicohlr.gitlab.io/ipychart/user_guide/usage.html
        """

        msg_format = (
            'Wrong input format for {} argument. See '
            'https://nicohlr.gitlab.io/ipychart/user_guide/usage.html '
            'for more details')

        msg_kind = (
            'Chart kind must be one of : line, bar, radar, doughnut,'
            'polarArea, bubble, horizontalBar, pie, scatter. See '
            'https://nicohlr.gitlab.io/ipychart/user_guide/charts.html '
            'for more details'
        )

        # Copy input data to avoid modifying it
        self._data = copy.deepcopy(self._data_in)
        self._options = copy.deepcopy(self._options_in)
        self._kind = self._kind_in
        self._colorscheme = self._colorscheme_in
        self._zoom = self._zoom_in

        datasets = self._data['datasets']

        # Check data argument
        assert 'datasets' in self._data, msg_format.format('data')
        assert len(datasets), msg_format.format('data')
        assert ['data' in ds for ds in datasets] == [True] * len(datasets), (
            msg_format.format('data'))

        if 'kind' in ['bubble', 'scatter']:

            for dataset in datasets:
                assert all(isinstance(x, dict) for x in dataset['data']), (
                    msg_format.format("data['datasets']"))
                assert all(k in p for k in ('x', 'y', 'r') for p in self._data
                           ), msg_format.format('data')

        for dataset in datasets:

            dataset['data'] = (
                dataset['data'].tolist() if isinstance(
                    dataset['data'], pd.Series)
                else dataset['data']
            )

            if 'datalabels' in dataset:
                assert isinstance(dataset['datalabels'], dict), (
                    msg_format.format('data'))

        if 'labels' in self._data:

            self._data['labels'] = (
                self._data['labels'].tolist()
                if isinstance(self._data['labels'], pd.Series)
                else self._data['labels']
            )

        # Check kind argument
        kinds = ['line', 'bar', 'horizontalBar', 'radar', 'doughnut',
                 'polarArea', 'bubble', 'pie', 'scatter']
        assert self._kind in kinds, msg_kind

        # Check options argument
        if self._options:

            assert isinstance(self._options, dict), msg_format.format('options')

            all_options = ['legend', 'title', 'tooltips', 'scales', 'scale',
                           'layout', 'animation', 'hover', 'plugins',
                           'legendCallback']

            assert set(self._options.keys()).issubset(set(all_options)), (
                msg_format.format('options'))

        # Check colorscheme argument
        if self._colorscheme:
            assert isinstance(self._colorscheme, str), (
                msg_format.format('colorscheme'))

        # Check zoom argument
        assert isinstance(self._zoom, bool), msg_format.format('zoom')
        # Disable zoom for radial charts
        radials = ['radar', 'doughnut', 'polarArea', 'pie']
        self._zoom = False if self._kind in radials else self._zoom

    def _set_default_options(self):
        """
        This function set some default options for the chart.
        To see more details about options in ipychart, please
        check the official documentation:
        https://nicohlr.gitlab.io/ipychart/user_guide/configuration.html
        """

        # Disable cartesian axis by default for some charts
        no_axis = ['radar', 'doughnut', 'polarArea', 'pie']

        show_xaxis, show_yaxis = (
            (False,) * 2 if self._kind in no_axis else (True,) * 2
        )

        if self._kind not in ['radar', 'polarArea']:
            default_options = {'scales': {
                'yAxes': [{'display': show_yaxis, 'ticks': {
                    'beginAtZero': True, 'display': show_yaxis}}],
                'xAxes': [{'display': show_xaxis, 'ticks': {
                    'beginAtZero': True, 'display': show_xaxis}}]}
            }
        else:
            default_options = {'scale': {'ticks': {'beginAtZero': True}}}

        # Disable legend by default for some charts
        no_legend = [
            'bar', 'line', 'horizontalBar', 'bubble', 'radar', 'scatter']

        if (len(self._data['datasets']) == 1) and (self._kind in no_legend):
            default_options = set_(default_options, 'legend', False)

        self._options = merge(default_options, self._options)

    def _set_default_style(self):
        """
        This function set a default style for the chart. It allows to get a
        good looking chart with ipychart without having to input some styling
        options. To see more details about styling in ipychart, please check
        the official documentation:
        https://nicohlr.gitlab.io/ipychart/user_guide/charts.html
        """

        random_colors = [
            'rgba({}, {}, {}, 0.2)'.format(*random.sample(
                list(np.random.choice(range(256), size=2)) +
                list(np.random.choice(range(200, 256), size=1)), 3))
            for _ in range(100)
        ]

        # Chart.js main colors for one dataset
        colors_one = [
            'rgba(54, 163, 235, 0.2)',
            'rgba(254, 119, 124, 0.2)',
            'rgba(255, 206, 87, 0.2)'
        ]

        # Chosen colors for the ten fist datasets then random colors
        colors_all = [
            'rgba(54, 163, 235, 0.2)',
            'rgba(254, 119, 124, 0.2)',
            'rgba(255, 206, 87, 0.2)',
            'rgba(11, 255, 238, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(255, 159, 64, 0.2)',
            'rgba(5, 169, 69, 0.2)',
            'rgba(230, 120, 199, 0.2)',
            'rgba(35, 120, 206, 0.2)',
            'rgba(211, 216, 214, 0.2)'
        ] + random_colors

        # Accessors for readability
        bgc = 'backgroundColor'
        bdc = 'borderColor'
        bdw = 'borderWidth'
        pbgc = 'pointBackgroundColor'
        pbdc = 'pointBorderColor'

        # Chart types lists
        bars = ['bar', 'horizontalBar']
        lrsb = ['line', 'radar', 'scatter', 'bubble']

        # Set a mix of color if only one dataset
        if len(self._data['datasets']) == 1:

            ds = self._data['datasets'][0]
            ds_type = ds['type'] if 'type' in ds else self._kind

            if bgc not in ds:

                if ds_type in lrsb:
                    ds[bgc] = colors_one[0]
                elif ds_type in ['bar', 'horizontalBar']:
                    size = int(len(ds['data']))
                    colors = colors_one * (size + 1)
                    ds[bgc] = colors[:size]
                else:
                    ds[bgc] = colors_all[:len(ds['data'])]

            if bdc not in ds:
                if ds_type in lrsb:
                    ds[bdc] = ds[bgc].replace('0.2', '1')
                else:
                    ds[bdc] = [c.replace('0.2', '1') for c in ds[bgc]]

            if bdw not in ds:
                ds[bdw] = 1

            if ds_type in lrsb:
                if pbgc not in ds:
                    ds[pbgc] = ds[bgc]
                if pbdc not in ds:
                    ds[pbdc] = ds[bdc]

        # Set one color per dataset if more than one dataset
        else:

            for idx, ds in enumerate(self._data['datasets']):

                ds_type = ds['type'] if 'type' in ds else self._kind

                if bgc not in ds:
                    if ds_type in lrsb + bars:
                        ds[bgc] = colors_all[idx]
                    else:
                        ds[bgc] = colors_all[:len(ds['data'])]

                if bdc not in ds:
                    if ds_type in lrsb + bars:
                        ds[bdc] = ds[bgc].replace('0.2', '1')
                    else:
                        ds[bdc] = [c.replace('0.2', '1') for c in ds[bgc]]

                if bdw not in ds:
                    ds[bdw] = 1

                if ds_type in lrsb:
                    if pbgc not in ds:
                        ds[pbgc] = ds[bgc]
                    if pbdc not in ds:
                        ds[pbdc] = ds[bdc]

    def _set_default_inputs(self):
        self._validate_inputs()
        self._set_default_options()
        if (not self._colorscheme
                and not has(self._options, 'plugins.colorschemes.scheme')):
            self._set_default_style()

    def to_html(self, path):
        """
        This function embed the chart widget into an HTML file dumped at the
        inputted path location. To see more details about embeding an ipywidget
        see: https://ipywidgets.readthedocs.io/en/latest/embedding.html
        """

        embed_minimal_html(path, views=[self], state=dependency_state([self]))

    def get_html_template(self) -> str:
        """
        This function gives HTML code to embed the chart widget.
        To see more details about embeding an ipywidget see:
        https://ipywidgets.readthedocs.io/en/latest/embedding.html

        Returns:
            widget_html (str): HTML code to embed the chart.
        """

        html_template = (
            """<script src="https://cdnjs.cloudflare.com/ajax/libs/require."""
            """js/2.3.4/require.min.js" integrity="sha256-Ae2Vz/4ePdIu6ZyI/5"""
            """ZGsYnb+m0JlOmKPjt6XZ9JJkA=" crossorigin="anonymous">"""
            """</script>\n"""
            """<script src="https://unpkg.com/@jupyter-widgets/html-manager@"""
            """^0.18.0/dist/embed-amd.js" crossorigin="anonymous">"""
            """</script>\n\n"""
            """<script type="application/vnd.jupyter.widget-state+json">\n"""
            "{manager_state}\n"
            """</script>\n\n"""
            """<script type="application/vnd.jupyter.widget-state+json">"""
            """</script>\n\n"""
            """<script type="application/vnd.jupyter.widget-view+json">\n"""
            "{widget_views[0]}\n"
            """</script>"""
        )

        data = embed_data(views=[self])
        manager_state = json.dumps(data['manager_state'])
        widget_views = [json.dumps(view) for view in data['view_specs']]
        rendered_template = html_template.format(manager_state=manager_state,
                                                 widget_views=widget_views)

        return rendered_template

    def get_python_template(self) -> str:
        """
        This function returns the python code to run in order to reproduce
        exactly the same chart.
        """

        python_template = (
            f'data = {self._data}\n\n'
            f'options = {self._options}\n\n'
            f"mychart = Chart(data=data, kind='{self._kind}', options=options,"
        )

        end_template = (
            f" colorscheme='{self._colorscheme}')" if self._colorscheme else ')'
        )

        python_template += end_template

        return python_template
