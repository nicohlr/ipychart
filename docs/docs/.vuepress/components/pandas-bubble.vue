<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_2c688a39-7988-40eb-9f1d-251d33c0c4ae" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_2c688a39-7988-40eb-9f1d-251d33c0c4ae" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'pandas-bubble',
  data () {return {}},
  beforeMount: function () {
    this.$nextTick(function () {
      var iframe = document.getElementById('chartframe_2c688a39-7988-40eb-9f1d-251d33c0c4ae');
      fetch('../charts-examples/pandas-bubble.html').then(response => response.text()).then(data => iframe.srcdoc = data);
    });
  }
}
</script>
