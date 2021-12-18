<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_002ef36d-09a5-4a76-9972-47e9ce608c4a" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_002ef36d-09a5-4a76-9972-47e9ce608c4a" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'pandas-bar',
  data () {return {}},
  beforeMount: function () {
    this.$nextTick(function () {
      // Split embeded widget string into several strings to avoid JS "SyntaxError: unterminated string literal"
      let embedwidget = '<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js" integrity="sha2' + '56-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=" crossorigin="anonymous"><\/script><script data-jupy' + 'ter-widgets-cdn="https://cdn.jsdelivr.net/npm/" src="https://unpkg.com/@jupyter-widgets/html-manager' + '@*/dist/embed-amd.js" crossorigin="anonymous"><\/script><script type="application/vnd.jupyter.widget' + '-state+json">{"version_major": 2, "version_minor": 0, "state": {"d125d798e98c4a9e84639987038185c2": ' + '{"model_name": "LayoutModel", "model_module": "@jupyter-widgets/base", "model_module_version": "1.2.' + '0", "state": {"align_self": "stretch", "height": "auto"}}, "f30900f463e64bdc8eb600ec728f4bcf": {"mod' + 'el_name": "ChartModel", "model_module": "ipychart", "model_module_version": "^0.3.0", "state": {"_da' + 'ta_sync": {"datasets": [{"data": [67.2261, 19.7418, 12.6616], "label": "male"}, {"data": [106.1258, 21.97' + '01, 16.1188], "label": "female"}], "labels": [1, 2, 3]}, "_dom_classes": [], "_zoom_sync": true, "_options_sync": {"scales": ' + '{"xAxes": [{"scaleLabel": {"display": true, "labelString": "Pclass"}}], "yAxes": [{"scaleLabel": {"d' + 'isplay": true, "labelString": "Fare (mean)"}}]}, "legend": {"labels": {"generateLabels": "function(chart) {' + 'let labels = Chart.defaults.global.legend.labels.generateLabels(chart);' + "labels.map(label => {label['text'] = 'Sex' + ' = ' + label['text']; retur" + 'n label});return labels;};"}}, "plugins": {"colorschemes": {"scheme": "off' + 'ice.Parallax6"}}}, "_kind_sync": "bar", "layout": "IPY_MODEL_d125d798e98c4a9e84639987038185c2"}}}}<\/scri' + 'pt><div id="widgetcontainer_002ef36d-09a5-4a76-9972-47e9ce608c4a"><script type="application/vnd.jupy' + 'ter.widget-view+json">{"version_major": 2, "version_minor": 0, "model_id": "f30900f463e64bdc8eb600ec' + '728f4bcf"}<\/script></div>';
      // Set srcdoc of the iframe with embed widget HTML string. This trick allow to avoid disapearance of the iframe on page refresh
      var iframe = document.getElementById('chartframe_002ef36d-09a5-4a76-9972-47e9ce608c4a');
      iframe.srcdoc = embedwidget;
    });
  }
}
</script>
