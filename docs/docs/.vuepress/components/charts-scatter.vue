<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_1072a001-0de1-48a2-912b-7c5fcbd4a04b" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_1072a001-0de1-48a2-912b-7c5fcbd4a04b" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'chart-scatter',
  data () {return {}},
  beforeMount: function () {
    this.$nextTick(function () {
      var iframe = document.getElementById('chartframe_1072a001-0de1-48a2-912b-7c5fcbd4a04b');
      fetch('../charts-examples/chart-scatter.html').then(response => response.text()).then(data => iframe.srcdoc = data);
    });
  }
}
</script>
