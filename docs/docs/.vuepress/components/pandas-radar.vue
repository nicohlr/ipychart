<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_d7070eaf-ef98-4a2e-b7d3-8583689013a8" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_d7070eaf-ef98-4a2e-b7d3-8583689013a8" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'chart-horizontalbar',
  data () {return {}},
  beforeCreate: function () {
    this.$nextTick(function () {
      // Split embeded widget string into several strings to avoid JS "SyntaxError: unterminated string literal"
      let embedwidget = '<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js" integrity="sha2' + '56-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=" crossorigin="anonymous"><\/script><script data-jupy' + 'ter-widgets-cdn="https://cdn.jsdelivr.net/npm/" src="https://unpkg.com/@jupyter-widgets/html-manager' + '@*/dist/embed-amd.js" crossorigin="anonymous"><\/script><script type="application/vnd.jupyter.widget' + '-state+json">{"version_major": 2, "version_minor": 0, "state": {"1c6f4d5256ee4f8d87685077e3ab3c5e": ' + '{"model_name": "LayoutModel", "model_module": "@jupyter-widgets/base", "model_module_version": "1.2.' + '0", "state": {"align_self": "stretch", "height": "auto"}}, "acaf1f7d38ae46e2a59d0bc2b149700e": {"mod' + 'el_name": "ChartModel", "model_module": "ipychart", "model_module_version": "^0.1.1", "state": {"_da' + 'ta": {"datasets": [{"data": [34.7031, 43.8001, 24.4416, 45.3303, 37.1697]}], "labels": ["Mr", "Mrs",' + ' "Miss", "Master", "Rare"]}, "_dom_classes": [], "_options": {"plugins": {"colorschemes": {"scheme":' + ' "office.Yellow6"}}, "scale": {"ticks": {"beginAtZero": true}}, "legend": false}, "_type": "radar", ' + '"layout": "IPY_MODEL_1c6f4d5256ee4f8d87685077e3ab3c5e"}}}}<\/script><div id="widgetcontainer_d7070ea' + 'f-ef98-4a2e-b7d3-8583689013a8"><script type="application/vnd.jupyter.widget-view+json">{"version_maj' + 'or": 2, "version_minor": 0, "model_id": "acaf1f7d38ae46e2a59d0bc2b149700e"}<\/script></div>';
      // Set srcdoc of the iframe with embed widget HTML string. This trick allow to avoid disapearance of the iframe on page refresh
      var iframe = document.getElementById('chartframe_d7070eaf-ef98-4a2e-b7d3-8583689013a8');
      iframe.srcdoc = embedwidget;
    });
  }
}
</script>

