<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_86acc705-0ff5-4c46-9b59-51eb1559848b" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_86acc705-0ff5-4c46-9b59-51eb1559848b" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'chart-horizontalbar',
  data () {return {}},
  beforeCreate: function () {
    this.$nextTick(function () {
      // Split embeded widget string into several strings to avoid JS "SyntaxError: unterminated string literal"
      let embedwidget = '<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js" integrity="sha2' + '56-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=" crossorigin="anonymous"><\/script><script data-jupy' + 'ter-widgets-cdn="https://cdn.jsdelivr.net/npm/" src="https://unpkg.com/@jupyter-widgets/html-manager' + '@*/dist/embed-amd.js" crossorigin="anonymous"><\/script><script type="application/vnd.jupyter.widget' + '-state+json">{"version_major": 2, "version_minor": 0, "state": {"868c9cd0eec94f5aa26a41f14f18413d": ' + '{"model_name": "LayoutModel", "model_module": "@jupyter-widgets/base", "model_module_version": "1.2.' + '0", "state": {"align_self": "stretch", "height": "auto"}}, "73a25d2d00c642fe950db7cfa526fb26": {"mod' + 'el_name": "ChartModel", "model_module": "ipychart", "model_module_version": "^0.1.2", "state": {"_da' + 'ta": {"datasets": [{"label": "US", "data": [{"x": "01/01/2019", "y": 172}, {"x": "04/01/2019", "y": ' + '173}, {"x": "08/01/2019", "y": 174}, {"x": "10/01/2019", "y": 175}, {"x": "12/01/2019", "y": 178}, {' + '"x": "04/01/2020", "y": 182}, {"x": "10/01/2020", "y": 192}, {"x": "12/01/2020", "y": 200}], "fill":' + ' false}, {"label": "UK", "data": [{"x": "01/01/2019", "y": 175}, {"x": "04/01/2019", "y": 177}, {"x"' + ': "08/01/2019", "y": 182}, {"x": "10/01/2019", "y": 172}, {"x": "12/01/2019", "y": 184}, {"x": "04/0' + '1/2020", "y": 192}, {"x": "10/01/2020", "y": 188}, {"x": "12/01/2020", "y": 210}], "fill": false}]},' + ' "_dom_classes": [], "_options": {"scales": {"xAxes": [{"type": "time", "time": {"tooltipFormat": "l' + 'l", "unit": "week", "round": "week", "isoWeekday": true, "stepSize": 2, "displayFormats": {"week": "' + 'ddd D MMM YYYY"}}, "scaleLabel": {"display": true, "labelString": "Date"}}], "yAxes": [{"scaleLabel"' + ': {"display": true, "labelString": "Value"}}]}, "plugins": {"colorschemes": {"scheme": "tableau.Tabl' + 'eau10"}}}, "_type": "line", "layout": "IPY_MODEL_868c9cd0eec94f5aa26a41f14f18413d"}}}}<\/script><div' + ' id="widgetcontainer_86acc705-0ff5-4c46-9b59-51eb1559848b"><script type="application/vnd.jupyter.wid' + 'get-view+json">{"version_major": 2, "version_minor": 0, "model_id": "73a25d2d00c642fe950db7cfa526fb2' + '6"}<\/script></div>';
      // Set srcdoc of the iframe with embed widget HTML string. This trick allow to avoid disapearance of the iframe on page refresh
      var iframe = document.getElementById('chartframe_86acc705-0ff5-4c46-9b59-51eb1559848b');
      iframe.srcdoc = embedwidget;
    });
  }
}
</script>