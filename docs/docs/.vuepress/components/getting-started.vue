<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer" style="position:relative;width:100%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {

  name: 'getting-started',
  data () {return {}},

  beforeCreate: function () {
    this.$nextTick(function () {
      // Split embeded widget string into several strings to avoid JS "SyntaxError: unterminated string literal"
      let embedwidget = '<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js" integrity="sha2' + '56-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=" crossorigin="anonymous"><\/script><script data-jupy' + 'ter-widgets-cdn="https://cdn.jsdelivr.net/npm/" src="https://unpkg.com/@jupyter-widgets/html-manager' + '@*/dist/embed-amd.js" crossorigin="anonymous"><\/script><script type="application/vnd.jupyter.widget' + '-state+json">{"version_major": 2, "version_minor": 0, "state": {"b5e61f557b254da0bc5ff98e83806561": ' + '{"model_name": "LayoutModel", "model_module": "@jupyter-widgets/base", "model_module_version": "1.2.' + '0", "state": {"align_self": "stretch", "height": "auto"}}, "ac96ed534d164594bcbdccfe23419a2b": {"mod' + 'el_name": "ChartModel", "model_module": "ipychart", "model_module_version": "^0.1.0", "state": {"_da' + 'ta": {"labels": ["Germany", "Spain", "UK", "Italy", "Norway", "France", "Poland", "Portugal"], "data' + 'sets": [{"data": [114, 106, 106, 107, 111, 133, 109, 109], "backgroundColor": "rgba(255, 99, 132, 0.' + '2)", "borderColor": "rgba(255, 99, 132, 1)", "borderWidth": 1}]}, "_dom_classes": [], "_options": {"' + 'scales": [{"yAxes": [{"display": true, "ticks": {"beginAtZero": true, "display": true}}]}, {"xAxes":' + ' [{"display": true, "ticks": {"beginAtZero": true, "display": true}}]}], "beginAtZero": true, "legen' + 'd": false}, "_type": "bar", "layout": "IPY_MODEL_b5e61f557b254da0bc5ff98e83806561"}}}}<\/script><div' + ' id="widgetcontainer"><script type="application/vnd.jupyter.widget-view+json">{"version_major": 2, "' + 'version_minor": 0, "model_id": "ac96ed534d164594bcbdccfe23419a2b"}<\/script></div>';
      // Set srcdoc of the iframe with embed widget HTML string. This trick allow to avoid disapearance of the iframe on page refresh
      var iframe = document.getElementById('chartframe');
      iframe.srcdoc = embedwidget;
    });
  }
}
</script>