<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_4fc980a3-4fa4-414f-aa01-35b92d24d0c3" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_4fc980a3-4fa4-414f-aa01-35b92d24d0c3" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'chart-horizontalbar',
  data () {return {}},
  beforeCreate: function () {
    this.$nextTick(function () {
      // Split embeded widget string into several strings to avoid JS "SyntaxError: unterminated string literal"
      let embedwidget = '<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js" integrity="sha2' + '56-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=" crossorigin="anonymous"><\/script><script data-jupy' + 'ter-widgets-cdn="https://cdn.jsdelivr.net/npm/" src="https://unpkg.com/@jupyter-widgets/html-manager' + '@*/dist/embed-amd.js" crossorigin="anonymous"><\/script><script type="application/vnd.jupyter.widget' + '-state+json">{"version_major": 2, "version_minor": 0, "state": {"957b1867454a4d1ebc3ecdb2d7591366": ' + '{"model_name": "LayoutModel", "model_module": "@jupyter-widgets/base", "model_module_version": "1.2.' + '0", "state": {"align_self": "stretch", "height": "auto"}}, "fe1da7db76d9409c93cd9584c0728860": {"mod' + 'el_name": "ChartModel", "model_module": "ipychart", "model_module_version": "^0.1.1", "state": {"_da' + 'ta": {"labels": ["Germany", "Spain", "UK", "Italy", "Norway", "France", "Poland", "Portugal", "Swede' + 'n", "Ireland"], "datasets": [{"data": [14, 106, 16, 107, 45, 133, 109, 109, 108, 107], "fill": true,' + ' "datalabels": {"display": false}}]}, "_dom_classes": [], "_options": {"plugins": {"colorschemes": {' + '"scheme": "brewer.PuOr3"}}, "scales": {"yAxes": [{"display": true, "ticks": {"beginAtZero": true, "d' + 'isplay": true}}], "xAxes": [{"display": true, "ticks": {"beginAtZero": true, "display": true}}]}, "l' + 'egend": false}, "_type": "line", "layout": "IPY_MODEL_957b1867454a4d1ebc3ecdb2d7591366"}}}}<\/script' + '><div id="widgetcontainer_cf10a53e-e9e5-4945-8537-cabaf2c092e9"><script type="application/vnd.jupyte' + 'r.widget-view+json">{"version_major": 2, "version_minor": 0, "model_id": "fe1da7db76d9409c93cd9584c0' + '728860"}<\/script></div>';
      // Set srcdoc of the iframe with embed widget HTML string. This trick allow to avoid disapearance of the iframe on page refresh
      var iframe = document.getElementById('chartframe_4fc980a3-4fa4-414f-aa01-35b92d24d0c3');
      iframe.srcdoc = embedwidget;
    });
  }
}
</script>