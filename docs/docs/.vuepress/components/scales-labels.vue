<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_cddffda8-84b9-407d-be39-8a31598ea22c" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_cddffda8-84b9-407d-be39-8a31598ea22c" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'scales-labels',
  data () {return {}},
  beforeMount: function () {
    this.$nextTick(function () {
      var iframe = document.getElementById('chartframe_cddffda8-84b9-407d-be39-8a31598ea22c');
      fetch('../charts-examples/scales-labels.html').then(response => response.text()).then(data => iframe.srcdoc = data);
    });
  }
}
</script>
