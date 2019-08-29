const widgets = require('@jupyter-widgets/base');
const _ = require('lodash');
const Chart = require('chart.js');

const ChartModel = widgets.DOMWidgetModel.extend({
    defaults: _.extend(widgets.DOMWidgetModel.prototype.defaults(), {
        _model_name : 'BarChartModel',
        _view_name : 'BarChartView',
        _model_module : 'ipychart',
        _view_module : 'ipychart',
        _model_module_version : '^0.1.0',
        _view_module_version : '^0.1.0',
    })
});

const ChartView = widgets.DOMWidgetView.extend({
    render: function() {

        // Get data and type from python
        let data = this.model.get("_data");
        let options = this.model.get("_options");
        let type = this.model.get("_type");

        // Create Chart.js HTML element
        const canvas = document.createElement("canvas");
        const ctx = canvas.getContext('2d');

        // Create chart
        new Chart(ctx, {
            type: type,
            data: data,
            options: options
        });

        // Add element to output
        this.el.appendChild(canvas);
        console.log('end ipychart render');
    }
});

module.exports = {
    ChartModel: ChartModel,
    ChartView: ChartView
};