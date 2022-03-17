<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_58104228-9be2-4f37-b9e1-736e592c3015" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_58104228-9be2-4f37-b9e1-736e592c3015" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'scales-gridlines',
  data () {return {}},
  beforeMount: function () {
    this.$nextTick(function () {
      var iframe = document.getElementById('chartframe_58104228-9be2-4f37-b9e1-736e592c3015');
      fetch('../charts-examples/scales-gridlines.html').then(response => response.text()).then(data => iframe.srcdoc = data);
    });
  }
}
</script>
