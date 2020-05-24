<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_5c018451-804c-4653-8a4f-c6638f19b3c3" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_5c018451-804c-4653-8a4f-c6638f19b3c3" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {

  name: 'options-legend',
  data () {return {}},

  beforeCreate: function () {
    this.$nextTick(function () {
      // Split embeded widget string into several strings to avoid JS "SyntaxError: unterminated string literal"
      let embedwidget = '<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js" integrity="sha2' + '56-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=" crossorigin="anonymous"><\/script><script data-jupy' + 'ter-widgets-cdn="https://cdn.jsdelivr.net/npm/" src="https://unpkg.com/@jupyter-widgets/html-manager' + '@*/dist/embed-amd.js" crossorigin="anonymous"><\/script><script type="application/vnd.jupyter.widget' + '-state+json">{"version_major": 2, "version_minor": 0, "state": {"e2b4f7b58b554b24a16ddec9babfddad": ' + '{"model_name": "LayoutModel", "model_module": "@jupyter-widgets/base", "model_module_version": "1.2.' + '0", "state": {"align_self": "stretch", "height": "auto"}}, "f82031e1b84044bd843199f19ea8876e": {"mod' + 'el_name": "ChartModel", "model_module": "ipychart", "model_module_version": "^0.1.0", "state": {"_da' + 'ta": {"labels": [1500, 1600, 1700, 1750, 1800, 1850, 1900, 1950, 1999, 2050], "datasets": [{"data": ' + '[86, 114, 106, 106, 107, 111, 133, 221, 121, 142], "label": "Africa", "fill": false, "backgroundColo' + 'r": "rgba(54, 163, 235, 0.2)", "borderColor": "rgba(54, 163, 235, 1)", "borderWidth": 1, "datalabels' + '": {"display": false}}, {"data": [99, 130, 64, 100, 73, 22, 88, 198, 144, 64], "label": "Asia", "fil' + 'l": false, "backgroundColor": "rgba(254, 119, 124, 0.2)", "borderColor": "rgba(254, 119, 124, 1)", "' + 'borderWidth": 1, "datalabels": {"display": false}}, {"data": [168, 170, 178, 190, 203, 200, 164, 100' + ', 72, 85], "label": "Europe", "fill": false, "backgroundColor": "rgba(255, 206, 87, 0.2)", "borderCo' + 'lor": "rgba(255, 206, 87, 1)", "borderWidth": 1, "datalabels": {"display": false}}, {"data": [40, 20' + ', 10, 16, 24, 38, 74, 167, 80, 150], "label": "Latin America", "fill": false, "backgroundColor": "rg' + 'ba(11, 255, 238, 0.2)", "borderColor": "rgba(11, 255, 238, 1)", "borderWidth": 1, "datalabels": {"di' + 'splay": false}}, {"data": [56, 95, 44, 112, 215, 35, 95, 74, 64, 78], "label": "North America", "fil' + 'l": false, "backgroundColor": "rgba(153, 102, 255, 0.2)", "borderColor": "rgba(153, 102, 255, 1)", "' + 'borderWidth": 1, "datalabels": {"display": false}}]}, "_dom_classes": [], "_options": {"legend": {"a' + 'lign": "end", "position": "right", "labels": {"boxWidth": 80, "fontSize": 14}}, "scale": {"ticks": {' + '"beginAtZero": true}}}, "_type": "radar", "layout": "IPY_MODEL_e2b4f7b58b554b24a16ddec9babfddad"}}}}' + '<\/script><div id="widgetcontainer_5c018451-804c-4653-8a4f-c6638f19b3c3"><script type="application/v' + 'nd.jupyter.widget-view+json">{"version_major": 2, "version_minor": 0, "model_id": "f82031e1b84044bd8' + '43199f19ea8876e"}<\/script></div>';
      // Set srcdoc of the iframe with embed widget HTML string. This trick allow to avoid disapearance of the iframe on page refresh
      var iframe = document.getElementById('chartframe_5c018451-804c-4653-8a4f-c6638f19b3c3');
      iframe.srcdoc = embedwidget;
    });
  }
}
</script>