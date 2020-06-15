<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_fa18798a-6506-4932-8868-ed1858a3fe7a" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_fa18798a-6506-4932-8868-ed1858a3fe7a" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'chart-horizontalbar',
  data () {return {}},
  beforeCreate: function () {
    this.$nextTick(function () {
      // Split embeded widget string into several strings to avoid JS "SyntaxError: unterminated string literal"
      let embedwidget = '<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js" integrity="sha2' + '56-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=" crossorigin="anonymous"><\/script><script data-jupy' + 'ter-widgets-cdn="https://cdn.jsdelivr.net/npm/" src="https://unpkg.com/@jupyter-widgets/html-manager' + '@*/dist/embed-amd.js" crossorigin="anonymous"><\/script><script type="application/vnd.jupyter.widget' + '-state+json">{"version_major": 2, "version_minor": 0, "state": {"09cb683cd9d24e0baf49b2b0198fd3ce": ' + '{"model_name": "LayoutModel", "model_module": "@jupyter-widgets/base", "model_module_version": "1.2.' + '0", "state": {"align_self": "stretch", "height": "auto"}}, "1bb82d6796764524ae6ce474428d2cf3": {"mod' + 'el_name": "ChartModel", "model_module": "ipychart", "model_module_version": "^0.1.0", "state": {"_da' + 'ta": {"labels": ["Red", "Blue", "Yellow", "Green", "Purple"], "datasets": [{"data": [140, 106, 160, ' + '107, 45], "backgroundColor": ["rgba(255, 99, 132, 1)", "rgba(54, 162, 235, 1)", "rgba(255, 206, 86, ' + '1)", "rgba(75, 192, 192, 1)", "rgba(153, 102, 255, 1)"], "borderColor": ["rgba(255, 99, 132, 1)", "r' + 'gba(54, 162, 235, 1)", "rgba(255, 206, 86, 1)", "rgba(75, 192, 192, 1)", "rgba(153, 102, 255, 1)"], ' + '"borderWidth": 1}]}, "_dom_classes": [], "_options": {"scales": [{"yAxes": [{"display": false, "tick' + 's": {"beginAtZero": true, "display": false}}]}, {"xAxes": [{"display": false, "ticks": {"beginAtZero' + '": true, "display": false}}]}], "beginAtZero": true}, "_type": "doughnut", "layout": "IPY_MODEL_09cb' + '683cd9d24e0baf49b2b0198fd3ce"}}}}<\/script><div id="widgetcontainer_b2730fac-1998-4106-a5da-199d7ae9' + '9fa2"><script type="application/vnd.jupyter.widget-view+json">{"version_major": 2, "version_minor": ' + '0, "model_id": "1bb82d6796764524ae6ce474428d2cf3"}<\/script></div>';
      // Set srcdoc of the iframe with embed widget HTML string. This trick allow to avoid disapearance of the iframe on page refresh
      var iframe = document.getElementById('chartframe_fa18798a-6506-4932-8868-ed1858a3fe7a');
      iframe.srcdoc = embedwidget;
    });
  }
}
</script>