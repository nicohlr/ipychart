<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_775c8afe-c418-4158-b5f4-345eb6557a20" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_775c8afe-c418-4158-b5f4-345eb6557a20" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'pandas-scatter',
  data () {return {}},
  beforeMount: function () {
    this.$nextTick(function () {
      var iframe = document.getElementById('chartframe_775c8afe-c418-4158-b5f4-345eb6557a20');
      fetch('../charts-examples/pandas-scatter.html').then(response => response.text()).then(data => iframe.srcdoc = data);
    });
  }
}
</script>
