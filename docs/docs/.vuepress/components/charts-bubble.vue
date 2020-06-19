<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_c9ef7af6-92db-494c-8a61-d3f0ac9af769" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_c9ef7af6-92db-494c-8a61-d3f0ac9af769" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'chart-horizontalbar',
  data () {return {}},
  beforeCreate: function () {
    this.$nextTick(function () {
      // Split embeded widget string into several strings to avoid JS "SyntaxError: unterminated string literal"
      let embedwidget = '<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js" integrity="sha2' + '56-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=" crossorigin="anonymous"><\/script><script data-jupy' + 'ter-widgets-cdn="https://cdn.jsdelivr.net/npm/" src="https://unpkg.com/@jupyter-widgets/html-manager' + '@*/dist/embed-amd.js" crossorigin="anonymous"><\/script><script type="application/vnd.jupyter.widget' + '-state+json">{"version_major": 2, "version_minor": 0, "state": {"f74e2fd9d9ed4ae1a9ead02a5972878a": ' + '{"model_name": "LayoutModel", "model_module": "@jupyter-widgets/base", "model_module_version": "1.2.' + '0", "state": {"align_self": "stretch", "height": "auto"}}, "a9f5504e0de942aa840b98bd53f48acb": {"mod' + 'el_name": "ChartModel", "model_module": "ipychart", "model_module_version": "^0.1.1", "state": {"_da' + 'ta": {"labels": ["Red", "Blue", "Yellow", "Green", "Purple"], "datasets": [{"data": [{"x": 20, "y": ' + '30, "r": 20}, {"x": 10, "y": 20, "r": 40}, {"x": 15, "y": 40, "r": 90}, {"x": 5, "y": 10, "r": 50}],' + ' "borderWidth": 4, "datalabels": {"display": false}, "backgroundColor": ["rgba(54, 163, 235, 0.2)", ' + '"rgba(254, 119, 124, 0.2)", "rgba(255, 206, 87, 0.2)", "rgba(11, 255, 238, 0.2)"], "borderColor": ["' + 'rgba(54, 163, 235, 1)", "rgba(254, 119, 124, 1)", "rgba(255, 206, 87, 1)", "rgba(11, 255, 238, 1)"]}' + ']}, "_dom_classes": [], "_options": {"scales": {"xAxes": [{"ticks": {"min": 0, "max": 25}}], "yAxes"' + ': [{"ticks": {"min": 0, "max": 60}}]}, "legend": false}, "_type": "bubble", "layout": "IPY_MODEL_f74' + 'e2fd9d9ed4ae1a9ead02a5972878a"}}}}<\/script><div id="widgetcontainer_a817164f-8fe3-40ed-8ab9-c933c0c' + '4dd88"><script type="application/vnd.jupyter.widget-view+json">{"version_major": 2, "version_minor":' + ' 0, "model_id": "a9f5504e0de942aa840b98bd53f48acb"}<\/script></div>';
      // Set srcdoc of the iframe with embed widget HTML string. This trick allow to avoid disapearance of the iframe on page refresh
      var iframe = document.getElementById('chartframe_c9ef7af6-92db-494c-8a61-d3f0ac9af769');
      iframe.srcdoc = embedwidget;
    });
  }
}
</script>