<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <div id="chartframecontainer_002ef36d-09a5-4a76-9972-47e9ce608c4a" style="position:relative;width:99%;height:0;padding-bottom:51%;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" id="chartframe_002ef36d-09a5-4a76-9972-47e9ce608c4a" width="100%" frameborder="0"></iframe></div>
</template>

<script>
export default {
  name: 'chart-horizontalbar',
  data () {return {}},
  beforeCreate: function () {
    this.$nextTick(function () {
      // Split embeded widget string into several strings to avoid JS "SyntaxError: unterminated string literal"
      let embedwidget = '<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n' + '     <th>PassengerId</th>\n      <th>Survived</th>\n      <th>Pclass</th>\n      <th>Name</th>\n      <t' + 'h>Sex</th>\n      <th>Age</th>\n      <th>SibSp</th>\n      <th>Parch</th>\n      <th>Ticket</th>\n      ' + '<th>Fare</th>\n      <th>Cabin</th>\n      <th>Embarked</th>\n      <th>Title</th>\n    </tr>\n  </thead>' + '\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>1</td>\n      <td>0</td>\n      <td>3</td>\n      <td>Br' + 'aund, Mr. Owen Harris</td>\n      <td>male</td>\n      <td>22.0</td>\n      <td>1</td>\n      <td>0</td>' + '\n      <td>A/5 21171</td>\n      <td>7.2500</td>\n      <td>NaN</td>\n      <td>S</td>\n      <td>Mr</td' + '>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>2</td>\n      <td>1</td>\n      <td>1</td>\n      <td>C' + 'umings, Mrs. John Bradley (Florence Briggs Thayer)</td>\n      <td>female</td>\n      <td>38.0</td>\n  ' + '    <td>1</td>\n      <td>0</td>\n      <td>PC 17599</td>\n      <td>71.2833</td>\n      <td>C85</td>\n  ' + '    <td>C</td>\n      <td>Mrs</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>3</td>\n      <td>1</' + 'td>\n      <td>3</td>\n      <td>Heikkinen, Miss. Laina</td>\n      <td>female</td>\n      <td>26.0</td>' + '\n      <td>0</td>\n      <td>0</td>\n      <td>STON/O2. 3101282</td>\n      <td>7.9250</td>\n      <td>N' + 'aN</td>\n      <td>S</td>\n      <td>Miss</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>4</td>\n  ';
      // Set srcdoc of the iframe with embed widget HTML string. This trick allow to avoid disapearance of the iframe on page refresh
      var iframe = document.getElementById('chartframe_002ef36d-09a5-4a76-9972-47e9ce608c4a');
      iframe.srcdoc = embedwidget;
    });
  }
}
</script>
