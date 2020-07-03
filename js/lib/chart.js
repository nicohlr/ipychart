const widgets = require('@jupyter-widgets/base');
const Chart = require('chart.js');
const ChartDataLabels = require('chartjs-plugin-datalabels');
const ChartColorSchemes = require('chartjs-plugin-colorschemes');
var version = require('../package.json')['version'];
var _ = require('lodash');


const ChartModel = widgets.DOMWidgetModel.extend({
    defaults: _.extend(widgets.DOMWidgetModel.prototype.defaults(), {
        _model_name : 'ChartModel',
        _view_name : 'ChartView',
        _model_module : 'ipychart',
        _view_module : 'ipychart',
        _model_module_version : '^' + version,
        _view_module_version : '^' + version,
    })
});


const ChartView = widgets.DOMWidgetView.extend({

    render: function() {

        // Get data and type from python
        let data = this.model.get("_data");
        let options = this.model.get("_options");
        let type = this.model.get("_type");

        // All paths of options dict with callback functions
        let callbacks_options_paths = [
            ['tooltips', 'custom'],
            ['tooltips', 'itemSort'],
            ['tooltips', 'filter'],
            ['tooltips', 'callbacks', 'beforeTitle'],
            ['tooltips', 'callbacks', 'title'],
            ['tooltips', 'callbacks', 'afterTitle'],
            ['tooltips', 'callbacks', 'beforeBody'],
            ['tooltips', 'callbacks', 'beforeLabel'],
            ['tooltips', 'callbacks', 'label'],
            ['tooltips', 'callbacks', 'labelColor'],
            ['tooltips', 'callbacks', 'labelTextColor'],
            ['tooltips', 'callbacks', 'afterLabel'],
            ['tooltips', 'callbacks', 'afterBody'],
            ['tooltips', 'callbacks', 'beforeFooter'],
            ['tooltips', 'callbacks', 'footer'],
            ['tooltips', 'callbacks', 'afterFooter'],
            ['legendCallback'],
            ['legend', 'onClick'],
            ['legend', 'onHover'],
            ['legend', 'onLeave'],
            ['legend', 'labels', 'generateLabels'],
            ['legend', 'labels', 'filter'],
            ['animation', 'onProgress'],
            ['animation', 'onComplete '],
            ['scale', 'pointLabels', 'callback'],
            ['scale', 'ticks', 'callback'],
            ['scale', 'ticks', 'minor', 'callback'],
            ['scale', 'ticks', 'major', 'callback']
        ]
        
        // These paths must be handled for all axes
        let callbacks_scales_paths = [
            ['ticks', 'callback'],
            ['ticks', 'minor', 'callback'],
            ['ticks', 'major', 'callback'],
            ['beforeUpdate'],
            ['beforeSetDimensions'],
            ['afterSetDimensions'],
            ['beforeDataLimits'],
            ['afterDataLimits'],
            ['beforeBuildTicks'],
            ['afterBuildTicks'],
            ['beforeTickToLabelConversion'],
            ['afterTickToLabelConversion'],
            ['beforeCalculateTickRotation'],
            ['afterCalculateTickRotation'],
            ['beforeFit'],
            ['afterFit'],
            ['afterUpdate']
        ]
        
        // Convert strings containing callback functions to real JS functions
        _.forEach(callbacks_options_paths, function(callback, i) { 
            if (_.has(options, callback)) {
                _.set(options, callback, new Function('return ' + _.get(options, callback))());
            }
        });
        
        // Convert strings containing callback functions to real JS functions for each axes
        if (_.has(options, ['scales', 'xAxes'])) {
            _.forEach(options.scales.xAxes, function(axis, i) {
                _.forEach(callbacks_scales_paths, function(callback, j) {
                    if (_.has(options.scales.xAxes[i], callback)) {
                        _.set(options.scales.xAxes[i], callback, new Function('return ' + _.get(options.scales.xAxes[i], callback))());
                    }
                });
            });
        }

        if (_.has(options, ['scales', 'yAxes'])) {
            _.forEach(options.scales.yAxes, function(axis, i) {
                _.forEach(callbacks_scales_paths, function(callback, j) {
                    if (_.has(options.scales.yAxes[i], callback)) {
                        _.set(options.scales.yAxes[i], callback, new Function('return ' + _.get(options.scales.yAxes[i], callback))());
                    }
                });
            });
        }

        console.log('Chart options:', options)
        
        // Create Chart.js HTML element
        const canvas = document.createElement("canvas");
        const ctx = canvas.getContext('2d');

        // Create chart
        new Chart(ctx, {
            plugins: [ChartDataLabels, ChartColorSchemes],
            type: type,
            data: data,
            options: options
        });

        // Add element to output
        this.el.appendChild(canvas);
        console.log(version)
        console.log('end ipychart render');
    }
});

module.exports = {
    ChartModel: ChartModel,
    ChartView: ChartView
};