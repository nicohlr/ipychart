<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_26a0dccd-bdb4-4033-912a-7ea45082cc0f" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_26a0dccd-bdb4-4033-912a-7ea45082cc0f" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'pandas-polararea',
  data () {return {}},
  beforeMount: function () {
    this.$nextTick(function () {
      var iframe = document.getElementById('chartframe_26a0dccd-bdb4-4033-912a-7ea45082cc0f');
      fetch('../charts-examples/pandas-polararea.html').then(response => response.text()).then(data => iframe.srcdoc = data);
    });
  }
}
</script>
