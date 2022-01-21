import * as base from '@jupyter-widgets/base';
import * as plugin from './chart';
import version from './version';

export default {
    id: 'ipychart',
    requires: [base.IJupyterWidgetRegistry],
    activate(app, widgets) {
        widgets.registerWidget({
            name: 'ipychart',
            version,
            exports: plugin,
        });
    },
    autoStart: true,
};
