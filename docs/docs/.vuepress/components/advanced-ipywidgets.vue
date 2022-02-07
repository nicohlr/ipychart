<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_3b258535-77fb-4276-95ff-6d2a036a3b10" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_3b258535-77fb-4276-95ff-6d2a036a3b10" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'advanced-ipywidgets',
  data () {return {}},
  beforeMount: function () {
    this.$nextTick(function () {
      var iframe = document.getElementById('chartframe_3b258535-77fb-4276-95ff-6d2a036a3b10');
      fetch('../charts-examples/advanced-ipywidgets.html').then(response => response.text()).then(data => iframe.srcdoc = data);
    });
  }
}
</script>
