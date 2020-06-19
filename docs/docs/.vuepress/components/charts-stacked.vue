<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_32603687-fb9a-4e25-8a24-179288388b67" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_32603687-fb9a-4e25-8a24-179288388b67" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'chart-horizontalbar',
  data () {return {}},
  beforeCreate: function () {
    this.$nextTick(function () {
      // Split embeded widget string into several strings to avoid JS "SyntaxError: unterminated string literal"
      let embedwidget = '<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js" integrity="sha2' + '56-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=" crossorigin="anonymous"><\/script><script data-jupy' + 'ter-widgets-cdn="https://cdn.jsdelivr.net/npm/" src="https://unpkg.com/@jupyter-widgets/html-manager' + '@*/dist/embed-amd.js" crossorigin="anonymous"><\/script><script type="application/vnd.jupyter.widget' + '-state+json">{"version_major": 2, "version_minor": 0, "state": {"710219e4f5af4136bd16d20c02981422": ' + '{"model_name": "LayoutModel", "model_module": "@jupyter-widgets/base", "model_module_version": "1.2.' + '0", "state": {"align_self": "stretch", "height": "auto"}}, "167ce0a9a6e04287af0d52c622e9bc7e": {"mod' + 'el_name": "ChartModel", "model_module": "ipychart", "model_module_version": "^0.1.1", "state": {"_da' + 'ta": {"labels": ["Dataset 1", "Dataset 2", "Dataset 3"], "datasets": [{"data": [221, 783, 2478], "la' + 'bel": "Africa", "fill": false, "datalabels": {"display": false}, "backgroundColor": "rgba(54, 163, 2' + '35, 0.2)", "borderColor": "rgba(54, 163, 235, 1)", "borderWidth": 1}, {"data": [1402, 3700, 5267], "' + 'label": "Asia", "fill": false, "datalabels": {"display": false}, "backgroundColor": "rgba(254, 119, ' + '124, 0.2)", "borderColor": "rgba(254, 119, 124, 1)", "borderWidth": 1}, {"data": [547, 675, 734], "l' + 'abel": "Europe", "fill": false, "datalabels": {"display": false}, "backgroundColor": "rgba(255, 206,' + ' 87, 0.2)", "borderColor": "rgba(255, 206, 87, 1)", "borderWidth": 1}, {"data": [167, 508, 784], "la' + 'bel": "Latin America", "fill": false, "datalabels": {"display": false}, "backgroundColor": "rgba(11,' + ' 255, 238, 0.2)", "borderColor": "rgba(11, 255, 238, 1)", "borderWidth": 1}, {"data": [172, 312, 433' + '], "label": "North America", "fill": false, "datalabels": {"display": false}, "backgroundColor": "rg' + 'ba(153, 102, 255, 0.2)", "borderColor": "rgba(153, 102, 255, 1)", "borderWidth": 1}]}, "_dom_classes' + '": [], "_options": {"scales": {"xAxes": [{"stacked": true}], "yAxes": [{"stacked": true}]}}, "_type"' + ': "bar", "layout": "IPY_MODEL_710219e4f5af4136bd16d20c02981422"}}}}<\/script><div id="widgetcontaine' + 'r_fef85279-a775-4c7d-a146-189cfce34a75"><script type="application/vnd.jupyter.widget-view+json">{"ve' + 'rsion_major": 2, "version_minor": 0, "model_id": "167ce0a9a6e04287af0d52c622e9bc7e"}<\/script></div>';
      // Set srcdoc of the iframe with embed widget HTML string. This trick allow to avoid disapearance of the iframe on page refresh
      var iframe = document.getElementById('chartframe_32603687-fb9a-4e25-8a24-179288388b67');
      iframe.srcdoc = embedwidget;
    });
  }
}
</script>