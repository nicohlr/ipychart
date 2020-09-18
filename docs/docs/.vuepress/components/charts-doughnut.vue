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
      let embedwidget = '<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js" integrity="sha2' + '56-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=" crossorigin="anonymous"><\/script><script data-jupy' + 'ter-widgets-cdn="https://cdn.jsdelivr.net/npm/" src="https://unpkg.com/@jupyter-widgets/html-manager' + '@*/dist/embed-amd.js" crossorigin="anonymous"><\/script><script type="application/vnd.jupyter.widget' + '-state+json">{"version_major": 2, "version_minor": 0, "state": {"e363992e1706454aa87402fb9560c92d": ' + '{"model_name": "LayoutModel", "model_module": "@jupyter-widgets/base", "model_module_version": "1.2.' + '0", "state": {"align_self": "stretch", "height": "auto"}}, "b16ab8eb104b48ca8294b94315102bb9": {"mod' + 'el_name": "ChartModel", "model_module": "ipychart", "model_module_version": "^0.2.1", "state": {"_da' + 'ta": {"labels": ["Red", "Blue", "Yellow", "Green", "Purple"], "datasets": [{"data": [140, 106, 160, ' + '107, 45], "backgroundColor": ["rgba(255, 99, 132, 1)", "rgba(54, 162, 235, 1)", "rgba(255, 206, 86, ' + '1)", "rgba(75, 192, 192, 1)", "rgba(153, 102, 255, 1)"], "datalabels": {"display": false}, "borderCo' + 'lor": ["rgba(255, 99, 132, 1)", "rgba(54, 162, 235, 1)", "rgba(255, 206, 86, 1)", "rgba(75, 192, 192' + ', 1)", "rgba(153, 102, 255, 1)"], "borderWidth": 1}]}, "_dom_classes": [], "_zoom": false, "_options": {"scales": {"' + 'yAxes": [{"display": false, "ticks": {"beginAtZero": true, "display": false}}], "xAxes": [{"display"' + ': false, "ticks": {"beginAtZero": true, "display": false}}]}}, "_type": "doughnut", "layout": "IPY_M' + 'ODEL_e363992e1706454aa87402fb9560c92d"}}}}<\/script><div id="widgetcontainer_e780d750-f47d-4433-b767' + '-5c0748361d2d"><script type="application/vnd.jupyter.widget-view+json">{"version_major": 2, "version' + '_minor": 0, "model_id": "b16ab8eb104b48ca8294b94315102bb9"}<\/script></div>';
      // Set srcdoc of the iframe with embed widget HTML string. This trick allow to avoid disapearance of the iframe on page refresh
      var iframe = document.getElementById('chartframe_fa18798a-6506-4932-8868-ed1858a3fe7a');
      iframe.srcdoc = embedwidget;
    });
  }
}
</script>