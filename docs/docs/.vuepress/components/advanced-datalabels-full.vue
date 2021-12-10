<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_6f9a025e-23c4-4774-984d-faa021fed844" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_6f9a025e-23c4-4774-984d-faa021fed844" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'advances-datalabels-full',
  data () {return {}},
  beforeMount: function () {
    this.$nextTick(function () {
      // Split embeded widget string into several strings to avoid JS "SyntaxError: unterminated string literal"
      let embedwidget = '<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js" integrity="sha2' + '56-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=" crossorigin="anonymous"><\/script><script data-jupy' + 'ter-widgets-cdn="https://cdn.jsdelivr.net/npm/" src="https://unpkg.com/@jupyter-widgets/html-manager' + '@*/dist/embed-amd.js" crossorigin="anonymous"><\/script><script type="application/vnd.jupyter.widget' + '-state+json">{"version_major": 2, "version_minor": 0, "state": {"a0b2697ab2344f159f91c7855453f492": ' + '{"model_name": "LayoutModel", "model_module": "@jupyter-widgets/base", "model_module_version": "1.2.' + '0", "state": {"align_self": "stretch", "height": "auto"}}, "c38b049e24084cb884da7463518d492f": {"mod' + 'el_name": "ChartModel", "model_module": "ipychart", "model_module_version": "^0.3.0", "state": {"_da' + 'ta_sync": {"labels": ["Label 1", "Label 2", "Label 3"], "datasets": [{"data": [221, 783, 2478], "label": "Af' + 'rica", "datalabels": {"display": true, "borderWidth": 1, "anchor": "end", "align": "end", "borderRad' + 'ius": 5, "color": "#fff"}}, {"data": [1402, 3700, 5267], "label": "Asia", "datalabels": {"display": ' + 'true, "borderWidth": 1, "anchor": "end", "align": "end", "borderRadius": 5, "color": "#fff"}}, {"dat' + 'a": [547, 675, 734], "label": "Europe", "datalabels": {"display": true, "borderWidth": 1, "anchor": ' + '"end", "align": "end", "borderRadius": 5, "color": "#fff"}}, {"data": [167, 508, 784], "label": "Lat' + 'in America", "datalabels": {"display": true, "borderWidth": 1, "anchor": "end", "align": "end", "bor' + 'derRadius": 5, "color": "#fff"}}, {"data": [172, 312, 433], "label": "North America", "datalabels": ' + '{"display": true, "borderWidth": 1, "anchor": "end", "align": "end", "borderRadius": 5, "color": "#f' + 'ff"}}]}, "_dom_classes": [], "_zoom_sync": true, "_options_sync": {"plugins": {"colorschemes": {"scheme": "tableau.Tableau10"' + '}}, "scales": {"yAxes": [{"display": true, "ticks": {"beginAtZero": true, "display": true}}], "xAxes' + '": [{"display": true, "ticks": {"beginAtZero": true, "display": true}}]}}, "_kind_sync": "bar", "layout":' + ' "IPY_MODEL_a0b2697ab2344f159f91c7855453f492"}}}}<\/script><div id="widgetcontainer"><script type="a' + 'pplication/vnd.jupyter.widget-view+json">{"version_major": 2, "version_minor": 0, "model_id": "c38b0' + '49e24084cb884da7463518d492f"}<\/script></div>';
      // Set srcdoc of the iframe with embed widget HTML string. This trick allow to avoid disapearance of the iframe on page refresh
      var iframe = document.getElementById('chartframe_6f9a025e-23c4-4774-984d-faa021fed844');
      iframe.srcdoc = embedwidget;
    });
  }
}
</script>
