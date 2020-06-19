<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_996db55d-7bd7-44ae-b271-78977886b51c" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_996db55d-7bd7-44ae-b271-78977886b51c" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {

  name: 'getting-started',
  data () {return {}},

  beforeCreate: function () {
    this.$nextTick(function () {
      // Split embeded widget string into several strings to avoid JS "SyntaxError: unterminated string literal"
      let embedwidget = '<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js" integrity="sha2' + '56-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=" crossorigin="anonymous"><\/script><script data-jupy' + 'ter-widgets-cdn="https://cdn.jsdelivr.net/npm/" src="https://unpkg.com/@jupyter-widgets/html-manager' + '@*/dist/embed-amd.js" crossorigin="anonymous"><\/script><script type="application/vnd.jupyter.widget' + '-state+json">{"version_major": 2, "version_minor": 0, "state": {"4b1dff4d0aa04ffd8676cf4f6d78ffb8": ' + '{"model_name": "LayoutModel", "model_module": "@jupyter-widgets/base", "model_module_version": "1.2.' + '0", "state": {"align_self": "stretch", "height": "auto"}}, "2394a9ba18074276ab7fee4aa4aac424": {"mod' + 'el_name": "ChartModel", "model_module": "ipychart", "model_module_version": "^0.1.0", "state": {"_da' + 'ta": {"labels": ["Germany", "Spain", "UK", "Italy", "Norway", "France", "Poland", "Portugal", "Swede' + 'n", "Ireland"], "datasets": [{"data": [14, 106, 16, 107, 45, 133, 109, 109, 108, 107], "backgroundCo' + 'lor": "rgba(75, 192, 192, 0.2)", "fill": false, "datalabels": {"display": true, "borderRadius": 4, "' + 'borderWidth": 1, "anchor": "end", "align": "end", "backgroundColor": "rgba(75, 192, 192, 0.2)", "bor' + 'derColor": "rgba(75, 192, 192, 1)"}, "borderColor": "rgba(75, 192, 192, 1)", "borderWidth": 1}]}, "_' + 'dom_classes": [], "_options": {"layout": {"padding": {"left": 40, "right": 40, "top": 60, "bottom"' + ': 60}}, "scales": {"yAxes": [{"display": true, "ticks": {"beginAtZero": true, "display": true}}], "x' + 'Axes": [{"display": true, "ticks": {"beginAtZero": true, "display": true}}]}, "legend": false}, "_ty' + 'pe": "line", "layout": "IPY_MODEL_4b1dff4d0aa04ffd8676cf4f6d78ffb8"}}}}<\/script><div id="widgetcont' + 'ainer_996db55d-7bd7-44ae-b271-78977886b51c"><script type="application/vnd.jupyter.widget-view+json">' + '{"version_major": 2, "version_minor": 0, "model_id": "2394a9ba18074276ab7fee4aa4aac424"}<\/script></' + 'div>';
      // Set srcdoc of the iframe with embed widget HTML string. This trick allow to avoid disapearance of the iframe on page refresh
      var iframe = document.getElementById('chartframe_996db55d-7bd7-44ae-b271-78977886b51c');
      iframe.srcdoc = embedwidget;
    });
  }
}
</script>