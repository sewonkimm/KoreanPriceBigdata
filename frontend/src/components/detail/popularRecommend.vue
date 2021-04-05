<script>
import { HorizontalBar } from 'vue-chartjs';

export default {
  name: 'PopularRecommend',
  extends: HorizontalBar,
  data() {
    return {
      id: [],
      chartdata: {
        labels: [],
        datasets: [
          {
            label: '인기도',
            data: [],
            barPercentage: 0.5,
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          xAxes: [
            {
              ticks: {
                beginAtZero: true,
              },
            },
          ],
        },
      },
    };
  },
  methods: {
    getPopularityRecommand: function() {
      this.$axios({
        url: '/popularity',
        method: 'GET',
      })
        .then((response) => {
          this.chartdata.labels = response.data.map((item) => {
            if (item.ingredientDetailName == null) {
              return item.ingredientName;
            } else {
              return item.ingredientDetailName;
            }
          });
          this.chartdata.datasets.data = response.data.map((item) => {
            return item.Popularity;
          });
          this.id = response.data.map((item) => {
            return item.ingredientId;
          });
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getPopularityRecommand();
  },
  mounted() {
    this.renderChart(this.chartdata, this.options);
  },
};
</script>
