<template>
  <div class="example-ipychart">
      <iframe sandbox="allow-scripts" srcdoc='

            <!-- Load require.js. Delete this if your page already loads require.js -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js" integrity="sha256-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=" crossorigin="anonymous"></script>
<script src="https://unpkg.com/@jupyter-widgets/html-manager@^0.18.0/dist/embed-amd.js" crossorigin="anonymous"></script>

<script type="application/vnd.jupyter.widget-state+json">
{
  "version_major": 2,
  "version_minor": 0,
  "state": {
    "fc09cfa645d44c979fdf8749c27f341e": {
      "model_name": "ChartModel",
      "model_module": "ipychart",
      "model_module_version": "^0.1.0",
      "state": {
        "_data": {
          "labels": [
            "Germany",
            "Spain",
            "UK",
            "Italy",
            "Norway",
            "France",
            "Poland",
            "Portugal",
            "Sweden",
            "Ireland"
          ],
          "datasets": [
            {
              "data": [
                114,
                106,
                106,
                107,
                111,
                133,
                109,
                109,
                108,
                107
              ],
              "backgroundColor": "rgba(255, 99, 132, 0.2)",
              "borderColor": "rgba(255, 99, 132, 1)",
              "borderWidth": 1
            }
          ]
        },
        "_dom_classes": [],
        "_options": {
          "title": {
            "display": true,
            "text": "Bar Chart",
            "fontSize": 22
          },
          "scales": {
            "xAxes": [
              {
                "ticks": {
                  "beginAtZero": true
                },
                "scaleLabel": {
                  "display": true,
                  "labelString": "Country",
                  "fontSize": 15
                }
              }
            ],
            "yAxes": [
              {
                "ticks": {
                  "beginAtZero": true
                },
                "scaleLabel": {
                  "display": true,
                  "labelString": "Count",
                  "fontSize": 15
                }
              }
            ]
          },
          "legend": false
        },
        "_type": "bar",
        "layout": "IPY_MODEL_c997cab92a094a46bcadab4cb99528a0"
      }
    },
    "c997cab92a094a46bcadab4cb99528a0": {
      "model_name": "LayoutModel",
      "model_module": "@jupyter-widgets/base",
      "model_module_version": "1.2.0",
      "state": {
        "align_self": "stretch",
        "height": "auto"
      }
    }
  }
}
</script>
<script type="application/vnd.jupyter.widget-view+json">
{"version_major": 2, "version_minor": 0, "model_id": "fc09cfa645d44c979fdf8749c27f341e"}
</script>


        '
      ></iframe>
  </div>
</template>

<script>
export default {
  name: 'getting-started',
  data() {return {}}
}
</script>