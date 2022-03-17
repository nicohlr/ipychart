<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_1ffdc891-0f79-4900-a8fc-948f9fb38795" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_1ffdc891-0f79-4900-a8fc-948f9fb38795" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'pandas-line',
  data () {return {}},
  beforeMount: function () {
    this.$nextTick(function () {
      var iframe = document.getElementById('chartframe_1ffdc891-0f79-4900-a8fc-948f9fb38795');
      fetch('../charts-examples/pandas-line.html').then(response => response.text()).then(data => iframe.srcdoc = data);
    });
  }
}
</script>
