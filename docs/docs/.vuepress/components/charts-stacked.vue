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
      let embedwidget = '<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js" integrity="sha2' + '56-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=" crossorigin="anonymous"><\/script><script data-jupy' + 'ter-widgets-cdn="https://cdn.jsdelivr.net/npm/" src="https://unpkg.com/@jupyter-widgets/html-manager' + '@*/dist/embed-amd.js" crossorigin="anonymous"><\/script><script type="application/vnd.jupyter.widget' + '-state+json">{"version_major": 2, "version_minor": 0, "state": {"b09dd316f13f4db88609e34ba9fb8392": ' + '{"model_name": "LayoutModel", "model_module": "@jupyter-widgets/base", "model_module_version": "1.2.' + '0", "state": {"align_self": "stretch", "height": "auto"}}, "e8c15d7e9921490c8777e60bcd8551db": {"mod' + 'el_name": "ChartModel", "model_module": "ipychart", "model_module_version": "^0.1.1", "state": {"_da' + 'ta": {"labels": ["Dataset 1", "Dataset 2", "Dataset 3"], "datasets": [{"data": [221, 783, 2478], "la' + 'bel": "Africa", "fill": false, "datalabels": {"display": false}}, {"data": [1402, 3700, 5267], "labe' + 'l": "Asia", "fill": false, "datalabels": {"display": false}}, {"data": [547, 675, 734], "label": "Eu' + 'rope", "fill": false, "datalabels": {"display": false}}, {"data": [167, 508, 784], "label": "Latin A' + 'merica", "fill": false, "datalabels": {"display": false}}, {"data": [172, 312, 433], "label": "North' + ' America", "fill": false, "datalabels": {"display": false}}]}, "_dom_classes": [], "_options": {"sca' + 'les": {"xAxes": [{"stacked": true}], "yAxes": [{"stacked": true}]}, "plugins": {"colorschemes": {"sc' + 'heme": "tableau.Tableau20"}}}, "_type": "bar", "layout": "IPY_MODEL_b09dd316f13f4db88609e34ba9fb8392' + '"}}}}<\/script><div id="widgetcontainer_b0f70ec4-6c4b-4061-84e5-a9623c6a4026"><script type="applicat' + 'ion/vnd.jupyter.widget-view+json">{"version_major": 2, "version_minor": 0, "model_id": "e8c15d7e9921' + '490c8777e60bcd8551db"}<\/script></div>';
      // Set srcdoc of the iframe with embed widget HTML string. This trick allow to avoid disapearance of the iframe on page refresh
      var iframe = document.getElementById('chartframe_32603687-fb9a-4e25-8a24-179288388b67');
      iframe.srcdoc = embedwidget;
    });
  }
}
</script>