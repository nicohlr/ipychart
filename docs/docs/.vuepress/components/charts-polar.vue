<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_df88306a-5d2f-43f2-bd7e-8620167c2780" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_df88306a-5d2f-43f2-bd7e-8620167c2780" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'chart-polar',
  data () {return {}},
  beforeMount: function () {
    this.$nextTick(function () {
      var iframe = document.getElementById('chartframe_df88306a-5d2f-43f2-bd7e-8620167c2780');
      fetch('../charts-examples/chart-polar.html').then(response => response.text()).then(data => iframe.srcdoc = data);
    });
  }
}
</script>
