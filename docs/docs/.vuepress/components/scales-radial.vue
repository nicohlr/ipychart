<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_2de65b17-e026-48a3-a358-8d96603da380" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_2de65b17-e026-48a3-a358-8d96603da380" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'scales-radial',
  data () {return {}},
  beforeMount: function () {
    this.$nextTick(function () {
      // Split embeded widget string into several strings to avoid JS "SyntaxError: unterminated string literal"
      let embedwidget = '<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js" integrity="sha2' + '56-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=" crossorigin="anonymous"><\/script><script data-jupy' + 'ter-widgets-cdn="https://cdn.jsdelivr.net/npm/" src="https://unpkg.com/@jupyter-widgets/html-manager' + '@*/dist/embed-amd.js" crossorigin="anonymous"><\/script><script type="application/vnd.jupyter.widget' + '-state+json">{"version_major": 2, "version_minor": 0, "state": {"841ce5dcd2e940ce8320fa60082dda2f": ' + '{"model_name": "LayoutModel", "model_module": "@jupyter-widgets/base", "model_module_version": "1.2.' + '0", "state": {"align_self": "stretch", "height": "auto"}}, "f845bbadffd6488ba375bacea5bb10af": {"mod' + 'el_name": "ChartModel", "model_module": "ipychart", "model_module_version": "^0.3.0", "state": {"_da' + 'ta_sync": {"labels": ["Top", "TopRight", "BottomRight", "Bottom", "BottomLeft", "TopLeft"], "datasets": [' + '{"data": [140, 106, 160, 107, 45, 27], "label": "Dataset 1", "borderWidth": 3, "lineTension": 0.3}, ' + '{"data": [32, 160, 72, 140, 89, 112], "label": "Dataset 2", "borderWidth": 3, "lineTension": 0.3}]},' + ' "_dom_classes": [], "_zoom_sync": false, "_options_sync": {"scale": {"angleLines": {"display": true, "color": "black", "lineW' + 'idth": 1.5, "borderDashOffset": 10}, "gridLines": {"color": "black", "lineWidth": 1.5, "circular": t' + 'rue}, "pointLabels": {"display": true, "fontColor": "black", "fontSize": 14, "fontStyle": "italic"},' + ' "ticks": {"fontSize": 18, "fontColor": "black", "stepSize": 30}}, "plugins": {"colorschemes": {"sch' + 'eme": "brewer.DarkTwo3"}}}, "_kind_sync": "radar", "layout": "IPY_MODEL_841ce5dcd2e940ce8320fa60082dda2f"' + '}}}}<\/script><div id="widgetcontainer_2de65b17-e026-48a3-a358-8d96603da380"><script type="applicati' + 'on/vnd.jupyter.widget-view+json">{"version_major": 2, "version_minor": 0, "model_id": "f845bbadffd64' + '88ba375bacea5bb10af"}<\/script></div>';
      // Set srcdoc of the iframe with embed widget HTML string. This trick allow to avoid disapearance of the iframe on page refresh
      var iframe = document.getElementById('chartframe_2de65b17-e026-48a3-a358-8d96603da380');
      iframe.srcdoc = embedwidget;
    });
  }
}
</script>
