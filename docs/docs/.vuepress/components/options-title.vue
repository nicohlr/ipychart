<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_1bb5c1f9-6d7f-49cf-baed-242647e8eee2" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_1bb5c1f9-6d7f-49cf-baed-242647e8eee2" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {

  name: 'options-title',
  data () {return {}},

  beforeCreate: function () {
    this.$nextTick(function () {
      // Split embeded widget string into several strings to avoid JS "SyntaxError: unterminated string literal"
      let embedwidget = '<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js" integrity="sha2' + '56-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=" crossorigin="anonymous"><\/script><script data-jupy' + 'ter-widgets-cdn="https://cdn.jsdelivr.net/npm/" src="https://unpkg.com/@jupyter-widgets/html-manager' + '@*/dist/embed-amd.js" crossorigin="anonymous"><\/script><script type="application/vnd.jupyter.widget' + '-state+json">{"version_major": 2, "version_minor": 0, "state": {"115d8e5c5a9a43e68fbdb7a4dde84742": ' + '{"model_name": "LayoutModel", "model_module": "@jupyter-widgets/base", "model_module_version": "1.2.' + '0", "state": {"align_self": "stretch", "height": "auto"}}, "3e6a1aa8bc8f4b55916dc3370f241f7f": {"mod' + 'el_name": "ChartModel", "model_module": "ipychart", "model_module_version": "^0.1.0", "state": {"_da' + 'ta": {"labels": [1500, 1600, 1700, 1750, 1800, 1850, 1900, 1950, 1999, 2050], "datasets": [{"data": ' + '[86, 114, 106, 106, 107, 111, 133, 221, 783, 2478], "label": "Africa", "backgroundColor": "rgba(54, ' + '163, 235, 0.2)", "borderColor": "rgba(54, 163, 235, 1)", "borderWidth": 1, "datalabels": {"display":' + ' false}}, {"data": [282, 350, 411, 502, 635, 809, 947, 1402, 3700, 5267], "label": "Asia", "backgrou' + 'ndColor": "rgba(254, 119, 124, 0.2)", "borderColor": "rgba(254, 119, 124, 1)", "borderWidth": 1, "da' + 'talabels": {"display": false}}, {"data": [168, 170, 178, 190, 203, 276, 408, 547, 675, 734], "label"' + ': "Europe", "backgroundColor": "rgba(255, 206, 87, 0.2)", "borderColor": "rgba(255, 206, 87, 1)", "b' + 'orderWidth": 1, "datalabels": {"display": false}}, {"data": [40, 20, 10, 16, 24, 38, 74, 167, 508, 7' + '84], "label": "Latin America", "backgroundColor": "rgba(11, 255, 238, 0.2)", "borderColor": "rgba(11' + ', 255, 238, 1)", "borderWidth": 1, "datalabels": {"display": false}}, {"data": [6, 3, 2, 2, 7, 26, 8' + '2, 172, 312, 433], "label": "North America", "backgroundColor": "rgba(153, 102, 255, 0.2)", "borderC' + 'olor": "rgba(153, 102, 255, 1)", "borderWidth": 1, "datalabels": {"display": false}}]}, "_dom_classe' + 's": [], "_options": {"title": {"display": true, "text": "This is a Bar Chart", "fontSize": 30, "font' + 'Style": "normal"}, "scales": {"yAxes": [{"display": true, "ticks": {"beginAtZero": true, "display": ' + 'true}}], "xAxes": [{"display": true, "ticks": {"beginAtZero": true, "display": true}}]}}, "_type": "' + 'bar", "layout": "IPY_MODEL_115d8e5c5a9a43e68fbdb7a4dde84742"}}}}<\/script><div id="widgetcontainer_1' + 'bb5c1f9-6d7f-49cf-baed-242647e8eee2"><script type="application/vnd.jupyter.widget-view+json">{"versi' + 'on_major": 2, "version_minor": 0, "model_id": "3e6a1aa8bc8f4b55916dc3370f241f7f"}<\/script></div>';
      // Set srcdoc of the iframe with embed widget HTML string. This trick allow to avoid disapearance of the iframe on page refresh
      var iframe = document.getElementById('chartframe_1bb5c1f9-6d7f-49cf-baed-242647e8eee2');
      iframe.srcdoc = embedwidget;
    });
  }
}
</script>