'use strict';

// This code comes from the chartjs-plugin-colorschemes package.
// The original code of this package is not compatible with chart.js 3.x.
// Therefore, the code has been adapted to work with chart.js 3.x. and integrated to ipychart.
// To see the original version of this file, please visit:
// https://github.com/nagix/chartjs-plugin-colorschemes/blob/master/src/plugins/plugin.colorschemes.js

import { Chart, registerables } from 'chart.js';
import { color, isArray } from 'chart.js/helpers';
Chart.register(...registerables);

var EXPANDO_KEY = '$colorschemes';


function getScheme(scheme) {
	var colorschemes, matches, arr, category;

	if (isArray(scheme)) {
		return scheme;
	} else if (typeof scheme === 'string') {
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

var ColorSchemesPlugin = {
	id: 'colorschemes',

	beforeUpdate: function(chart, args, options) {
		// Please note that in v3, the args argument was added. It was not used before it was added,
		// so we just check if it is not actually our options object
		if (options === undefined) {
			options = args;
		}

		var scheme = getScheme(options.scheme);
		var fillAlpha = options.fillAlpha;
		var reverse = options.reverse;
		var override = options.override;
		var custom = options.custom;
		var schemeClone, customResult, length, colorIndex, colorCode;

		if (scheme) {

			if (typeof custom === 'function') {
				// clone the original scheme
				schemeClone = scheme.slice();

				// Execute own custom color function
				customResult = custom(schemeClone);

				// check if we really received a filled array; otherwise we keep and use the original scheme
				if (isArray(customResult) && customResult.length) {
					scheme = customResult;
				} else if (isArray(schemeClone) && schemeClone.length) {
					scheme = schemeClone;
				}
			}

			length = scheme.length;

			// Set scheme colors
			chart.config.data.datasets.forEach(function(dataset, datasetIndex) {
				colorIndex = datasetIndex % length;
				colorCode = scheme[reverse ? length - colorIndex - 1 : colorIndex];

				// Object to store which color option is set
				dataset[EXPANDO_KEY] = {};

				switch (dataset.type || chart.config.type) {
				// For line, radar and scatter chart, borderColor and backgroundColor (50% transparent) are set
				case 'line':
				case 'radar':
				case 'scatter':
					if (typeof dataset.backgroundColor === 'undefined' || override) {
						dataset[EXPANDO_KEY].backgroundColor = dataset.backgroundColor;
						dataset.backgroundColor = color(colorCode).alpha(fillAlpha).rgbString();
					}
					if (typeof dataset.borderColor === 'undefined' || override) {
						dataset[EXPANDO_KEY].borderColor = dataset.borderColor;
						dataset.borderColor = colorCode;
					}
					if (typeof dataset.pointBackgroundColor === 'undefined' || override) {
						dataset[EXPANDO_KEY].pointBackgroundColor = dataset.pointBackgroundColor;
						dataset.pointBackgroundColor = color(colorCode).alpha(fillAlpha).rgbString();
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
						dataset.backgroundColor = dataset.data.map(function(data, dataIndex) {
							colorIndex = dataIndex % length;
							return scheme[reverse ? length - colorIndex - 1 : colorIndex];
						});
					}
					break;
				// For bar chart backgroundColor (including fillAlpha) and borderColor are set
				case 'bar':
					if (typeof dataset.backgroundColor === 'undefined' || override) {
						dataset[EXPANDO_KEY].backgroundColor = dataset.backgroundColor;
						dataset.backgroundColor = color(colorCode).alpha(fillAlpha).rgbString();
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

	afterUpdate: function(chart) {
		// Unset colors
		chart.config.data.datasets.forEach(function(dataset) {
			if (dataset[EXPANDO_KEY]) {
				if (dataset[EXPANDO_KEY].hasOwnProperty('backgroundColor')) {
					dataset.backgroundColor = dataset[EXPANDO_KEY].backgroundColor;
				}
				if (dataset[EXPANDO_KEY].hasOwnProperty('borderColor')) {
					dataset.borderColor = dataset[EXPANDO_KEY].borderColor;
				}
				if (dataset[EXPANDO_KEY].hasOwnProperty('pointBackgroundColor')) {
					dataset.pointBackgroundColor = dataset[EXPANDO_KEY].pointBackgroundColor;
				}
				if (dataset[EXPANDO_KEY].hasOwnProperty('pointBorderColor')) {
					dataset.pointBorderColor = dataset[EXPANDO_KEY].pointBorderColor;
				}
				delete dataset[EXPANDO_KEY];
			}
		});
	},
};

export default ColorSchemesPlugin;
