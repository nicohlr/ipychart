var plugin = require('./index');
var base = require('@jupyter-widgets/base');

module.exports = {
  id: 'ipychart',
  requires: [base.IJupyterWidgetRegistry],
  activate: function(app, widgets) {
      widgets.registerWidget({
          name: 'ipychart',
          version: plugin.version,
          exports: plugin
      });
  },
  autoStart: true
};

