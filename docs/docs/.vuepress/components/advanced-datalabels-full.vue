<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_6f9a025e-23c4-4774-984d-faa021fed844" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_6f9a025e-23c4-4774-984d-faa021fed844" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'advanced-datalabels-full',
  data () {return {}},
  beforeMount: function () {
    this.$nextTick(function () {
      var iframe = document.getElementById('chartframe_6f9a025e-23c4-4774-984d-faa021fed844');
      fetch('../charts-examples/advanced-datalabels-full.html').then(response => response.text()).then(data => iframe.srcdoc = data);
    });
  }
}
</script>
