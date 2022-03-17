<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_86acc705-0ff5-4c46-9b59-51eb1559848b" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_86acc705-0ff5-4c46-9b59-51eb1559848b" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'scales-time',
  data () {return {}},
  beforeMount: function () {
    this.$nextTick(function () {
      var iframe = document.getElementById('chartframe_86acc705-0ff5-4c46-9b59-51eb1559848b');
      fetch('../charts-examples/scales-time.html').then(response => response.text()).then(data => iframe.srcdoc = data);
    });
  }
}
</script>
