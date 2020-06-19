<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_9be18b10-b779-48a4-97fe-72fdf42604aa" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_9be18b10-b779-48a4-97fe-72fdf42604aa" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'chart-horizontalbar',
  data () {return {}},
  beforeCreate: function () {
    this.$nextTick(function () {
      // Split embeded widget string into several strings to avoid JS "SyntaxError: unterminated string literal"
      let embedwidget = '<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js" integrity="sha2' + '56-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=" crossorigin="anonymous"><\/script><script data-jupy' + 'ter-widgets-cdn="https://cdn.jsdelivr.net/npm/" src="https://unpkg.com/@jupyter-widgets/html-manager' + '@*/dist/embed-amd.js" crossorigin="anonymous"><\/script><script type="application/vnd.jupyter.widget' + '-state+json">{"version_major": 2, "version_minor": 0, "state": {"e3634d40e46b4009993bc8993c593c66": ' + '{"model_name": "LayoutModel", "model_module": "@jupyter-widgets/base", "model_module_version": "1.2.' + '0", "state": {"align_self": "stretch", "height": "auto"}}, "a7844327921440e3ba42d54b53093490": {"mod' + 'el_name": "ChartModel", "model_module": "ipychart", "model_module_version": "^0.1.0", "state": {"_da' + 'ta": {"labels": ["Dataset 1", "Dataset 2", "Dataset 3", "Dataset 4", "Dataset 5"], "datasets": [{"da' + 'ta": [500, 114, 106, 420, 107], "label": "Africa", "fill": false, "backgroundColor": "rgba(255, 99, ' + '132, 0.2)", "borderColor": "rgba(255, 99, 132, 1)", "borderWidth": 1}, {"data": [282, 350, 411, 350,' + ' 220], "label": "Asia", "fill": false, "backgroundColor": "rgba(54, 162, 235, 0.2)", "borderColor": ' + '"rgba(54, 162, 235, 1)", "borderWidth": 1}, {"data": [168, 170, 250, 380, 480], "label": "Europe", "' + 'fill": false, "backgroundColor": "rgba(255, 206, 86, 0.2)", "borderColor": "rgba(255, 206, 86, 1)", ' + '"borderWidth": 1}, {"data": [450, 270, 10, 100, 24], "label": "Latin America", "fill": false, "backg' + 'roundColor": "rgba(75, 192, 192, 0.2)", "borderColor": "rgba(75, 192, 192, 1)", "borderWidth": 1}, {' + '"data": [6, 40, 200, 300, 350], "label": "North America", "fill": false, "backgroundColor": "rgba(15' + '3, 102, 255, 0.2)", "borderColor": "rgba(153, 102, 255, 1)", "borderWidth": 1}]}, "_dom_classes": []' + ', "_options": {"scales": {"xAxes": [{"ticks": {"min": 0, "max": 500, "fontSize": 15, "fontStyle": "i' + 'talic", "stepSize": 0.5, "maxTicksLimit": 100}}], "yAxes": [{"ticks": {"min": 0, "max": 500, "fontSi' + 'ze": 15, "fontStyle": "italic", "stepSize": 50, "minRotation": 45, "padding": 20}}]}}, "_type": "lin' + 'e", "layout": "IPY_MODEL_e3634d40e46b4009993bc8993c593c66"}}}}<\/script><div id="widgetcontainer_9be' + '18b10-b779-48a4-97fe-72fdf42604aa"><script type="application/vnd.jupyter.widget-view+json">{"version' + '_major": 2, "version_minor": 0, "model_id": "a7844327921440e3ba42d54b53093490"}<\/script></div>';
      // Set srcdoc of the iframe with embed widget HTML string. This trick allow to avoid disapearance of the iframe on page refresh
      var iframe = document.getElementById('chartframe_9be18b10-b779-48a4-97fe-72fdf42604aa');
      iframe.srcdoc = embedwidget;
    });
  }
}
</script>