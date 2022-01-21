import * as plugin from './index';
import base from '@jupyter-widgets/base';
import {version} from "./version";

export default {
  id: 'ipychart',
  requires: [base.IJupyterWidgetRegistry],
  activate: function(app, widgets) {
      widgets.registerWidget({
          name: 'ipychart',
          version: version,
          exports: plugin
      });
  },
  autoStart: true
};

