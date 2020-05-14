const widgets = require('@jupyter-widgets/base');
const _ = require('lodash');
const Chart = require('chart.js');
const ChartDataLabels = require('chartjs-plugin-datalabels');
var version = require('../package.json')['version'];


// USEFUL FUNCTIONS
function checkNested(obj /*, level1, level2, ... levelN*/) {
    var args = Array.prototype.slice.call(arguments, 1);
    for (var i = 0; i < args.length; i++) {
        if (!obj || !obj.hasOwnProperty(args[i])) {
            return false;
        }
        obj = obj[args[i]];
    }
    return true;
}
  
// CREATE CHART
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

        // CHECK ALL POTENTIAL CALLBACK FUNCTIONS PASSED
        let check_callback_tooltips_beforetitle = checkNested(options, 'tooltips', 'callbacks', 'beforeTitle');
        let check_callback_tooltips_title = checkNested(options, 'tooltips', 'callbacks', 'title');
        let check_callback_tooltips_aftertitle = checkNested(options, 'tooltips', 'callbacks', 'afterTitle');
        let check_callback_tooltips_beforebody = checkNested(options, 'tooltips', 'callbacks', 'beforeBody');
        let check_callback_tooltips_beforelabel = checkNested(options, 'tooltips', 'callbacks', 'beforeLabel');
        let check_callback_tooltips_label = checkNested(options, 'tooltips', 'callbacks', 'label');
        let check_callback_tooltips_labelcolor = checkNested(options, 'tooltips', 'callbacks', 'labelColor');
        let check_callback_tooltips_labeltextcolor = checkNested(options, 'tooltips', 'callbacks', 'labelTextColor');
        let check_callback_tooltips_afterlabel = checkNested(options, 'tooltips', 'callbacks', 'afterLabel');
        let check_callback_tooltips_afterbody = checkNested(options, 'tooltips', 'callbacks', 'afterBody');
        let check_callback_tooltips_beforefooter = checkNested(options, 'tooltips', 'callbacks', 'beforeFooter');
        let check_callback_tooltips_footer = checkNested(options, 'tooltips', 'callbacks', 'footer');
        let check_callback_tooltips_afterfooter = checkNested(options, 'tooltips', 'callbacks', 'afterFooter');
        let check_callback_tooltips_custom = checkNested(options, 'tooltips', 'custom');

        let check_callback_legend = checkNested(options, 'legendCallback');
        let check_callback_legend_onclick = checkNested(options, 'legend', 'onClick');

        let check_callback_animation_progress = checkNested(options, 'animation', 'onProgress');
        let check_callback_animation_complete = checkNested(options, 'animation', 'onComplete ');

        let check_callback_xticks = checkNested(options, 'scales', 'xAxes', 'ticks', 'callback');
        let check_callback_yticks = checkNested(options, 'scales', 'yAxes', 'ticks', 'callback');
        let check_callback_xticks_major = checkNested(options, 'scales', 'xAxes', 'ticks', 'major', 'callback');
        let check_callback_yticks_major = checkNested(options, 'scales', 'yAxes', 'ticks', 'major', 'callback');
        let check_callback_xticks_beforeupdate = checkNested(options, 'scales', 'xAxes', 'beforeUpdate');
        let check_callback_yticks_beforeupdate = checkNested(options, 'scales', 'yAxes', 'beforeUpdate');
        let check_callback_xticks_beforesetdimensions = checkNested(options, 'scales', 'xAxes', 'beforeSetDimensions');
        let check_callback_yticks_beforesetdimensions = checkNested(options, 'scales', 'yAxes', 'beforeSetDimensions');
        let check_callback_xticks_aftersetdimensions = checkNested(options, 'scales', 'xAxes', 'afterSetDimensions');
        let check_callback_yticks_aftersetdimensions = checkNested(options, 'scales', 'yAxes', 'afterSetDimensions');
        let check_callback_xticks_beforedatalimits = checkNested(options, 'scales', 'xAxes', 'beforeDataLimits');
        let check_callback_yticks_beforedatalimits = checkNested(options, 'scales', 'yAxes', 'beforeDataLimits');
        let check_callback_xticks_afterdatalimits = checkNested(options, 'scales', 'xAxes', 'afterDataLimits');
        let check_callback_yticks_afterdatalimits = checkNested(options, 'scales', 'yAxes', 'afterDataLimits');
        let check_callback_xticks_beforebuildticks = checkNested(options, 'scales', 'xAxes', 'beforeBuildTicks');
        let check_callback_yticks_beforebuildticks = checkNested(options, 'scales', 'yAxes', 'beforeBuildTicks');
        let check_callback_xticks_afterbuildticks = checkNested(options, 'scales', 'xAxes', 'afterBuildTicks');
        let check_callback_yticks_afterbuildticks = checkNested(options, 'scales', 'yAxes', 'afterBuildTicks');
        let check_callback_xticks_beforeticktolabelconversion = checkNested(options, 'scales', 'xAxes', 'beforeTickToLabelConversion');
        let check_callback_yticks_beforeticktolabelconversion = checkNested(options, 'scales', 'yAxes', 'beforeTickToLabelConversion');
        let check_callback_xticks_afterticktolabelconversion = checkNested(options, 'scales', 'xAxes', 'afterTickToLabelConversion');
        let check_callback_yticks_afterticktolabelconversion = checkNested(options, 'scales', 'yAxes', 'afterTickToLabelConversion');
        let check_callback_xticks_beforecalculatetickrotation = checkNested(options, 'scales', 'xAxes', 'beforeCalculateTickRotation');
        let check_callback_yticks_beforecalculatetickrotation = checkNested(options, 'scales', 'yAxes', 'beforeCalculateTickRotation');
        let check_callback_xticks_aftercalculatetickrotation = checkNested(options, 'scales', 'xAxes', 'afterCalculateTickRotation');
        let check_callback_yticks_aftercalculatetickrotation = checkNested(options, 'scales', 'yAxes', 'afterCalculateTickRotation');
        let check_callback_xticks_beforefit = checkNested(options, 'scales', 'xAxes', 'beforeFit');
        let check_callback_yticks_beforefit = checkNested(options, 'scales', 'yAxes', 'beforeFit');
        let check_callback_xticks_afterfit = checkNested(options, 'scales', 'xAxes', 'afterFit');
        let check_callback_yticks_afterfit = checkNested(options, 'scales', 'yAxes', 'afterFit');
        let check_callback_xticks_afterupdate = checkNested(options, 'scales', 'xAxes', 'afterUpdate');
        let check_callback_yticks_afterupdate = checkNested(options, 'scales', 'yAxes', 'afterUpdate');

        let check_callback_pointlabels = checkNested(options, 'pointLabels', 'callback');
     
        // EVAL JAVASCRIPT CODE PASSED IN STRING FROM PYTHON
        if (check_callback_tooltips_beforetitle){
            options.tooltips.callbacks.beforeTitle = new Function('return ' + options.tooltips.callbacks.beforeTitle)();
        }
        if (check_callback_tooltips_title){
            options.tooltips.callbacks.title = new Function('return ' + options.tooltips.callbacks.title)();
        }
        if (check_callback_tooltips_aftertitle){
            options.tooltips.callbacks.afterTitle = new Function('return ' + options.tooltips.callbacks.afterTitle)();
        }
        if (check_callback_tooltips_beforebody){
            options.tooltips.callbacks.beforeBody = new Function('return ' + options.tooltips.callbacks.beforeBody)();
        }
        if (check_callback_tooltips_beforelabel){
            options.tooltips.callbacks.beforeLabel = new Function('return ' + options.tooltips.callbacks.beforeLabel)();
        }
        if (check_callback_tooltips_label){
            options.tooltips.callbacks.label = new Function('return ' + options.tooltips.callbacks.label)();
        }
        if (check_callback_tooltips_labelcolor){
            options.tooltips.callbacks.labelColor = new Function('return ' + options.tooltips.callbacks.labelColor)();
        }
        if (check_callback_tooltips_labeltextcolor){
            options.tooltips.callbacks.labelTextColor = new Function('return ' + options.tooltips.callbacks.labelTextColor)();
        }
        if (check_callback_tooltips_afterlabel){
            options.tooltips.callbacks.afterLabel = new Function('return ' + options.tooltips.callbacks.afterLabel)();
        }
        if (check_callback_tooltips_afterbody){
            options.tooltips.callbacks.afterBody = new Function('return ' + options.tooltips.callbacks.afterBody)();
        }
        if (check_callback_tooltips_beforefooter){
            options.tooltips.callbacks.beforeFooter = new Function('return ' + options.tooltips.callbacks.beforeFooter)();
        }
        if (check_callback_tooltips_footer){
            options.tooltips.callbacks.footer = new Function('return ' + options.tooltips.callbacks.footer)();
        }
        if (check_callback_tooltips_afterfooter){
            options.tooltips.callbacks.afterFooter = new Function('return ' + options.tooltips.callbacks.afterFooter)();
        }
        if (check_callback_tooltips_custom){
            options.tooltips.callbacks.custom = new Function('return ' + options.tooltips.callbacks.custom)();
        }


        if (check_callback_legend){
            options.legendCallback = new Function('return ' + options.legendCallback)();
        }
        if (check_callback_legend_onclick){
            options.legend.onClick = new Function('return ' + options.legend.onClick)();
        }


        if (check_callback_animation_progress){
            options.animation.onProgress = new Function('return ' + options.animation.onProgress)();
        }
        if (check_callback_animation_complete){
            options.animation.onComplete = new Function('return ' + options.animation.onComplete)();
        }


        if (check_callback_xticks){
            options.scales.xAxes.ticks.callback = new Function('return ' + options.scales.xAxes.ticks.callback)();
        }
        if (check_callback_yticks){
            options.scales.yAxes.ticks.callback = new Function('return ' + options.scales.yAxes.ticks.callback)();
        }
        if (check_callback_xticks_major){
            options.scales.xAxes.ticks.major.callback = new Function('return ' + options.scales.xAxes.ticks.major.callback)();
        }
        if (check_callback_yticks_major){
            options.scales.yAxes.ticks.major.callback = new Function('return ' + options.scales.yAxes.ticks.major.callback)();
        }
        if (check_callback_xticks_beforeupdate){
            options.scales.xAxes.beforeUpdate = new Function('return ' + options.scales.xAxes.beforeUpdate)();
        }
        if (check_callback_yticks_beforeupdate){
            options.scales.yAxes.beforeUpdate = new Function('return ' + options.scales.yAxes.beforeUpdate)();
        }
        if (check_callback_xticks_beforesetdimensions){
            options.scales.xAxes.beforeSetDimensions = new Function('return ' + options.scales.xAxes.beforeSetDimensions)();
        }
        if (check_callback_yticks_beforesetdimensions){
            options.scales.yAxes.beforeSetDimensions = new Function('return ' + options.scales.yAxes.beforeSetDimensions)();
        }
        if (check_callback_xticks_aftersetdimensions){
            options.scales.xAxes.afterSetDimensions = new Function('return ' + options.scales.xAxes.afterSetDimensions)();
        }
        if (check_callback_yticks_aftersetdimensions){
            options.scales.yAxes.afterSetDimensions = new Function('return ' + options.scales.yAxes.afterSetDimensions)();
        }
        if (check_callback_xticks_beforedatalimits){
            options.scales.xAxes.beforeDataLimits = new Function('return ' + options.scales.xAxes.beforeDataLimits)();
        }
        if (check_callback_yticks_beforedatalimits){
            options.scales.yAxes.beforeDataLimits = new Function('return ' + options.scales.yAxes.beforeDataLimits)();
        }
        if (check_callback_xticks_afterdatalimits){
            options.scales.xAxes.afterDataLimits = new Function('return ' + options.scales.xAxes.afterDataLimits)();
        }
        if (check_callback_yticks_afterdatalimits){
            options.scales.yAxes.afterDataLimits = new Function('return ' + options.scales.yAxes.afterDataLimits)();
        }
        if (check_callback_xticks_beforebuildticks){
            options.scales.xAxes.beforeBuildTicks = new Function('return ' + options.scales.xAxes.beforeBuildTicks)();
        }
        if (check_callback_yticks_beforebuildticks){
            options.scales.yAxes.beforeBuildTicks = new Function('return ' + options.scales.yAxes.beforeBuildTicks)();
        }
        if (check_callback_xticks_afterbuildticks){
            options.scales.xAxes.afterBuildTicks = new Function('return ' + options.scales.xAxes.afterBuildTicks)();
        }
        if (check_callback_yticks_afterbuildticks){
            options.scales.yAxes.afterBuildTicks = new Function('return ' + options.scales.yAxes.afterBuildTicks)();
        }
        if (check_callback_xticks_beforeticktolabelconversion){
            options.scales.xAxes.beforeTickToLabelConversion = new Function('return ' + options.scales.xAxes.beforeTickToLabelConversion)();
        }
        if (check_callback_yticks_beforeticktolabelconversion){
            options.scales.yAxes.beforeTickToLabelConversion = new Function('return ' + options.scales.yAxes.beforeTickToLabelConversion)();
        }
        if (check_callback_xticks_afterticktolabelconversion){
            options.scales.xAxes.afterTickToLabelConversion = new Function('return ' + options.scales.xAxes.afterTickToLabelConversion)();
        }
        if (check_callback_yticks_afterticktolabelconversion){
            options.scales.yAxes.afterTickToLabelConversion = new Function('return ' + options.scales.yAxes.afterTickToLabelConversion)();
        }
        if (check_callback_xticks_beforecalculatetickrotation){
            options.scales.xAxes.beforeCalculateTickRotation = new Function('return ' + options.scales.xAxes.beforeCalculateTickRotation)();
        }
        if (check_callback_yticks_beforecalculatetickrotation){
            options.scales.yAxes.beforeCalculateTickRotation = new Function('return ' + options.scales.yAxes.beforeCalculateTickRotation)();
        }
        if (check_callback_xticks_aftercalculatetickrotation){
            options.scales.xAxes.afterCalculateTickRotation = new Function('return ' + options.scales.xAxes.afterCalculateTickRotation)();
        }
        if (check_callback_yticks_aftercalculatetickrotation){
            options.scales.yAxes.afterCalculateTickRotation = new Function('return ' + options.scales.yAxes.afterCalculateTickRotation)();
        }
        if (check_callback_xticks_beforefit){
            options.scales.xAxes.beforeFit = new Function('return ' + options.scales.xAxes.beforeFit)();
        }
        if (check_callback_yticks_beforefit){
            options.scales.yAxes.beforeFit = new Function('return ' + options.scales.yAxes.beforeFit)();
        }
        if (check_callback_xticks_afterfit){
            options.scales.xAxes.afterFit = new Function('return ' + options.scales.xAxes.afterFit)();
        }
        if (check_callback_yticks_afterfit){
            options.scales.yAxes.afterFit = new Function('return ' + options.scales.yAxes.afterFit)();
        }
        if (check_callback_xticks_afterupdate){
            options.scales.xAxes.afterUpdate = new Function('return ' + options.scales.xAxes.afterUpdate)();
        }
        if (check_callback_yticks_afterupdate){
            options.scales.yAxes.afterUpdate = new Function('return ' + options.scales.yAxes.afterUpdate)();
        }

        
        if (check_callback_pointlabels){
            options.pointLabels.callback = new Function('return ' + options.pointLabels.callback)();
        }

        console.log('Chart options:', options)
        
        // Create Chart.js HTML element
        const canvas = document.createElement("canvas");
        const ctx = canvas.getContext('2d');

        // Create chart
        new Chart(ctx, {
            plugins: [ChartDataLabels],
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