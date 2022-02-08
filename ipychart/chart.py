import random
import json

import numpy as np
import ipywidgets as widgets

from pydash import has, set_, merge
from traitlets import Unicode, default, Dict, Bool
from ipywidgets.embed import embed_minimal_html, dependency_state, embed_data

from ._version import __version__

from .values import KINDS, COLORSCHEMES

MSG_FORMAT = (
    'Wrong input format for {} argument. See '
    'https://nicohlr.github.io/ipychart/user_guide/usage.html '
    'for more details'
)

MSG_KIND = (
    'Chart kind must be one of : line, bar, radar, doughnut,'
    'polarArea, bubble, pie, scatter. See '
    'https://nicohlr.github.io/ipychart/user_guide/charts.html '
    'for more details'
)

MSG_COLORSCHEME = (
    'Chart colorscheme must be one of the exposed colorschemes. See '
    'https://nagix.github.io/chartjs-plugin-colorschemes/colorchart.html '
    'for the list of available colorschemes.'
)


@widgets.register
class Chart(widgets.DOMWidget):
    """
    A Jupyter - Chart.js bridge enabling interactive data visualization in
    the Jupyter notebook.

    Official documentation : https://nicohlr.github.io/ipychart/

    Args:
        data (dict): Data to draw. This dictionary corresponds to the "data"
            argument of Chart.js.

        kind (str): Type of chart. This string corresponds to the "type"
            argument of Chart.js.

        options (dict, optional): All options to configure the chart. This
            dictionary corresponds to the "options" argument of Chart.js.
            Defaults to None.

        colorscheme (str, optional): Choose a predefined color scheme to your
            chart. Defaults to None. A list of all possible colorschemes can be
            found at:
            https://nagix.github.io/chartjs-plugin-colorschemes/colorchart.html.

        zoom (bool, optional): Allow the user to zoom on the Chart once it is
            created. Disabled for Doughnut, Pie, PolarArea and Radar Charts.
            Defaults to True.
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
                 options: dict | None = None,
                 colorscheme: str | None = None,
                 zoom: bool = True):

        super().__init__()

        self._data = data
        self._kind = kind
        self._options = options if options else {}
        self._colorscheme = colorscheme
        self._zoom = zoom

        # Check inputs and sync to JS
        self._refresh_chart()

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self._refresh_chart()

    @property
    def kind(self):
        return self._kind

    @kind.setter
    def kind(self, value):
        self._kind = value
        self._refresh_chart()

    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, value):
        self._options = value
        self._refresh_chart()

    @property
    def colorscheme(self):
        return self._colorscheme

    @colorscheme.setter
    def colorscheme(self, value):
        self._colorscheme = value
        self._refresh_chart()

    @property
    def zoom(self):
        return self._zoom

    @zoom.setter
    def zoom(self, value):
        self._zoom = value
        self._refresh_chart()

    @default('layout')
    def _default_layout(self):
        return widgets.Layout(height='auto', align_self='stretch')

    def _refresh_chart(self):
        """
        This function is called when the user modifies the chart's inputs. It
        checks inputted values, set some default options and style, and sync
        the chart with the Javascript part.
        """

        self._validate_current_arguments()
        self._set_default_inputs()
        self._set_synced_attributes()

    def _validate_current_arguments(self):
        """
        This function checks all current arguments of the chart and raises
        errors if they are not valid. To match Chart.js format, arguments must
        follow a specific structure. To see more details about this structure,
        please check the documentation:
        https://nicohlr.github.io/ipychart/user_guide/usage.html
        """

        # Validate data argument
        if 'datasets' not in self._data:
            raise ValueError(MSG_FORMAT.format('data'))

        datasets = self._data['datasets']
        if not isinstance(datasets, list):
            raise ValueError(MSG_FORMAT.format('data'))
        if not len(datasets):
            raise ValueError(MSG_FORMAT.format('data'))
        if not ['data' in ds for ds in datasets] == [True] * len(datasets):
            raise ValueError(MSG_FORMAT.format('data'))

        for dataset in datasets:

            if 'kind' in ['bubble', 'scatter']:
                if not all(isinstance(x, dict) for x in dataset['data']):
                    raise ValueError(MSG_FORMAT.format("data['datasets']"))
                if not all(k in p for k in ('x', 'y', 'r') for p in self._data):
                    raise ValueError(MSG_FORMAT.format('data'))

            if 'datalabels' in dataset:
                if not isinstance(dataset['datalabels'], dict):
                    raise ValueError(MSG_FORMAT.format('data'))

        if 'labels' in self._data:
            if not isinstance(self._data['labels'], list):
                raise ValueError(MSG_FORMAT.format('data'))

        # Validate kind argument
        if self._kind not in KINDS:
            raise ValueError(MSG_KIND)

        # Validate options argument
        if not isinstance(self._options, dict):
            raise ValueError(MSG_FORMAT.format('options'))

        # TODO: Adapt
        all_options = ['legend', 'title', 'scales',
                       'layout', 'animation', 'hover', 'plugins',
                       'legendCallback', 'indexAxis', 'aspectRatio']

        if not set(self._options.keys()).issubset(set(all_options)):
            raise ValueError(MSG_FORMAT.format('options'))

        # Validate colorscheme argument
        if (self._colorscheme is not None
                and self._colorscheme not in COLORSCHEMES):
            raise ValueError(MSG_COLORSCHEME)

        # Validate zoom argument
        if not isinstance(self._zoom, bool):
            raise ValueError(MSG_FORMAT.format('zoom'))

    def _set_synced_attributes(self):
        """
        This function sync the attributes of the chart with the Javascript
        variables used to draw the chart.
        """

        self._options_sync = self._options
        self._data_sync = self._data
        self._kind_sync = self._kind
        self._colorscheme_sync = self._colorscheme
        self._zoom_sync = self._zoom

    def _set_default_inputs(self):
        """
        This function set some default inputs for the chart. To see more
        details about options in ipychart, please check the official
        documentation:
        https://nicohlr.github.io/ipychart/user_guide/configuration.html
        """

        # Disable cartesian axis by default for some charts
        radials = ['radar', 'doughnut', 'polarArea', 'pie']
        default_options = {}

        # Disable legend by default for some charts
        no_legend = ['bar', 'line', 'bubble', 'radar', 'scatter']
        if (len(self._data['datasets']) == 1) and (self._kind in no_legend):
            default_options = set_(default_options, 'plugins.legend', False)

        self._options = merge(default_options, self._options)

        # Disable zoom by default for some charts
        self._zoom = False if self._kind in radials else self._zoom

        # Set default style is colorscheme is not provided
        cs_plugin_key = 'plugins.colorschemes.scheme'
        if not self._colorscheme and not has(self._options, cs_plugin_key):
            self._set_default_style()

    def _set_default_style(self):
        """
        This function set a default style for the chart. It allows to get a
        good looking chart with ipychart without having to input some styling
        options. To see more details about styling in ipychart, please check
        the official documentation:
        https://nicohlr.github.io/ipychart/user_guide/charts.html
        """

        random_colors = [
            'rgba({}, {}, {}, 0.2)'.format(*random.sample(
                list(np.random.choice(range(256), size=2)) +
                list(np.random.choice(range(200, 256), size=1)), 3))
            for _ in range(100)
        ]

        # Chart.js main colors for one dataset
        colors_unique = [
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
        bars = ['bar']
        lrsb = ['line', 'radar', 'scatter', 'bubble']

        # Set a mix of color if only one dataset
        if len(self._data['datasets']) == 1:

            ds = self._data['datasets'][0]
            ds_type = ds['type'] if 'type' in ds else self._kind

            if bgc not in ds:

                if ds_type in lrsb:
                    ds[bgc] = colors_unique[0]
                elif ds_type in bars:
                    size = int(len(ds['data']))
                    colors = colors_unique * (size + 1)
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

    def to_html(self, path):
        """
        This function embed the chart widget into an HTML file dumped at the
        inputted path location. To see more details about embeding an ipywidget
        see: https://ipywidgets.readthedocs.io/en/latest/embedding.html
        """

        embed_minimal_html(path, views=[self], state=dependency_state([self]))

    def get_html_template(self) -> str:
        """
        This function gives HTML code to embed the chart widget. To see more
        details about embeding an ipywidget see:
        https://ipywidgets.readthedocs.io/en/latest/embedding.html

        Returns:
            [str]: HTML code to embed the chart.
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

        Returns:
            [str]: Python code as a string.
        """

        python_template = (
            f'data = {self._data}\n\n'
            f'options = {self._options}\n\n'
            f"mychart = Chart(data=data, kind='{self._kind}', options=options"
        )

        if self._colorscheme:
            python_template += f", colorscheme='{self._colorscheme}'"

        python_template += ')'

        return python_template
