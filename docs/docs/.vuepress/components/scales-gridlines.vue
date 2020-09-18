<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_58104228-9be2-4f37-b9e1-736e592c3015" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_58104228-9be2-4f37-b9e1-736e592c3015" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'chart-horizontalbar',
  data () {return {}},
  beforeCreate: function () {
    this.$nextTick(function () {
      // Split embeded widget string into several strings to avoid JS "SyntaxError: unterminated string literal"
      let embedwidget = '<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js" integrity="sha2' + '56-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=" crossorigin="anonymous"><\/script><script data-jupy' + 'ter-widgets-cdn="https://cdn.jsdelivr.net/npm/" src="https://unpkg.com/@jupyter-widgets/html-manager' + '@*/dist/embed-amd.js" crossorigin="anonymous"><\/script><script type="application/vnd.jupyter.widget' + '-state+json">{"version_major": 2, "version_minor": 0, "state": {"ee5da58f0a814219acfcc57db27497a5": ' + '{"model_name": "LayoutModel", "model_module": "@jupyter-widgets/base", "model_module_version": "1.2.' + '0", "state": {"align_self": "stretch", "height": "auto"}}, "b483768feb014ebca4b2349fe9281c3b": {"mod' + 'el_name": "ChartModel", "model_module": "ipychart", "model_module_version": "^0.2.1", "state": {"_da' + 'ta": {"labels": ["Germany", "Spain", "UK", "Italy", "Norway", "France", "Poland", "Portugal", "Swede' + 'n", "Ireland"], "datasets": [{"data": [14, 106, 16, 107, 45, 133, 19, 109, 60, 107], "label": "Datas' + 'et 1"}, {"data": [95, 28, 56, 82, 37, 155, 120, 132, 74, 85], "label": "Dataset 2"}]}, "_dom_classes' + '": [], "_zoom": true, "_options": {"scales": {"xAxes": [{"gridLines": {"display": true, "color": "black", "z": -1}}' + '], "yAxes": [{"gridLines": {"display": true, "color": "black", "z": -1}}]}, "plugins": {"colorscheme' + 's": {"scheme": "tableau.JewelBright9"}}}, "_type": "line", "layout": "IPY_MODEL_ee5da58f0a814219acfc' + 'c57db27497a5"}}}}<\/script><div id="widgetcontainer_58104228-9be2-4f37-b9e1-736e592c3015"><script ty' + 'pe="application/vnd.jupyter.widget-view+json">{"version_major": 2, "version_minor": 0, "model_id": "' + 'b483768feb014ebca4b2349fe9281c3b"}<\/script></div>';
      // Set srcdoc of the iframe with embed widget HTML string. This trick allow to avoid disapearance of the iframe on page refresh
      var iframe = document.getElementById('chartframe_58104228-9be2-4f37-b9e1-736e592c3015');
      iframe.srcdoc = embedwidget;
    });
  }
}
</script>