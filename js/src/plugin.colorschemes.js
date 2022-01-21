// This code comes from the chartjs-plugin-colorschemes package.
// The original code of this package is not compatible with chart.js 3.x.
// Therefore, the code has been adapted to work with chart.js 3.x. and integrated to ipychart.
// To see the original version of this file, please visit:
// https://github.com/nagix/chartjs-plugin-colorschemes/blob/master/src/plugins/plugin.colorschemes.js

import { Chart, registerables } from 'chart.js';
import { color, isArray } from 'chart.js/helpers';

Chart.register(...registerables);

const EXPANDO_KEY = '$colorschemes';

function getScheme(scheme) {
    let colorschemes; let matches; let arr; let
        category;

    if (isArray(scheme)) {
        return scheme;
    } if (typeof scheme === 'string') {
        colorschemes = Chart.colorschemes || {};

        // For backward compatibility
        matches = scheme.match(/^(brewer\.\w+)([1-3])-(\d+)$/);
        if (matches) {
            scheme = matches[1] + ['One', 'Two', 'Three'][matches[2] - 1] + matches[3];
        } else if (scheme === 'office.Office2007-2010-6') {
            scheme = 'office.OfficeClassic6';
        }

        arr = scheme.split('.');
        category = colorschemes[arr[0]];
        if (category) {
            return category[arr[1]];
        }
    }
}

const ColorSchemesPlugin = {
    id: 'colorschemes',

    beforeUpdate(chart, args, options) {
        // Please note that in v3, the args argument was added. It was not used before it was added,
        // so we just check if it is not actually our options object
        if (options === undefined) {
            options = args;
        }

        let scheme = getScheme(options.scheme);
        const { fillAlpha } = options;
        const { reverse } = options;
        const { override } = options;
        const { custom } = options;
        let schemeClone; let customResult; let length; let colorIndex; let
            colorCode;

        if (scheme) {
            if (typeof custom === 'function') {
                // Clone the original scheme
                schemeClone = scheme.slice();

                // Execute own custom color function
                customResult = custom(schemeClone);

                // Check if we received a filled array; otherwise keep and use the original scheme
                if (isArray(customResult) && customResult.length) {
                    scheme = customResult;
                } else if (isArray(schemeClone) && schemeClone.length) {
                    scheme = schemeClone;
                }
            }

            length = scheme.length;

            // Set scheme colors
            chart.config.data.datasets.forEach((dataset, datasetIndex) => {
                colorIndex = datasetIndex % length;
                colorCode = scheme[reverse ? length - colorIndex - 1 : colorIndex];

                // Object to store which color option is set
                dataset[EXPANDO_KEY] = {};

                switch (dataset.type || chart.config.type) {
                // For line, radar and scatter chart, borderColor and backgroundColor are set
                case 'line':
                case 'radar':
                case 'scatter':
                    if (typeof dataset.backgroundColor === 'undefined' || override) {
                        dataset[EXPANDO_KEY].backgroundColor = dataset.backgroundColor;
                        dataset.backgroundColor = color(colorCode)
                            .alpha(fillAlpha)
                            .rgbString();
                    }
                    if (typeof dataset.borderColor === 'undefined' || override) {
                        dataset[EXPANDO_KEY].borderColor = dataset.borderColor;
                        dataset.borderColor = colorCode;
                    }
                    if (typeof dataset.pointBackgroundColor === 'undefined' || override) {
                        dataset[EXPANDO_KEY].pointBackgroundColor = dataset.pointBackgroundColor;
                        dataset.pointBackgroundColor = color(colorCode)
                            .alpha(fillAlpha)
                            .rgbString();
                    }
                    if (typeof dataset.pointBorderColor === 'undefined' || override) {
                        dataset[EXPANDO_KEY].pointBorderColor = dataset.pointBorderColor;
                        dataset.pointBorderColor = colorCode;
                    }
                    break;
                    // For doughnut and pie chart, backgroundColor is set to an array of colors
                case 'doughnut':
                case 'pie':
                case 'polarArea':
                    if (typeof dataset.backgroundColor === 'undefined' || override) {
                        dataset[EXPANDO_KEY].backgroundColor = dataset.backgroundColor;
                        dataset.backgroundColor = dataset.data.map((data, dataIndex) => {
                            colorIndex = dataIndex % length;
                            return scheme[reverse ? length - colorIndex - 1 : colorIndex];
                        });
                    }
                    break;
                    // For bar chart backgroundColor (including fillAlpha) and borderColor are set
                case 'bar':
                    if (typeof dataset.backgroundColor === 'undefined' || override) {
                        dataset[EXPANDO_KEY].backgroundColor = dataset.backgroundColor;
                        dataset.backgroundColor = color(colorCode)
                            .alpha(fillAlpha)
                            .rgbString();
                    }
                    if (typeof dataset.borderColor === 'undefined' || override) {
                        dataset[EXPANDO_KEY].borderColor = dataset.borderColor;
                        dataset.borderColor = colorCode;
                    }
                    break;
                    // For the other chart, only backgroundColor is set
                default:
                    if (typeof dataset.backgroundColor === 'undefined' || override) {
                        dataset[EXPANDO_KEY].backgroundColor = dataset.backgroundColor;
                        dataset.backgroundColor = colorCode;
                    }
                    break;
                }
            });
        }
    },

    afterUpdate(chart) {
        // Unset colors
        chart.config.data.datasets.forEach((dataset) => {
            if (dataset[EXPANDO_KEY]) {
                if (Object.prototype.hasOwnProperty.call(dataset[EXPANDO_KEY], 'backgroundColor')) {
                    dataset.backgroundColor = dataset[EXPANDO_KEY].backgroundColor;
                }
                if (Object.prototype.hasOwnProperty.call(dataset[EXPANDO_KEY], 'borderColor')) {
                    dataset.borderColor = dataset[EXPANDO_KEY].borderColor;
                }
                if (Object.prototype.hasOwnProperty.call(dataset[EXPANDO_KEY], 'pointBackgroundColor')) {
                    dataset.pointBackgroundColor = dataset[EXPANDO_KEY].pointBackgroundColor;
                }
                if (Object.prototype.hasOwnProperty.call(dataset[EXPANDO_KEY], 'pointBorderColor')) {
                    dataset.pointBorderColor = dataset[EXPANDO_KEY].pointBorderColor;
                }
                delete dataset[EXPANDO_KEY];
            }
        });
    },
};

export default ColorSchemesPlugin;
