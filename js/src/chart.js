// Global imports
import * as widgets from '@jupyter-widgets/base';
import { Chart, registerables } from 'chart.js';
import ChartDataLabels from 'chartjs-plugin-datalabels';
import ChartZoom from 'chartjs-plugin-zoom';
import _ from 'lodash';

// Local imports
import colorschemes from './colorschemes/index';
import ColorSchemesPlugin from './plugin.colorschemes';
import version from './version';

// Register plugins
Chart.colorschemes = colorschemes;
Chart.register(ColorSchemesPlugin);
Chart.register(...registerables);
Chart.register(ChartZoom);
Chart.register(ChartDataLabels);

// Define the widget model.
const ChartModel = widgets.DOMWidgetModel.extend({
    defaults: _.extend(widgets.DOMWidgetModel.prototype.defaults(), {
        _model_name: 'ChartModel',
        _view_name: 'ChartView',
        _model_module: 'ipychart',
        _view_module: 'ipychart',
        _model_module_version: `^${version}`,
        _view_module_version: `^${version}`,
    }),
});

// Define the widget view.
const ChartView = widgets.DOMWidgetView.extend({
    convert_input_data(data, options) {
        // Set datalabels default options
        _.forEach(data.datasets, (dataset, i) => {
            // If datalabels options are not provided, hide datalabels by default in each dataset.
            // If datalabels options are provided, set automatic coloring based on colorscheme or
            // dataset color when borderwidth is != 0

            if (!_.has(dataset, 'datalabels')) {
                _.set(dataset, 'datalabels', { display: false });
            } else if (_.has(options, ['plugins', 'colorschemes', 'scheme'])) {
                const color = _.get(Chart.colorschemes, options.plugins.colorschemes.scheme)[i];
                if (_.has(dataset.datalabels, 'borderWidth')) {
                    if (!_.has(dataset.datalabels, 'backgroundColor')) {
                        _.set(dataset.datalabels, 'backgroundColor', color);
                    }
                    if (!_.has(dataset.datalabels, 'borderColor')) {
                        _.set(dataset.datalabels, 'borderColor', color);
                    }
                }
            } else {
                if (!_.has(dataset.datalabels, 'backgroundColor')) {
                    _.set(dataset.datalabels, 'backgroundColor', dataset.backgroundColor);
                }
                if (!_.has(dataset.datalabels, 'borderColor')) {
                    _.set(dataset.datalabels, 'borderColor', dataset.borderColor);
                }
            }
        });

        return data;
    },

    convert_input_options(options, colorscheme, zoom) {
        // All paths of options dictionary with callback functions
        const callbackOptionsPaths = [
            ['legendCallback'],
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
            ['animations', 'onProgress'],
            ['animations', 'onComplete '],
            ['scale', 'pointLabels', 'callback'],
            ['scale', 'ticks', 'callback'],
            ['scale', 'ticks', 'minor', 'callback'],
            ['scale', 'ticks', 'major', 'callback'],
            ['plugins', 'datalabels', 'formatter']
        ];

        // These paths must be handled for all axes
        // i.e. all axes contained in scales.xAxes or scales.yAxes arrays
        const callbackScalesPaths = [
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
            ['afterUpdate'],
        ];

        // Convert strings containing callback functions to real JS functions for all paths
        _.forEach(callbackOptionsPaths, (callbackPath) => {
            if (_.has(options, callbackPath)) {
                _.set(
                    options,
                    callbackPath,
                    new Function(`return ${_.get(options, callbackPath)}`)(),
                );
            }
        });

        // Convert strings containing this.callback functions to real JS functions for x axis paths
        if (_.has(options, ['scales', 'xAxes'])) {
            _.forEach(options.scales.xAxes, (xaxes) => {
                _.forEach(callbackScalesPaths, (callbackPath) => {
                    if (_.has(xaxes, callbackPath)) {
                        _.set(
                            xaxes,
                            callbackPath,
                            new Function(`return ${_.get(xaxes, callbackPath)}`)(),
                        );
                    }
                });
            });
        }

        // Convert strings containing callback functions to real JS functions for y axis paths
        if (_.has(options, ['scales', 'yAxes'])) {
            _.forEach(options.scales.yAxes, (yaxes) => {
                _.forEach(callbackScalesPaths, (callbackPath) => {
                    if (_.has(yaxes, callbackPath)) {
                        _.set(
                            yaxes,
                            callbackPath,
                            new Function(`return ${_.get(yaxes, callbackPath)}`)(),
                        );
                    }
                });
            });
        }

        // Set colorscheme options if not None
        if (colorscheme) {
            options = _.merge(
                { plugins: { colorschemes: { scheme: colorscheme, override: true } } },
                options,
            );
        }

        // Set zoom options
        options = _.merge(
            {
                plugins: {
                    zoom: {
                        zoom: {
                            wheel: { enabled: false },
                            pinch: { enabled: false },
                            drag: { enabled: zoom },
                        },
                        pan: { enabled: false },
                    },
                },
            },
            options,
        );

        return options;
    },

    render() {
        // Get data and type from python
        this.input = document.createElement('input');
        this.input.colorscheme = this.model.get('_colorscheme_sync');
        this.input.zoom = this.model.get('_zoom_sync');

        this.input.options = this.convert_input_options(
            this.model.get('_options_sync'),
            this.input.colorscheme,
            this.input.zoom,
        );
        this.input.data = this.convert_input_data(this.model.get('_data_sync'), this.input.options);
        this.input.kind = this.model.get('_kind_sync');

        console.log('Chart data:', this.input.data);
        console.log('Chart options:', this.input.options);
        console.log('Chart type:', this.input.kind);
        console.log('Chart colorscheme:', this.input.colorscheme);
        console.log('Chart zoom:', this.input.zoom);

        // Create Chart.js HTML element
        if (!this.chart) {
            this.canvas = document.createElement('canvas');
            this.ctx = this.canvas.getContext('2d');

            // Create chart
            this.chart = new Chart(this.ctx, {
                type: this.input.kind,
                data: this.input.data,
                options: this.input.options,
            });

            this.chart.canvas.ondblclick = function resetzoom() {
                this.chart.resetZoom();
            }.bind(this);

            // Add element to output
            if (!this.el.canvas) {
                this.el.appendChild(this.canvas);
            }
            console.log('Chart created');

            // Python -> JavaScript update
            this.model.on('change:_data_sync', this.data_changed, this);
            this.model.on('change:_options_sync', this.options_changed, this);
            this.model.on('change:_kind_sync', this.kind_changed, this);
            this.model.on('change:_colorscheme_sync', this.colorscheme_changed, this);
            this.model.on('change:_zoom_sync', this.zoom_changed, this);

            // JavaScript -> Python update
            this.input.onchange = this.input_changed.bind(this);
        } else {
            // Update chart
            this.chart.destroy();
            this.chart = new Chart(this.ctx, {
                type: this.input.kind,
                data: this.input.data,
                options: this.input.options,
            });

            this.chart.canvas.ondblclick = function resetzoom() {
                this.chart.resetZoom();
            }.bind(this);

            console.log('Chart udpated');
        }
    },

    data_changed() {
        this.input.data = this.model.get('_data_sync');
        this.render();
    },
    options_changed() {
        this.input.options = this.model.get('_options_sync');
        this.render();
    },
    kind_changed() {
        this.input.kind = this.model.get('_kind_sync');
        this.render();
    },
    colorscheme_changed() {
        this.input.colorscheme = this.model.get('_colorscheme_sync');
        this.render();
    },
    zoom_changed() {
        this.input.zoom = this.model.get('_zoom');
        this.render();
    },

    input_changed() {
        this.model.set('_data_sync', this.input.data);
        this.model.set('_options_sync', this.input.options);
        this.model.set('_kind_sync', this.input.kind);
        this.model.set('_colorscheme_sync', this.input.colorscheme);
        this.model.set('_zoom_sync', this.input.zoom);
        this.model.save_changes();
        this.render();
    },
});

export { ChartModel, ChartView };
