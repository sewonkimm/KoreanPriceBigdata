<script>
import { Line } from 'vue-chartjs';
import zoom from 'chartjs-plugin-zoom';
export default {
  extends: Line,
  created() {
    this.ingredientId = this.$route.params.id;

    this.getIngredientPriceYear(this.ingredientId);
  },
  data: () => ({
    chartdata: {
      labels: [],
      items: [],
      datasets: [
        {
          label: '가격 그래프',
          borderColor: 'rgb(229, 85, 114)',
          pointBackgroundColor: 'rgb(229, 85, 114)',
          backgroundColor: 'transparent',
          data: [],
          pointRadius: 0,
          borderWidth: 1,
          fill: false,
        },
        {
          label: '가격 예측 그래프',
          borderColor: ' rgb(72, 140, 222)',
          pointBackgroundColor: 'rgb(229, 85, 114)',
          backgroundColor: 'transparent',
          data: [],
          pointRadius: 0,
          borderWidth: 1,
          fill: false,
        },
      ],
    },
    ingredientId: '',
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        zoom: {
          zoom: {
            enabled: true,
            mode: 'x',
          },
        },
      },
      scales: {
        xAxes: [
          {
            gridLines: {
              // display: false,
              color: 'lightgray',
              borderDash: [2, 5],
            },
            scaleLabel: {
              display: true,
              labelString: '일',
              fontColor: 'red',
            },
          },
        ],
        yAxes: [
          {
            gridLines: {
              color: 'lightgray',
              borderDash: [2, 5],
            },
            scaleLabel: {
              display: true,
              labelString: '단위: 원',
              fontColor: 'green',
            },
          },
        ],
      },
    },
  }),
  methods: {
    getIngredientPriceYear(ingredientId) {
      this.$axios({
        url: '/transition/' + ingredientId,
        method: 'GET',
      })
        .then((response) => {
          this.items = response.data;

          this.chartdata.labels = this.items.map((item) => {
            item = item.ingredientAvgDate;
            return item;
          });
          this.chartdata.datasets[0].data = this.items.map((price) => {
            price = price.ingredientAvgPrice;
            return price;
          });
          this.chartdata.datasets[1].data = this.items.map((PredictPrice) => {
            PredictPrice = PredictPrice.ingredientAvgPredictPrice;
            return PredictPrice;
          });
        })
        .catch(() => {});
    },
  },
  mounted() {
    this.addPlugin(zoom);
    this.renderChart(this.chartdata, this.options);
  },
};
</script>
