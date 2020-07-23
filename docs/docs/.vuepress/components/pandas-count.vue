<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_e6ae8e63-25db-43ee-8051-d545f45a6fb3" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_e6ae8e63-25db-43ee-8051-d545f45a6fb3" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'chart-horizontalbar',
  data () {return {}},
  beforeCreate: function () {
    this.$nextTick(function () {
      // Split embeded widget string into several strings to avoid JS "SyntaxError: unterminated string literal"
      let embedwidget = '<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js" integrity="sha2' + '56-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=" crossorigin="anonymous"><\/script><script data-jupy' + 'ter-widgets-cdn="https://cdn.jsdelivr.net/npm/" src="https://unpkg.com/@jupyter-widgets/html-manager' + '@*/dist/embed-amd.js" crossorigin="anonymous"><\/script><script type="application/vnd.jupyter.widget' + '-state+json">{"version_major": 2, "version_minor": 0, "state": {"16934f895e324ed4882004a0a3d35fd8": ' + '{"model_name": "LayoutModel", "model_module": "@jupyter-widgets/base", "model_module_version": "1.2.' + '0", "state": {"align_self": "stretch", "height": "auto"}}, "62bfca7645d04c4cad3838345e7bc761": {"mod' + 'el_name": "ChartModel", "model_module": "ipychart", "model_module_version": "^0.1.1", "state": {"_da' + 'ta": {"datasets": [{"data": [644, 168, 77], "backgroundColor": ["rgba(54, 163, 235, 0.2)", "rgba(254' + ', 119, 124, 0.2)", "rgba(255, 206, 87, 0.2)", "rgba(54, 163, 235, 0.2)", "rgba(254, 119, 124, 0.2)",' + ' "rgba(255, 206, 87, 0.2)", "rgba(54, 163, 235, 0.2)", "rgba(254, 119, 124, 0.2)", "rgba(255, 206, 8' + '7, 0.2)", "rgba(54, 163, 235, 0.2)", "rgba(254, 119, 124, 0.2)", "rgba(255, 206, 87, 0.2)"], "border' + 'Color": ["rgba(54, 163, 235, 1)", "rgba(254, 119, 124, 1)", "rgba(255, 206, 87, 1)", "rgba(54, 163, ' + '235, 1)", "rgba(254, 119, 124, 1)", "rgba(255, 206, 87, 1)", "rgba(54, 163, 235, 1)", "rgba(254, 119' + ', 124, 1)", "rgba(255, 206, 87, 1)", "rgba(54, 163, 235, 1)", "rgba(254, 119, 124, 1)", "rgba(255, 2' + '06, 87, 1)"], "borderWidth": 1}], "labels": ["S", "C", "Q"]}, "_dom_classes": [], "_options": {"scal' + 'es": {"xAxes": [{"scaleLabel": {"display": true, "labelString": "Embarked"}}], "yAxes": [{"scaleLabe' + 'l": {"display": true, "labelString": "Count"}}]}, "legend": false}, "_type": "bar", "layout": "IPY_M' + 'ODEL_16934f895e324ed4882004a0a3d35fd8"}}}}<\/script><div id="widgetcontainer_e6ae8e63-25db-43ee-8051' + '-d545f45a6fb3"><script type="application/vnd.jupyter.widget-view+json">{"version_major": 2, "version' + '_minor": 0, "model_id": "62bfca7645d04c4cad3838345e7bc761"}<\/script></div>';
      // Set srcdoc of the iframe with embed widget HTML string. This trick allow to avoid disapearance of the iframe on page refresh
      var iframe = document.getElementById('chartframe_e6ae8e63-25db-43ee-8051-d545f45a6fb3');
      iframe.srcdoc = embedwidget;
    });
  }
}
</script>

