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
        let label = this.model.get("_label");
        let type = this.model.get("_type");

        // Add options according to type
        let xaxis_display = true;
        let yaxis_display = true;
        if (['radar', 'doughnut', 'polarArea'].indexOf(str) >= 0) {
            xaxis_display = false;
            yaxis_display = false;
        }

        // Check if data are passed from python to js
        console.log(data);
        console.log(type);

        // Create Chart.js HTML element
        const canvas = document.createElement("canvas");
        const ctx = canvas.getContext('2d');

        // Create chart
        new Chart(ctx, {
            type: type,
            data: {
                labels: label,
                datasets: [{
                    label: '# of Votes',
                    data: data,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(255, 159, 64, 0.2)'
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    xAxes: [{
                        display: xaxis_display,
                        ticks: {
                            display: xaxis_display
                        }
                    }],
                    yAxes: [{
                        display: yaxis_display,
                        ticks: {
                            beginAtZero: true,
                            display: yaxis_display
                        }
                    }]
                }
            }
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