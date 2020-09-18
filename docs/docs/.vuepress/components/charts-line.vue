<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_de800071-2b7e-4409-bd0b-80bccda321cf" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_de800071-2b7e-4409-bd0b-80bccda321cf" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {

  name: 'getting-started',
  data () {return {}},

  beforeCreate: function () {
    this.$nextTick(function () {
      // Split embeded widget string into several strings to avoid JS "SyntaxError: unterminated string literal"
      let embedwidget = '<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js" integrity="sha2' + '56-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=" crossorigin="anonymous"><\/script><script data-jupy' + 'ter-widgets-cdn="https://cdn.jsdelivr.net/npm/" src="https://unpkg.com/@jupyter-widgets/html-manager' + '@*/dist/embed-amd.js" crossorigin="anonymous"><\/script><script type="application/vnd.jupyter.widget' + '-state+json">{"version_major": 2, "version_minor": 0, "state": {"43873cbc72eb4c91bd0af73693a75822": ' + '{"model_name": "LayoutModel", "model_module": "@jupyter-widgets/base", "model_module_version": "1.2.' + '0", "state": {"align_self": "stretch", "height": "auto"}}, "355060834b974b1d97e90c1e4c0c1071": {"mod' + 'el_name": "ChartModel", "model_module": "ipychart", "model_module_version": "^0.2.1", "state": {"_da' + 'ta": {"labels": ["Germany", "Spain", "UK", "Italy", "Norway", "France", "Poland", "Portugal", "Swede' + 'n", "Ireland"], "datasets": [{"data": [14, 106, 16, 107, 45, 133, 19, 109, 60, 107], "fill": false, ' + '"datalabels": {"display": false}, "backgroundColor": "rgba(54, 163, 235, 0.2)", "borderColor": "rgba' + '(54, 163, 235, 1)", "borderWidth": 1, "pointBackgroundColor": "rgba(54, 163, 235, 0.2)", "pointBorde' + 'rColor": "rgba(54, 163, 235, 1)"}]}, "_dom_classes": [], "_zoom": true, "_options": {"scales": {"yAxes": [{"display' + '": true, "ticks": {"beginAtZero": true, "display": true}}], "xAxes": [{"display": true, "ticks": {"b' + 'eginAtZero": true, "display": true}}]}, "legend": false}, "_type": "line", "layout": "IPY_MODEL_4387' + '3cbc72eb4c91bd0af73693a75822"}}}}<\/script><div id="widgetcontainer_92c2e8e1-fb36-47d8-824e-765e8cda' + 'e146"><script type="application/vnd.jupyter.widget-view+json">{"version_major": 2, "version_minor": ' + '0, "model_id": "355060834b974b1d97e90c1e4c0c1071"}<\/script></div>';
      // Set srcdoc of the iframe with embed widget HTML string. This trick allow to avoid disapearance of the iframe on page refresh
      var iframe = document.getElementById('chartframe_de800071-2b7e-4409-bd0b-80bccda321cf');
      iframe.srcdoc = embedwidget;
    });
  }
}
</script>