<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_c9ef7af6-92db-494c-8a61-d3f0ac9af769" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_c9ef7af6-92db-494c-8a61-d3f0ac9af769" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'chart-bubble',
  data () {return {}},
  beforeMount: function () {
    this.$nextTick(function () {
      var iframe = document.getElementById('chartframe_c9ef7af6-92db-494c-8a61-d3f0ac9af769');
      fetch('../charts-examples/chart-bubble.html').then(response => response.text()).then(data => iframe.srcdoc = data);
    });
  }
}
</script>
