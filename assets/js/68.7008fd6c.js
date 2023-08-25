(window.webpackJsonp=window.webpackJsonp||[]).push([[68],{356:function(t,a,s){"use strict";s.r(a);var e=s(14),n=Object(e.a)({},(function(){var t=this,a=t._self._c;return a("ContentSlotsDistributor",{attrs:{"slot-key":t.$parent.slotKey}},[a("h1",{attrs:{id:"usage"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#usage"}},[t._v("#")]),t._v(" Usage")]),t._v(" "),a("p",[t._v("The ipychart library can be used in two different ways:")]),t._v(" "),a("ul",[a("li",[a("p",[t._v("The first one is by using the "),a("em",[t._v("Chart")]),t._v(" class, which replicates the "),a("em",[t._v("Chart")]),t._v(" class of Chart.js library while being adapted to the syntax of Python. The majority of the documentation is dedicated to it.")])]),t._v(" "),a("li",[a("p",[t._v("The second one allows you to quickly create charts from a pandas dataframe by using the exposed plot functions. It is described in the "),a("a",{attrs:{href:"/ipychart/user_guide/pandas"}},[t._v("Pandas Interface section")]),t._v(".")])])]),t._v(" "),a("h2",{attrs:{id:"chart-js-vs-ipychart"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#chart-js-vs-ipychart"}},[t._v("#")]),t._v(" Chart.js vs ipychart")]),t._v(" "),a("div",{staticClass:"custom-block tip"},[a("p",{staticClass:"custom-block-title"},[t._v("TIP")]),t._v(" "),a("p",[t._v("If you are already familiar with Chart.js, you can skip this part.")])]),t._v(" "),a("p",[t._v("Before looking at ipychart, let's take a look at what it looks like to create a chart with Chart.js. It will allow us to better understand how ipychart works:")]),t._v(" "),a("div",{staticClass:"language-js extra-class"},[a("pre",{pre:!0,attrs:{class:"language-js"}},[a("code",[a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("// This is to gather the html container of the chart")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("// Don't pay too much attention to this line of code")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("var")]),t._v(" ctx "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" document"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),a("span",{pre:!0,attrs:{class:"token function"}},[t._v("getElementById")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'myChart'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),a("span",{pre:!0,attrs:{class:"token function"}},[t._v("getContext")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'2d'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(";")]),t._v("\n\n"),a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("// The creation of the chart begins here")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("var")]),t._v(" chart "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("new")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token class-name"}},[t._v("Chart")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("ctx"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n    "),a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("// The type of chart we want to create")]),t._v("\n    "),a("span",{pre:!0,attrs:{class:"token literal-property property"}},[t._v("type")]),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'line'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n\n    "),a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("// The data for our dataset")]),t._v("\n    "),a("span",{pre:!0,attrs:{class:"token literal-property property"}},[t._v("data")]),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n        "),a("span",{pre:!0,attrs:{class:"token literal-property property"}},[t._v("labels")]),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'January'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'February'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'March'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'April'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'May'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'June'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'July'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n        "),a("span",{pre:!0,attrs:{class:"token literal-property property"}},[t._v("datasets")]),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n            "),a("span",{pre:!0,attrs:{class:"token literal-property property"}},[t._v("label")]),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'My First dataset'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n            "),a("span",{pre:!0,attrs:{class:"token literal-property property"}},[t._v("backgroundColor")]),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'rgb(255, 99, 132)'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n            "),a("span",{pre:!0,attrs:{class:"token literal-property property"}},[t._v("borderColor")]),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'rgb(255, 99, 132)'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n            "),a("span",{pre:!0,attrs:{class:"token literal-property property"}},[t._v("data")]),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),a("span",{pre:!0,attrs:{class:"token number"}},[t._v("0")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token number"}},[t._v("10")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token number"}},[t._v("5")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token number"}},[t._v("2")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token number"}},[t._v("20")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token number"}},[t._v("30")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token number"}},[t._v("45")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v("\n        "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v("\n    "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n\n    "),a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("// Configuration options go here")]),t._v("\n    "),a("span",{pre:!0,attrs:{class:"token literal-property property"}},[t._v("options")]),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(";")]),t._v("\n")])])]),a("p",[t._v("This example is taken from "),a("a",{attrs:{href:"https://www.chartjs.org/docs/latest/getting-started/",target:"_blank",rel:"noopener noreferrer"}},[t._v("the getting-started page of the Chart.js documentation"),a("OutboundLink")],1),t._v(". As you can see, there are three main arguments in Chart.js : "),a("strong",[t._v("data")]),t._v(", "),a("strong",[t._v("type")]),t._v(" and "),a("strong",[t._v("options")]),t._v(". These are the same arguments in ipychart, except for the "),a("code",[t._v("type")]),t._v(" argument which has been renamed "),a("code",[t._v("kind")]),t._v(" in ipychart because "),a("code",[t._v("type")]),t._v(" is a reserved keyword in the Python language.")]),t._v(" "),a("p",[t._v("Now, let's take a look on how we can create the same chart as above while using Python code and the ipychart library:")]),t._v(" "),a("div",{staticClass:"language-py extra-class"},[a("pre",{pre:!0,attrs:{class:"language-py"}},[a("code",[a("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("from")]),t._v(" ipychart "),a("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("import")]),t._v(" Chart\n\n"),a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("# The creation of the chart begins here")]),t._v("\nmychart "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" Chart"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("\n    "),a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("# The type of chart we want to create")]),t._v("\n    kind"),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'line'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n\n    "),a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("# The data for our dataset")]),t._v("\n    data"),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n        "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'labels'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'January'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'February'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'March'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'April'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'May'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'June'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'July'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n        "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'datasets'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n            "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'label'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'My First dataset'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n            "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'backgroundColor'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'rgb(255, 99, 132)'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n            "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'borderColor'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'rgb(255, 99, 132)'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n            "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'data'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),a("span",{pre:!0,attrs:{class:"token number"}},[t._v("0")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token number"}},[t._v("10")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token number"}},[t._v("5")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token number"}},[t._v("2")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token number"}},[t._v("20")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token number"}},[t._v("30")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token number"}},[t._v("45")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v("\n        "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v("\n    "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n\n    "),a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("# Configuration options go here")]),t._v("\n    "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'options'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\n")])])]),a("p",[t._v("As you can see, a Chart.js user will not be disoriented by switching to ipychart. Now, let's take a look at the specificities of each of these three arguments.")]),t._v(" "),a("h2",{attrs:{id:"chart-arguments"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#chart-arguments"}},[t._v("#")]),t._v(" Chart arguments")]),t._v(" "),a("p",[t._v("The "),a("em",[t._v("Chart")]),t._v(" class takes 5 arguments as inputs: "),a("strong",[t._v("data")]),t._v(", "),a("strong",[t._v("kind")]),t._v(", "),a("strong",[t._v("options")]),t._v(", "),a("strong",[t._v("colorscheme")]),t._v(" and "),a("strong",[t._v("zoom")]),t._v(". These arguments have a particular structure to match the backend Chart.js API. If you don't respect the structure of these arguments the package may not work.")]),t._v(" "),a("div",{staticClass:"language-py extra-class"},[a("pre",{pre:!0,attrs:{class:"language-py"}},[a("code",[t._v("Chart"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("data"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("dict")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n\t  kind"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n\t  options"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("dict")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token boolean"}},[t._v("None")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n\t  colorscheme"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token boolean"}},[t._v("None")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n\t  zoom"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("bool")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token boolean"}},[t._v("True")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\n")])])]),a("p",[t._v("In this section, we will go through each argument to present its use and its structure.")]),t._v(" "),a("h3",{attrs:{id:"data"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#data"}},[t._v("#")]),t._v(" Data")]),t._v(" "),a("p",[t._v("The "),a("code",[t._v("data")]),t._v(" argument is the most important one of the "),a("em",[t._v("Chart")]),t._v(" class. Without this argument, the chart cannot be displayed. The "),a("code",[t._v("data")]),t._v(" argument "),a("strong",[t._v("must be a dict")]),t._v(". This constraint is imposed by Chart.js, which takes its arguments via a Javascript object. This data dictionary must have the following structure :")]),t._v(" "),a("div",{staticClass:"language-py extra-class"},[a("pre",{pre:!0,attrs:{class:"language-py"}},[a("code",[t._v("data "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n    "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'datasets'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("list")]),t._v(" of "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("dict")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n    "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'labels'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("list")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n")])])]),a("p",[t._v("The value of "),a("code",[t._v("'datasets'")]),t._v(" will hold your data, it "),a("strong",[t._v("must be a list of dictionaries, each one containing at least a key named")]),t._v(" "),a("code",[t._v("'data'")]),t._v(". It is a list because you can display more than one ensemble of data points in one chart. Each sub dictionary corresponds to an ensemble of data points, representing a dataset, and must also follow a specific structure. However, this structure may change according to the type of chart.")]),t._v(" "),a("p",[t._v("Please refer to "),a("a",{attrs:{href:"/ipychart/user_guide/charts"}},[t._v("the documentation of each chart type")]),t._v(" to have more details about the dataset structure to use.")]),t._v(" "),a("p",[t._v("The value of "),a("code",[t._v("'labels'")]),t._v(" "),a("strong",[t._v("must be a list")]),t._v(". If only one dataset is passed, the labels list will represent the labels of each datapoint of the only dataset passed. However, if more than one dataset is passed, the label list will represent the labels of each dataset.")]),t._v(" "),a("div",{staticClass:"custom-block warning"},[a("p",{staticClass:"custom-block-title"},[t._v("WARNING")]),t._v(" "),a("p",[t._v("The data dictionary must have these two elements, otherwise you can expect dysfunction or unexpected behavior.")])]),t._v(" "),a("h3",{attrs:{id:"kind"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#kind"}},[t._v("#")]),t._v(" Kind")]),t._v(" "),a("p",[t._v("The "),a("code",[t._v("kind")]),t._v(" argument allows you to choose the type of chart you want to draw. It "),a("strong",[t._v("must be a string")]),t._v(". You can choose a type of string from the following list:")]),t._v(" "),a("div",{staticClass:"language-py extra-class"},[a("pre",{pre:!0,attrs:{class:"language-py"}},[a("code",[a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("# Possible values for the kind argument")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'line'")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'bar'")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'radar'")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'doughnut'")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'pie'")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'polarArea'")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'bubble'")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'scatter'")]),t._v("\n")])])]),a("div",{staticClass:"custom-block tip"},[a("p",{staticClass:"custom-block-title"},[t._v("TIP")]),t._v(" "),a("p",[t._v("The "),a("code",[t._v("type")]),t._v(" argument in Chart.js became "),a("code",[t._v("kind")]),t._v(" argument in Python because, unlike Javascript, type is a reserved keyword in Python.")])]),t._v(" "),a("h3",{attrs:{id:"options"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#options"}},[t._v("#")]),t._v(" Options")]),t._v(" "),a("p",[t._v("Finally, the last argument of the "),a("em",[t._v("Chart")]),t._v(" class is "),a("code",[t._v("options")]),t._v(". This argument "),a("strong",[t._v("must be a dict")]),t._v(", it allows you to completely configure your chart.")]),t._v(" "),a("div",{staticClass:"language-py extra-class"},[a("pre",{pre:!0,attrs:{class:"language-py"}},[a("code",[t._v("options "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n    "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'legend'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("dict")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" \n    "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'title'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("dict")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n    "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'tooltips'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("dict")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n    "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'scales'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("dict")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n    "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'layout'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("dict")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n    "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'hover'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("dict")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n    "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'animation'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("dict")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n")])])]),a("p",[t._v("Below is the use case of each of these dictionaries. Of course, these five dictionaries have numerous sub arguments. This is why two whole sections of this documentation have been dedicated to them.")]),t._v(" "),a("ul",[a("li",[a("strong",[t._v("legend:")]),t._v(" you can configure the legend of your chart with this dictionary. In ipychart, legend is dynamic and allows you to display or hide some of your inputted datasets! To find out how you can customize the legend of your chart, please check the "),a("a",{attrs:{href:"/ipychart/user_guide/configuration#legend"}},[t._v("legend documentation section")]),t._v(".")]),t._v(" "),a("li",[a("strong",[t._v("title:")]),t._v(" you can configure the title of your chart with this dictionary. To find out how, please check the "),a("a",{attrs:{href:"/ipychart/user_guide/configuration#title"}},[t._v("title documentation section")]),t._v(".")]),t._v(" "),a("li",[a("strong",[t._v("tooltips:")]),t._v(' you can configure the tooltips of your chart with this dictionary. In ipychart, hovering a chart displays some information, these popups are called "tooltips". You can configure these tooltips in many ways. To find out how, please check the '),a("a",{attrs:{href:"/ipychart/user_guide/configuration#tooltips"}},[t._v("tooltips documentation section")]),t._v(". You can even inject some Javascript code to display your own text around your data on while hovering a chart. The procedure for doing this is described in the "),a("a",{attrs:{href:"/ipychart/user_guide/advanced#callback-functions"}},[t._v("callback functions section of the documentation")]),t._v(".")]),t._v(" "),a("li",[a("strong",[t._v("scales:")]),t._v(" you can configure the scales of your chart with this dictionary. To find out how, please check the "),a("a",{attrs:{href:"/ipychart/user_guide/scales"}},[t._v("scales page")]),t._v(".")]),t._v(" "),a("li",[a("strong",[t._v("layout:")]),t._v(" you can configure the layout of your chart with this dictionary. To find out how, please check the "),a("a",{attrs:{href:"/ipychart/user_guide/configuration#layout"}},[t._v("layout documentation section")]),t._v(".")]),t._v(" "),a("li",[a("strong",[t._v("hover:")]),t._v(" you can configure the hovering options of your chart with this dictionary. To find out how, please check the "),a("a",{attrs:{href:"/ipychart/user_guide/configuration#hover"}},[t._v("hover documentation section")]),t._v(".")]),t._v(" "),a("li",[a("strong",[t._v("animation:")]),t._v(" you can configure the animations of your chart with this dictionary. To find out how, please check the "),a("a",{attrs:{href:"/ipychart/user_guide/configuration#animations"}},[t._v("animation documentation section")]),t._v(".")])]),t._v(" "),a("h3",{attrs:{id:"colorscheme"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#colorscheme"}},[t._v("#")]),t._v(" Colorscheme")]),t._v(" "),a("div",{staticClass:"custom-block warning"},[a("p",{staticClass:"custom-block-title"},[t._v("WARNING")]),t._v(" "),a("p",[t._v("The "),a("code",[t._v("colorscheme")]),t._v(" argument will overwrite any color configuration passed through the datasets of the chart.")])]),t._v(" "),a("p",[t._v("The "),a("code",[t._v("colorscheme")]),t._v(" argument allow you to automatically set a predefined color scheme to your chart. This is a feature which is not present natively in Chart.js. It has been added in ipychart using "),a("a",{attrs:{href:"https://github.com/nagix/chartjs-plugin-colorschemes",target:"_blank",rel:"noopener noreferrer"}},[t._v("an open-source implementation"),a("OutboundLink")],1),t._v(".")]),t._v(" "),a("p",[t._v("The "),a("code",[t._v("colorscheme")]),t._v(" argument must be a string corresponding to the chosen color scheme ("),a("a",{attrs:{href:"https://nagix.github.io/chartjs-plugin-colorschemes/colorchart.html",target:"_blank",rel:"noopener noreferrer"}},[t._v("click here to see the list of all the available color schemes"),a("OutboundLink")],1),t._v("). Color schemes are based on popular tools such as ColorBrewer, Microsoft Office and Tableau.")]),t._v(" "),a("p",[t._v("Example of setting a colorscheme to a chart:")]),t._v(" "),a("div",{staticClass:"language-py extra-class"},[a("pre",{pre:!0,attrs:{class:"language-py"}},[a("code",[t._v("mychart "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" Chart"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("data"),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v("mydata"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'bar'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" options"),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v("myoptions"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" colorscheme"),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),a("span",{pre:!0,attrs:{class:"token string"}},[t._v("'tableau.Blue20'")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\n")])])]),a("p",[t._v("Please note that the chart will associate one color of the colorscheme to each dataset. Thus, if your chart contains only one dataset, this one will be drawn only in one color.")]),t._v(" "),a("p",[t._v("Now that you are familiar with the structure of each argument, you can head to the next section to learn about the different types of charts.")]),t._v(" "),a("h3",{attrs:{id:"zoom"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#zoom"}},[t._v("#")]),t._v(" Zoom")]),t._v(" "),a("div",{staticClass:"custom-block warning"},[a("p",{staticClass:"custom-block-title"},[t._v("WARNING")]),t._v(" "),a("p",[t._v("The zoom features is not available for "),a("strong",[t._v("radar")]),t._v(", "),a("strong",[t._v("doughnut")]),t._v(", "),a("strong",[t._v("pie")]),t._v(" and "),a("strong",[t._v("polarArea")]),t._v(" charts (i.e. the "),a("code",[t._v("zoom")]),t._v(" argument will automatically be set to "),a("code",[t._v("False")]),t._v(" for these charts).")])]),t._v(" "),a("p",[t._v("The "),a("code",[t._v("zoom")]),t._v(" argument allow you to zoom on the chart once it is created. As the "),a("code",[t._v("colorscheme")]),t._v(" argument, the "),a("code",[t._v("zoom")]),t._v(" argument is not present natively in Chart.js. It has been added in ipychart using "),a("a",{attrs:{href:"https://github.com/chartjs/chartjs-plugin-zoom",target:"_blank",rel:"noopener noreferrer"}},[t._v("an open-source implementation"),a("OutboundLink")],1),t._v(".")]),t._v(" "),a("p",[t._v("By default, the zoom is activated when you create a chart. To disable this feature, just set the zoom argument of the chart to "),a("code",[t._v("False")]),t._v(".")]),t._v(" "),a("div",{staticClass:"custom-block tip"},[a("p",{staticClass:"custom-block-title"},[t._v("TIP")]),t._v(" "),a("p",[t._v("To reset the zoom to its initial level, you only have to double click anywhere on the chart!")])])])}),[],!1,null,null,null);a.default=n.exports}}]);