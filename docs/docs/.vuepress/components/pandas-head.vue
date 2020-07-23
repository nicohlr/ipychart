<template>
  <!-- Styling is used to dynamically adjust the height of the iframe (see: https://www.h3xed.com/web-development/how-to-make-a-responsive-100-width-youtube-iframe-embed) -->
  <table border="0" class="dataframe">
    <thead>
      <tr style="text-align: right;">
        <th></th>
        <th>PassengerId</th>
        <th>Survived</th>
        <th>Pclass</th>
        <th>Title</th>
        <th>Sex</th>
        <th>Age</th>
        <th>SibSp</th>
        <th>Parch</th>
        <th>Ticket</th>
        <th>Fare</th>
        <th>Cabin</th>
        <th>Embarked</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th>0</th>
        <td>1</td>
        <td>0</td>
        <td>3</td>
        <td>Mr</td>
        <td>male</td>
        <td>22.0</td>
        <td>1</td>
        <td>0</td>
        <td>A/5 21171</td>
        <td>7.2500</td>
        <td>NaN</td>
        <td>S</td>
      </tr>
      <tr>
        <th>1</th>
        <td>2</td>
        <td>1</td>
        <td>1</td>
        <td>Mrs</td>
        <td>female</td>
        <td>38.0</td>
        <td>1</td>
        <td>0</td>
        <td>PC 17599</td>
        <td>71.2833</td>
        <td>C85</td>
        <td>C</td>
      </tr>
      <tr>
        <th>2</th>
        <td>3</td>
        <td>1</td>
        <td>3</td>
        <td>Miss</td>
        <td>female</td>
        <td>26.0</td>
        <td>0</td>
        <td>0</td>
        <td>STON/O2. 3101282</td>
        <td>7.9250</td>
        <td>NaN</td>
        <td>S</td>
      </tr>
      <tr>
        <th>3</th>
        <td>4</td>
        <td>1</td>
        <td>1</td>
        <td>Mrs</td>
        <td>female</td>
        <td>35.0</td>
        <td>1</td>
        <td>0</td>
        <td>113803</td>
        <td>53.1000</td>
        <td>C123</td>
        <td>S</td>
      </tr>
      <tr>
        <th>4</th>
        <td>5</td>
        <td>0</td>
        <td>3</td>
        <td>Mr</td>
        <td>male</td>
        <td>35.0</td>
        <td>0</td>
        <td>0</td>
        <td>373450</td>
        <td>8.0500</td>
        <td>NaN</td>
        <td>S</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  name: 'chart-horizontalbar',
  data () {return {}},
}
</script>
