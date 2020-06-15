<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_ec8f3a1c-80d7-4158-ab04-2752f92bac39" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_ec8f3a1c-80d7-4158-ab04-2752f92bac39" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'chart-horizontalbar',
  data () {return {}},
  beforeCreate: function () {
    this.$nextTick(function () {
      // Split embeded widget string into several strings to avoid JS "SyntaxError: unterminated string literal"
      let embedwidget = '<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js" integrity="sha2' + '56-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=" crossorigin="anonymous"><\/script><script data-jupy' + 'ter-widgets-cdn="https://cdn.jsdelivr.net/npm/" src="https://unpkg.com/@jupyter-widgets/html-manager' + '@*/dist/embed-amd.js" crossorigin="anonymous"><\/script><script type="application/vnd.jupyter.widget' + '-state+json">{"version_major": 2, "version_minor": 0, "state": {"fea881de52244b9e9fd2d795f88fd86c": ' + '{"model_name": "LayoutModel", "model_module": "@jupyter-widgets/base", "model_module_version": "1.2.' + '0", "state": {"align_self": "stretch", "height": "auto"}}, "e4f75141a3414730b9aa6c6d302bd5dd": {"mod' + 'el_name": "ChartModel", "model_module": "ipychart", "model_module_version": "^0.1.0", "state": {"_da' + 'ta": {"labels": ["Red", "Blue", "Yellow", "Green", "Purple"], "datasets": [{"data": [140, 106, 160, ' + '107, 45], "label": "Dataset1", "borderWidth": 3, "backgroundColor": "rgba(255, 99, 132, 0.2)", "bord' + 'erColor": "rgba(255, 99, 132, 1)"}, {"data": [32, 160, 72, 140, 89], "label": "Dataset2", "borderWid' + 'th": 3, "backgroundColor": "rgba(54, 162, 235, 0.2)", "borderColor": "rgba(54, 162, 235, 1)"}]}, "_d' + 'om_classes": [], "_options": {"scale": {"ticks": {"beginAtZero": true}}}, "_type": "radar", "layout"' + ': "IPY_MODEL_fea881de52244b9e9fd2d795f88fd86c"}}}}<\/script><div id="widgetcontainer_ec8f3a1c-80d7-4' + '158-ab04-2752f92bac39"><script type="application/vnd.jupyter.widget-view+json">{"version_major": 2, ' + '"version_minor": 0, "model_id": "e4f75141a3414730b9aa6c6d302bd5dd"}<\/script></div>';
      // Set srcdoc of the iframe with embed widget HTML string. This trick allow to avoid disapearance of the iframe on page refresh
      var iframe = document.getElementById('chartframe_ec8f3a1c-80d7-4158-ab04-2752f92bac39');
      iframe.srcdoc = embedwidget;
    });
  }
}
</script>