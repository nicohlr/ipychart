<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_6eb84199-9a39-4448-87a3-ae3d6c8ffd92" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_6eb84199-9a39-4448-87a3-ae3d6c8ffd92" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'chart-horizontalbar',
  data () {return {}},
  beforeCreate: function () {
    this.$nextTick(function () {
      // Split embeded widget string into several strings to avoid JS "SyntaxError: unterminated string literal"
      let embedwidget = '<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js" integrity="sha2' + '56-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=" crossorigin="anonymous"><\/script><script data-jupy' + 'ter-widgets-cdn="https://cdn.jsdelivr.net/npm/" src="https://unpkg.com/@jupyter-widgets/html-manager' + '@*/dist/embed-amd.js" crossorigin="anonymous"><\/script><script type="application/vnd.jupyter.widget' + '-state+json">{"version_major": 2, "version_minor": 0, "state": {"45181256a6364c3ca855fd9eb432c528": ' + '{"model_name": "LayoutModel", "model_module": "@jupyter-widgets/base", "model_module_version": "1.2.' + '0", "state": {"align_self": "stretch", "height": "auto"}}, "21dd4527c77940f5bdbf3befb1e2d9d5": {"mod' + 'el_name": "ChartModel", "model_module": "ipychart", "model_module_version": "^0.2.1", "state": {"_da' + 'ta": {"labels": ["Dataset 1", "Dataset 2", "Dataset 3", "Dataset 4", "Dataset 5", "Dataset 6", "Data' + 'set 7", "Dataset 8", "Dataset 9", "Dataset 10"], "datasets": [{"data": [86, 114, 106, 106, 107, 111,' + ' 133, 221, 121, 142], "label": "Africa", "fill": false, "type": "line", "pointRadius": 5, "pointHove' + 'rRadius": 10, "datalabels": {"display": false}}, {"data": [99, 130, 64, 100, 73, 22, 88, 198, 144, 6' + '4], "label": "Asia", "datalabels": {"display": false}}, {"data": [168, 170, 178, 190, 203, 200, 164,' + ' 100, 72, 85], "label": "Europe", "fill": false, "type": "line", "pointRadius": 5, "pointHoverRadius' + '": 10, "datalabels": {"display": false}}, {"data": [40, 20, 10, 16, 24, 38, 74, 167, 80, 150], "labe' + 'l": "Latin America", "datalabels": {"display": false}}, {"data": [56, 95, 44, 112, 215, 35, 95, 74, ' + '64, 78], "label": "North America", "datalabels": {"display": false}}]}, "_dom_classes": [], "_zoom": true, "_option' + 's": {"plugins": {"colorschemes": {"scheme": "tableau.ClassicLight10"}}, "scales": {"yAxes": [{"displ' + 'ay": true, "ticks": {"beginAtZero": true, "display": true}}], "xAxes": [{"display": true, "ticks": {' + '"beginAtZero": true, "display": true}}]}}, "_type": "bar", "layout": "IPY_MODEL_45181256a6364c3ca855' + 'fd9eb432c528"}}}}<\/script><div id="widgetcontainer_b5c6a51f-83e9-4b8f-aacb-1efae6373a9c"><script ty' + 'pe="application/vnd.jupyter.widget-view+json">{"version_major": 2, "version_minor": 0, "model_id": "' + '21dd4527c77940f5bdbf3befb1e2d9d5"}<\/script></div>';
      // Set srcdoc of the iframe with embed widget HTML string. This trick allow to avoid disapearance of the iframe on page refresh
      var iframe = document.getElementById('chartframe_6eb84199-9a39-4448-87a3-ae3d6c8ffd92');
      iframe.srcdoc = embedwidget;
    });
  }
}
</script>