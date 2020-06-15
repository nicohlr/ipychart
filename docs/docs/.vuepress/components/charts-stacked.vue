<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_32603687-fb9a-4e25-8a24-179288388b67" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_32603687-fb9a-4e25-8a24-179288388b67" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'chart-horizontalbar',
  data () {return {}},
  beforeCreate: function () {
    this.$nextTick(function () {
      // Split embeded widget string into several strings to avoid JS "SyntaxError: unterminated string literal"
      let embedwidget = '<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js" integrity="sha2' + '56-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=" crossorigin="anonymous"><\/script><script data-jupy' + 'ter-widgets-cdn="https://cdn.jsdelivr.net/npm/" src="https://unpkg.com/@jupyter-widgets/html-manager' + '@*/dist/embed-amd.js" crossorigin="anonymous"><\/script><script type="application/vnd.jupyter.widget' + '-state+json">{"version_major": 2, "version_minor": 0, "state": {"d8e9f0231bc340d09fbd3461b1621df1": ' + '{"model_name": "LayoutModel", "model_module": "@jupyter-widgets/base", "model_module_version": "1.2.' + '0", "state": {"align_self": "stretch", "height": "auto"}}, "daa29787dcef43c4a4f8d7ce4846202e": {"mod' + 'el_name": "ChartModel", "model_module": "ipychart", "model_module_version": "^0.1.0", "state": {"_da' + 'ta": {"labels": ["Dataset 1", "Dataset 2", "Dataset 3"], "datasets": [{"data": [221, 783, 2478], "la' + 'bel": "Africa", "fill": false, "backgroundColor": "rgba(255, 99, 132, 0.2)", "borderColor": "rgba(25' + '5, 99, 132, 1)", "borderWidth": 1}, {"data": [1402, 3700, 5267], "label": "Asia", "fill": false, "ba' + 'ckgroundColor": "rgba(54, 162, 235, 0.2)", "borderColor": "rgba(54, 162, 235, 1)", "borderWidth": 1}' + ', {"data": [547, 675, 734], "label": "Europe", "fill": false, "backgroundColor": "rgba(255, 206, 86,' + ' 0.2)", "borderColor": "rgba(255, 206, 86, 1)", "borderWidth": 1}, {"data": [167, 508, 784], "label"' + ': "Latin America", "fill": false, "backgroundColor": "rgba(75, 192, 192, 0.2)", "borderColor": "rgba' + '(75, 192, 192, 1)", "borderWidth": 1}, {"data": [172, 312, 433], "label": "North America", "fill": f' + 'alse, "backgroundColor": "rgba(153, 102, 255, 0.2)", "borderColor": "rgba(153, 102, 255, 1)", "borde' + 'rWidth": 1}]}, "_dom_classes": [], "_options": {"scales": {"xAxes": [{"stacked": true}], "yAxes": [{' + '"stacked": true}]}}, "_type": "bar", "layout": "IPY_MODEL_d8e9f0231bc340d09fbd3461b1621df1"}}}}<\/sc' + 'ript><div id="widgetcontainer_3d1becc0-43e8-46ae-8686-59c64f46730d"><script type="application/vnd.ju' + 'pyter.widget-view+json">{"version_major": 2, "version_minor": 0, "model_id": "daa29787dcef43c4a4f8d7' + 'ce4846202e"}<\/script></div>';
      // Set srcdoc of the iframe with embed widget HTML string. This trick allow to avoid disapearance of the iframe on page refresh
      var iframe = document.getElementById('chartframe_32603687-fb9a-4e25-8a24-179288388b67');
      iframe.srcdoc = embedwidget;
    });
  }
}
</script>