// This code comes from the chartjs-plugin-colorschemes package.
// The original code of this package is not compatible with chart.js 3.x.
// Therefore, the code has been adapted to work with chart.js 3.x. and integrated to ipychart.
// To see the original version of this file, please visit:
// https://github.com/nagix/chartjs-plugin-colorschemes/blob/master/src/plugins/plugin.colorschemes.js

import Chart from 'chart.js/auto';
import { isArray } from 'chart.js/helpers';

const EXPANDO_KEY = '$colorschemes';

function addAlpha(hex) {
    let c;
    if (/^#([A-Fa-f0-9]{3}){1,2}$/.test(hex)) {
        c = hex.substring(1).split('');
        if (c.length === 3) {
            c = [c[0], c[0], c[1], c[1], c[2], c[2]];
        }
        c = `0x${c.join('')}`;
        return `rgba(${[(c >> 16) & 255, (c >> 8) & 255, c & 255].join(',')},0.5)`;
    }
    throw new Error('Bad Hex');
}

function getScheme(scheme) {
    if (isArray(scheme) || scheme == null) {
        return scheme;
    }
    const colorschemes = Chart.colorschemes || {};
    const arr = scheme.split('.');
    const category = colorschemes[arr[0]];
    return category[arr[1]];
}

const ColorSchemesPlugin = {
    id: 'colorschemes',

    beforeUpdate(chart, args, options) {
        // Please note that in v3, the args argument was added. It was not used before it was added,
        // so we just check if it is not actually our options object
        if (options === undefined) {
            options = args;
        }

        const scheme = getScheme(options.scheme);
        const { reverse } = false;
        const { override } = true;
        let length;
        let colorIndex;
        let colorCode;

        if (scheme) {
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
                        dataset.backgroundColor = addAlpha(colorCode);
                    }
                    if (typeof dataset.borderColor === 'undefined' || override) {
                        dataset[EXPANDO_KEY].borderColor = dataset.borderColor;
                        dataset.borderColor = colorCode;
                    }
                    if (typeof dataset.pointBackgroundColor === 'undefined' || override) {
                        dataset[EXPANDO_KEY].pointBackgroundColor = dataset.pointBackgroundColor;
                        dataset.pointBackgroundColor = addAlpha(colorCode);
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
                        dataset.backgroundColor = colorCode;
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
                if (
                    Object.prototype.hasOwnProperty.call(
                        dataset[EXPANDO_KEY],
                        'pointBackgroundColor',
                    )
                ) {
                    dataset.pointBackgroundColor = dataset[EXPANDO_KEY].pointBackgroundColor;
                }
                if (
                    Object.prototype.hasOwnProperty.call(dataset[EXPANDO_KEY], 'pointBorderColor')
                ) {
                    dataset.pointBorderColor = dataset[EXPANDO_KEY].pointBorderColor;
                }
                delete dataset[EXPANDO_KEY];
            }
        });
    },
};

export default ColorSchemesPlugin;
