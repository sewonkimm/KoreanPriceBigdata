<script>
import { Line } from 'vue-chartjs';
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
          borderColor: '#FF9551',
          pointBackgroundColor: '#FF9551',
          backgroundColor: 'transparent',
          data: [],
          pointRadius: 0,
          borderWidth: 1,
          fill: false,
        },
        {
          label: '가격 예측 그래프',
          borderColor: ' #78D0FF',
          pointBackgroundColor: '#78D0FF',
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
              labelString: '단위: 천원',
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
    this.renderChart(this.chartdata, this.options);
  },
};
</script>
