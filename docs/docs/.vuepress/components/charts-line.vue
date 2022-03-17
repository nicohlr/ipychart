<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_de800071-2b7e-4409-bd0b-80bccda321cf" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_de800071-2b7e-4409-bd0b-80bccda321cf" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'chart-line',
  data () {return {}},
  beforeMount: function () {
    this.$nextTick(function () {
      var iframe = document.getElementById('chartframe_de800071-2b7e-4409-bd0b-80bccda321cf');
      fetch('../charts-examples/chart-line.html').then(response => response.text()).then(data => iframe.srcdoc = data);
    });
  }
}
</script>
