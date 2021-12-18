<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_9be18b10-b779-48a4-97fe-72fdf42604aa" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_9be18b10-b779-48a4-97fe-72fdf42604aa" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'scales-ticks',
  data () {return {}},
  beforeMount: function () {
    this.$nextTick(function () {
      // Split embeded widget string into several strings to avoid JS "SyntaxError: unterminated string literal"
      let embedwidget = '<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js" integrity="sha2' + '56-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=" crossorigin="anonymous"><\/script><script data-jupy' + 'ter-widgets-cdn="https://cdn.jsdelivr.net/npm/" src="https://unpkg.com/@jupyter-widgets/html-manager' + '@*/dist/embed-amd.js" crossorigin="anonymous"><\/script><script type="application/vnd.jupyter.widget' + '-state+json">{"version_major": 2, "version_minor": 0, "state": {"d35d96090e0d4c35a3a34b9699fbefc0": ' + '{"model_name": "LayoutModel", "model_module": "@jupyter-widgets/base", "model_module_version": "1.2.' + '0", "state": {"align_self": "stretch", "height": "auto"}}, "04462452010a418e8e52cde561b1b839": {"mod' + 'el_name": "ChartModel", "model_module": "ipychart", "model_module_version": "^0.3.0", "state": {"_da' + 'ta_sync": {"labels": ["Data 1", "Data 2", "Data 3", "Data 4", "Data 5"], "datasets": [{"da' + 'ta": [500, 114, 106, 420, 107], "label": "Africa", "fill": false, "datalabels": {"display": false}},' + ' {"data": [282, 350, 411, 350, 220], "label": "Asia", "fill": false, "datalabels": {"display": false' + '}}, {"data": [168, 170, 250, 380, 480], "label": "Europe", "fill": false, "datalabels": {"display": ' + 'false}}, {"data": [450, 270, 10, 100, 24], "label": "Latin America", "fill": false, "datalabels": {"' + 'display": false}}, {"data": [6, 40, 200, 300, 350], "label": "North America", "fill": false, "datala' + 'bels": {"display": false}}]}, "_dom_classes": [], "_zoom_sync": true, "_options_sync": {"scales": {"xAxes": [{"ticks": {"min"' + ': 0, "max": 500, "fontSize": 15, "fontStyle": "italic", "stepSize": 0.5, "maxTicksLimit": 100}}], "y' + 'Axes": [{"ticks": {"min": 0, "max": 500, "fontSize": 15, "fontStyle": "italic", "stepSize": 50, "min' + 'Rotation": 45, "padding": 20}}]}, "plugins": {"colorschemes": {"scheme": "office.Composite6"}}}, "_kind' + '_sync": "line", "layout": "IPY_MODEL_d35d96090e0d4c35a3a34b9699fbefc0"}}}}<\/script><div id="widgetcon' + 'tainer_ab148336-80d5-4329-beae-0b3cdfd084c4"><script type="application/vnd.jupyter.widget-view+json"' + '>{"version_major": 2, "version_minor": 0, "model_id": "04462452010a418e8e52cde561b1b839"}<\/script><' + '/div>';
      // Set srcdoc of the iframe with embed widget HTML string. This trick allow to avoid disapearance of the iframe on page refresh
      var iframe = document.getElementById('chartframe_9be18b10-b779-48a4-97fe-72fdf42604aa');
      iframe.srcdoc = embedwidget;
    });
  }
}
</script>
