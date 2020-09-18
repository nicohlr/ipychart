<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_26a0dccd-bdb4-4033-912a-7ea45082cc0f" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_26a0dccd-bdb4-4033-912a-7ea45082cc0f" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'chart-horizontalbar',
  data () {return {}},
  beforeCreate: function () {
    this.$nextTick(function () {
      // Split embeded widget string into several strings to avoid JS "SyntaxError: unterminated string literal"
      let embedwidget = '<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js" integrity="sha2' + '56-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=" crossorigin="anonymous"><\/script><script data-jupy' + 'ter-widgets-cdn="https://cdn.jsdelivr.net/npm/" src="https://unpkg.com/@jupyter-widgets/html-manager' + '@*/dist/embed-amd.js" crossorigin="anonymous"><\/script><script type="application/vnd.jupyter.widget' + '-state+json">{"version_major": 2, "version_minor": 0, "state": {"3d7ed44a4132488cb063f3d8972e3871": ' + '{"model_name": "LayoutModel", "model_module": "@jupyter-widgets/base", "model_module_version": "1.2.' + '0", "state": {"align_self": "stretch", "height": "auto"}}, "42bccf99b3924dba973d49926461b392": {"mod' + 'el_name": "ChartModel", "model_module": "ipychart", "model_module_version": "^0.2.1", "state": {"_da' + 'ta": {"datasets": [{"data": [34.7031, 43.8001, 24.4416, 45.3303, 37.1697]}], "labels": ["Rare", "Mas' + 'ter", "Mrs", "Mr", "Miss"]}, "_dom_classes": [], "_zoom": false, "_options": {"plugins": {"colorschemes": {"scheme":' + ' "brewer.SetThree5"}}, "scale": {"ticks": {"beginAtZero": true}}}, "_type": "polarArea", "layout": "' + 'IPY_MODEL_3d7ed44a4132488cb063f3d8972e3871"}}}}<\/script><div id="widgetcontainer_26a0dccd-bdb4-4033' + '-912a-7ea45082cc0f"><script type="application/vnd.jupyter.widget-view+json">{"version_major": 2, "ve' + 'rsion_minor": 0, "model_id": "42bccf99b3924dba973d49926461b392"}<\/script></div>';
      // Set srcdoc of the iframe with embed widget HTML string. This trick allow to avoid disapearance of the iframe on page refresh
      var iframe = document.getElementById('chartframe_26a0dccd-bdb4-4033-912a-7ea45082cc0f');
      iframe.srcdoc = embedwidget;
    });
  }
}
</script>