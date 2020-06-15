<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_248cdabf-1f08-43a9-b145-74173e91e6d0" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_248cdabf-1f08-43a9-b145-74173e91e6d0" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'chart-horizontalbar',
  data () {return {}},
  beforeCreate: function () {
    this.$nextTick(function () {
      // Split embeded widget string into several strings to avoid JS "SyntaxError: unterminated string literal"
      let embedwidget = '<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js" integrity="sha2' + '56-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=" crossorigin="anonymous"><\/script><script data-jupy' + 'ter-widgets-cdn="https://cdn.jsdelivr.net/npm/" src="https://unpkg.com/@jupyter-widgets/html-manager' + '@*/dist/embed-amd.js" crossorigin="anonymous"><\/script><script type="application/vnd.jupyter.widget' + '-state+json">{"version_major": 2, "version_minor": 0, "state": {"1a53b60e69c641f1831f24065556945f": ' + '{"model_name": "LayoutModel", "model_module": "@jupyter-widgets/base", "model_module_version": "1.2.' + '0", "state": {"align_self": "stretch", "height": "auto"}}, "df11d47797a14f198e55d66ab677f4e5": {"mod' + 'el_name": "ChartModel", "model_module": "ipychart", "model_module_version": "^0.1.0", "state": {"_da' + 'ta": {"labels": ["Red", "Blue", "Yellow", "Green", "Purple"], "datasets": [{"data": [140, 106, 160, ' + '107, 45], "backgroundColor": ["rgba(255, 99, 132, 1)", "rgba(54, 162, 235, 1)", "rgba(255, 206, 86, ' + '1)", "rgba(75, 192, 192, 1)", "rgba(153, 102, 255, 1)"], "borderColor": ["rgba(255, 99, 132, 1)", "r' + 'gba(54, 162, 235, 1)", "rgba(255, 206, 86, 1)", "rgba(75, 192, 192, 1)", "rgba(153, 102, 255, 1)"], ' + '"borderWidth": 1}]}, "_dom_classes": [], "_options": {"scales": [{"yAxes": [{"display": false, "tick' + 's": {"beginAtZero": true, "display": false}}]}, {"xAxes": [{"display": false, "ticks": {"beginAtZero' + '": true, "display": false}}]}], "beginAtZero": true}, "_type": "pie", "layout": "IPY_MODEL_1a53b60e6' + '9c641f1831f24065556945f"}}}}<\/script><div id="widgetcontainer_248cdabf-1f08-43a9-b145-74173e91e6d0"' + '><script type="application/vnd.jupyter.widget-view+json">{"version_major": 2, "version_minor": 0, "m' + 'odel_id": "df11d47797a14f198e55d66ab677f4e5"}<\/script></div>';
      // Set srcdoc of the iframe with embed widget HTML string. This trick allow to avoid disapearance of the iframe on page refresh
      var iframe = document.getElementById('chartframe_248cdabf-1f08-43a9-b145-74173e91e6d0');
      iframe.srcdoc = embedwidget;
    });
  }
}
</script>