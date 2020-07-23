<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_1ffdc891-0f79-4900-a8fc-948f9fb38795" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_1ffdc891-0f79-4900-a8fc-948f9fb38795" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'chart-horizontalbar',
  data () {return {}},
  beforeCreate: function () {
    this.$nextTick(function () {
      // Split embeded widget string into several strings to avoid JS "SyntaxError: unterminated string literal"
      let embedwidget = '<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js" integrity="sha2' + '56-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=" crossorigin="anonymous"><\/script><script data-jupy' + 'ter-widgets-cdn="https://cdn.jsdelivr.net/npm/" src="https://unpkg.com/@jupyter-widgets/html-manager' + '@*/dist/embed-amd.js" crossorigin="anonymous"><\/script><script type="application/vnd.jupyter.widget' + '-state+json">{"version_major": 2, "version_minor": 0, "state": {"282120f4254b4240a8804961d883d4f1": ' + '{"model_name": "LayoutModel", "model_module": "@jupyter-widgets/base", "model_module_version": "1.2.' + '0", "state": {"align_self": "stretch", "height": "auto"}}, "311790751c8d46c29755b2175b007023": {"mod' + 'el_name": "ChartModel", "model_module": "ipychart", "model_module_version": "^0.1.1", "state": {"_da' + 'ta": {"datasets": [{"data": [41.2814, 30.7407, 26.5076], "label": "male", "fill": false, "datalabels' + '": {"display": true, "borderWidth": 1, "anchor": "end", "align": "end", "borderRadius": 5, "color": ' + '"#fff"}}, {"data": [34.6118, 28.723, 21.75], "label": "female", "fill": false, "datalabels": {"displ' + 'ay": true, "borderWidth": 1, "anchor": "end", "align": "end", "borderRadius": 5, "color": "#fff"}}],' + ' "labels": [1, 2, 3]}, "_dom_classes": [], "_options": {"scales": {"xAxes": [{"scaleLabel": {"displa' + 'y": true, "labelString": "Pclass"}}], "yAxes": [{"scaleLabel": {"display": true, "labelString": "Age' + '"}}]}, "legend": {"labels": {"generateLabels": "function(chart) {let label' + 's = Chart.defaults.global.legend.labels.generateLabels(chart);labels.map(l' + "abel => {label['text'] = 'Sex' + ' = ' + label['text']; return label});" + ' return labels;};"}}, "plugins": {"colorschemes": {"scheme": "office.Parallax6"}}}, "_type": "line",' + ' "layout": "IPY_MODEL_282120f4254b4240a8804961d883d4f1"}}}}<\/script><div id="widgetcontainer_1ffdc8' + '91-0f79-4900-a8fc-948f9fb38795"><script type="application/vnd.jupyter.widget-view+json">{"version_ma' + 'jor": 2, "version_minor": 0, "model_id": "311790751c8d46c29755b2175b007023"}<\/script></div>';
      // Set srcdoc of the iframe with embed widget HTML string. This trick allow to avoid disapearance of the iframe on page refresh
      var iframe = document.getElementById('chartframe_1ffdc891-0f79-4900-a8fc-948f9fb38795');
      iframe.srcdoc = embedwidget;
    });
  }
}
</script>