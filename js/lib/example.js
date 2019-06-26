var widgets = require('@jupyter-widgets/base');
var _ = require('lodash');


// Custom Model. Custom widgets models must at least provide default values
// for model attributes, including
//
//  - `_view_name`
//  - `_view_module`
//  - `_view_module_version`
//
//  - `_model_name`
//  - `_model_module`
//  - `_model_module_version`
//
//  when different from the base class.

// When serialiazing the entire widget state for embedding, only values that
// differ from the defaults will be specified.
var HelloModel = widgets.DOMWidgetModel.extend({
    defaults: _.extend(widgets.DOMWidgetModel.prototype.defaults(), {
        _model_name : 'HelloModel',
        _view_name : 'HelloView',
        _model_module : 'ipychart',
        _view_module : 'ipychart',
        _model_module_version : '^0.1.0',
        _view_module_version : '^0.1.0',
        value : 'Hello World'
    })
});


// Custom View. Renders the widget model.
var HelloView = widgets.DOMWidgetView.extend({

    callback:function(inputEvent, formElement){
        this.model.set({'value':formElement[0].value})    // update the JS model with the current view value
        this.touch()   // sync the JS model with the Python backend
    },

    render: function() {
        this.model.on('change:value', this.value_changed, this);

        let view = this;

        // standard HTML DOM change from JS
        let f = document.createElement("form");
        let i = document.createElement("input"); // input element, text
        i.setAttribute('type',"text");
        f.appendChild(i);
        this.el.appendChild(f);
        let title = document.createElement("h3");
        this.el.appendChild(title);

        // initializing the form and the title values
        i.setAttribute('value', this.model.get('value'));
        title.textContent = this.model.get('value');

        // Listening to changes in the frontend input
        f.addEventListener("input", (inputEvent => view.callback(inputEvent, f)), false);

        // handle to access the DOM elements directly
        this.input = i;
        this.title = title;
    },

    value_changed: function() {
        // access to the 'input' DOM element
        this.input.setAttribute('value', this.model.get('value'))
        // access to the 'h3' DOM element
        this.title.textContent = this.model.get('value')

    }
});


module.exports = {
    HelloModel : HelloModel,
    HelloView : HelloView
};
