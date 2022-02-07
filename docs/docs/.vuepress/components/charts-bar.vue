<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_e3e28d41-8c74-4e79-881e-cf0a4b1acd7d" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_e3e28d41-8c74-4e79-881e-cf0a4b1acd7d" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'chart-bar',
  data () {return {}},
  beforeMount: function () {
    this.$nextTick(function () {
      var iframe = document.getElementById('chartframe_e3e28d41-8c74-4e79-881e-cf0a4b1acd7d');
      fetch('../charts-examples/chart-bar.html').then(response => response.text()).then(data => iframe.srcdoc = data);
    });
  }
}
</script>
