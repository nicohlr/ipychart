<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_e6ae8e63-25db-43ee-8051-d545f45a6fb3" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_e6ae8e63-25db-43ee-8051-d545f45a6fb3" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'pandas-count',
  data () {return {}},
  beforeMount: function () {
    this.$nextTick(function () {
      var iframe = document.getElementById('chartframe_e6ae8e63-25db-43ee-8051-d545f45a6fb3');
      fetch('../charts-examples/pandas-count.html').then(response => response.text()).then(data => iframe.srcdoc = data);
    });
  }
}
</script>
