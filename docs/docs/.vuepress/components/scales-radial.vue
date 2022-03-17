<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_2de65b17-e026-48a3-a358-8d96603da380" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_2de65b17-e026-48a3-a358-8d96603da380" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'scales-radial',
  data () {return {}},
  beforeMount: function () {
    this.$nextTick(function () {
      var iframe = document.getElementById('chartframe_2de65b17-e026-48a3-a358-8d96603da380');
      fetch('../charts-examples/scales-radial.html').then(response => response.text()).then(data => iframe.srcdoc = data);
    });
  }
}
</script>
