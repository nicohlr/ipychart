<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_fa18798a-6506-4932-8868-ed1858a3fe7a" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_fa18798a-6506-4932-8868-ed1858a3fe7a" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'chart-doughnut',
  data () {return {}},
  beforeMount: function () {
    this.$nextTick(function () {
      var iframe = document.getElementById('chartframe_fa18798a-6506-4932-8868-ed1858a3fe7a');
      fetch('../charts-examples/chart-doughnut.html').then(response => response.text()).then(data => iframe.srcdoc = data);
    });
  }
}
</script>
