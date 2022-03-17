<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_ec8f3a1c-80d7-4158-ab04-2752f92bac39" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_ec8f3a1c-80d7-4158-ab04-2752f92bac39" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'chart-radar',
  data () {return {}},
  beforeMount: function () {
    this.$nextTick(function () {
      var iframe = document.getElementById('chartframe_ec8f3a1c-80d7-4158-ab04-2752f92bac39');
      fetch('../charts-examples/chart-radar.html').then(response => response.text()).then(data => iframe.srcdoc = data);
    });
  }
}
</script>
