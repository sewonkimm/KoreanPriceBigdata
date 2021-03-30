<script>
import { HorizontalBar } from 'vue-chartjs';

export default {
  name: 'PopularRecommend',
  extends: HorizontalBar,
  data() {
    return {
      chartdata: {
        labels: ['양파', '대파', '연어', '김치', '닭가슴살'],
        datasets: [
          {
            label: '인기도',
            data: [30, 26, 22, 16, 10],
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
  mounted() {
    this.renderChart(this.chartdata, this.options);
  },
};
</script>
