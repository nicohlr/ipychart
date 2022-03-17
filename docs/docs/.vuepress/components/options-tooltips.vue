<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_f400381d-8315-4cbd-9ef1-2df02cd1bf9f" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_f400381d-8315-4cbd-9ef1-2df02cd1bf9f" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'options-tooltips',
  data () {return {}},
  beforeMount: function () {
    this.$nextTick(function () {
      var iframe = document.getElementById('chartframe_f400381d-8315-4cbd-9ef1-2df02cd1bf9f');
      fetch('../charts-examples/options-tooltips.html').then(response => response.text()).then(data => iframe.srcdoc = data);
    });
  }
}
</script>
