<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_7fa9eae2-c76b-4776-983c-7a106afe080b" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_7fa9eae2-c76b-4776-983c-7a106afe080b" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'chart-horizontalbar',
  data () {return {}},
  beforeCreate: function () {
    this.$nextTick(function () {
      // Split embeded widget string into several strings to avoid JS "SyntaxError: unterminated string literal"
      let embedwidget = '<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js" integrity="sha2' + '56-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=" crossorigin="anonymous"><\/script><script data-jupy' + 'ter-widgets-cdn="https://cdn.jsdelivr.net/npm/" src="https://unpkg.com/@jupyter-widgets/html-manager' + '@*/dist/embed-amd.js" crossorigin="anonymous"><\/script><script type="application/vnd.jupyter.widget' + '-state+json">{"version_major": 2, "version_minor": 0, "state": {"52e727705db74463882984c6a167b07c": ' + '{"model_name": "LayoutModel", "model_module": "@jupyter-widgets/base", "model_module_version": "1.2.' + '0", "state": {"align_self": "stretch", "height": "auto"}}, "2e8a0693a72c47e388da16aedf0b74a1": {"mod' + 'el_name": "ChartModel", "model_module": "ipychart", "model_module_version": "^0.1.1", "state": {"_da' + 'ta": {"labels": ["Label 1", "Label 2", "Label 3"], "datasets": [{"data": [221, 783, 2478], "label": "Af' + 'rica"}, {"data": [1402, 3700, 5267], "label": "Asia", "datalabels": {"display": true}}, {"data": [54' + '7, 675, 734], "label": "Europe"}, {"data": [167, 508, 784], "label": "Latin America"}, {"data": [172' + ', 312, 433], "label": "North America"}]}, "_dom_classes": [], "_options": {"plugins": {"colorschemes' + '": {"scheme": "tableau.Tableau10"}}, "scales": {"yAxes": [{"display": true, "ticks": {"beginAtZero":' + ' true, "display": true}}], "xAxes": [{"display": true, "ticks": {"beginAtZero": true, "display": tru' + 'e}}]}}, "_type": "bar", "layout": "IPY_MODEL_52e727705db74463882984c6a167b07c"}}}}<\/script><div id=' + '"widgetcontainer"><script type="application/vnd.jupyter.widget-view+json">{"version_major": 2, "vers' + 'ion_minor": 0, "model_id": "2e8a0693a72c47e388da16aedf0b74a1"}<\/script></div>';
      // Set srcdoc of the iframe with embed widget HTML string. This trick allow to avoid disapearance of the iframe on page refresh
      var iframe = document.getElementById('chartframe_7fa9eae2-c76b-4776-983c-7a106afe080b');
      iframe.srcdoc = embedwidget;
    });
  }
}
</script>
