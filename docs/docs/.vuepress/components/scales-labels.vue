<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_cddffda8-84b9-407d-be39-8a31598ea22c" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_cddffda8-84b9-407d-be39-8a31598ea22c" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'scales-labels',
  data () {return {}},
  beforeMount: function () {
    this.$nextTick(function () {
      // Split embeded widget string into several strings to avoid JS "SyntaxError: unterminated string literal"
      let embedwidget = '<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js" integrity="sha2' + '56-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=" crossorigin="anonymous"><\/script><script data-jupy' + 'ter-widgets-cdn="https://cdn.jsdelivr.net/npm/" src="https://unpkg.com/@jupyter-widgets/html-manager' + '@*/dist/embed-amd.js" crossorigin="anonymous"><\/script><script type="application/vnd.jupyter.widget' + '-state+json">{"version_major": 2, "version_minor": 0, "state": {"5b41921c6dfd4d518b167db2c2e8afaf": ' + '{"model_name": "LayoutModel", "model_module": "@jupyter-widgets/base", "model_module_version": "1.2.' + '0", "state": {"align_self": "stretch", "height": "auto"}}, "b92b45f99d504c7c91c2613f068f680f": {"mod' + 'el_name": "ChartModel", "model_module": "ipychart", "model_module_version": "^0.3.0", "state": {"_da' + 'ta_sync": {"labels": ["Germany", "Spain", "UK", "Italy", "Norway", "France", "Poland", "Portugal", "Swede' + 'n", "Ireland"], "datasets": [{"data": [14, 106, 16, 107, 45, 133, 19, 109, 60, 107], "datalabels": {' + '"display": false}}]}, "_dom_classes": [], "_zoom_sync": true, "_options_sync": {"scales": {"xAxes": [{"scaleLabel": {"display' + '": true, "labelString": "This is the x Axis", "fontSize": 20}}], "yAxes": [{"scaleLabel": {"display"' + ': true, "labelString": "This is the y Axis", "fontSize": 20}}]}, "plugins": {"colorschemes": {"schem' + 'e": "office.Median6"}}, "legend": false}, "_kind_sync": "bar", "layout": "IPY_MODEL_5b41921c6dfd4d518b167' + 'db2c2e8afaf"}}}}<\/script><div id="widgetcontainer_24e523da-a6e3-4f39-9a91-714e0fe89873"><script typ' + 'e="application/vnd.jupyter.widget-view+json">{"version_major": 2, "version_minor": 0, "model_id": "b' + '92b45f99d504c7c91c2613f068f680f"}<\/script></div>';
      // Set srcdoc of the iframe with embed widget HTML string. This trick allow to avoid disapearance of the iframe on page refresh
      var iframe = document.getElementById('chartframe_cddffda8-84b9-407d-be39-8a31598ea22c');
      iframe.srcdoc = embedwidget;
    });
  }
}
</script>
