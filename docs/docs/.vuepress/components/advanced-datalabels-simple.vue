<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_7fa9eae2-c76b-4776-983c-7a106afe080b" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_7fa9eae2-c76b-4776-983c-7a106afe080b" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'advanced-datalabels-simple',
  data () {return {}},
  beforeMount: function () {
    this.$nextTick(function () {
      var iframe = document.getElementById('chartframe_7fa9eae2-c76b-4776-983c-7a106afe080b');
      fetch('../charts-examples/advanced-datalabels-simple.html').then(response => response.text()).then(data => iframe.srcdoc = data);
    });
  }
}
</script>
