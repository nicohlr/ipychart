from ._version import version_info, __version__

from .example import *
from .chart import *


def _jupyter_nbextension_paths():
    return [{
        'section': 'notebook',
        'src': 'static',
        'dest': 'ipychart',
        'require': 'ipychart/extension'
    }]
