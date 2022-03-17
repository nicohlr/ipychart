<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_1bb5c1f9-6d7f-49cf-baed-242647e8eee2" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_1bb5c1f9-6d7f-49cf-baed-242647e8eee2" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'options-title',
  data () {return {}},
  beforeMount: function () {
    this.$nextTick(function () {
      var iframe = document.getElementById('chartframe_1bb5c1f9-6d7f-49cf-baed-242647e8eee2');
      fetch('../charts-examples/options-title.html').then(response => response.text()).then(data => iframe.srcdoc = data);
    });
  }
}
</script>
