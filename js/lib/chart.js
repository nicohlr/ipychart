var widgets = require('@jupyter-widgets/base');
var _ = require('lodash');
var Chart = require('chart.js');

var BarChartModel = widgets.DOMWidgetModel.extend({
    defaults: _.extend(widgets.DOMWidgetModel.prototype.defaults(), {
        _model_name : 'BarChartModel',
        _view_name : 'BarChartView',
        _model_module : 'ipychart',
        _view_module : 'ipychart',
        _model_module_version : '^0.1.0',
        _view_module_version : '^0.1.0',
    })
});

var BarChartView = widgets.DOMWidgetView.extend({
    render: function() {
        var data = this.model.get("_model_data");

        // Check if data are passed from python to js
        console.log(data);

        // Create Chart.js HTML element
        let canvas = document.createElement("canvas");
        var ctx = canvas.getContext('2d');

        // Create chart
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
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
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        });

        // Add element to output
        this.el.appendChild(canvas);
    }
});

module.exports = {
    BarChartModel: BarChartModel,
    BarChartView: BarChartView
};