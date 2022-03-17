<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_6eb84199-9a39-4448-87a3-ae3d6c8ffd92" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_6eb84199-9a39-4448-87a3-ae3d6c8ffd92" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'chart-mixed',
  data () {return {}},
  beforeMount: function () {
    this.$nextTick(function () {
      var iframe = document.getElementById('chartframe_6eb84199-9a39-4448-87a3-ae3d6c8ffd92');
      fetch('../charts-examples/chart-mixed.html').then(response => response.text()).then(data => iframe.srcdoc = data);
    });
  }
}
</script>
