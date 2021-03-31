<script>
import { Line } from 'vue-chartjs';
import '@/components/css/detail/style.scss';
export default {
  extends: Line,
  data: () => ({
    chartdata: {
      labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
      datasets: [
        {
          label: '가격 그래프',
          borderColor: '#FF9551',
          pointBackgroundColor: '#FF9551',
          backgroundColor: 'transparent',
          data: [40, 20, 30, 50, 12, 10, 40, 20, 40, 20, 25, 15],
          fill: false,
        },
        {
          label: '가격 예측 그래프',
          borderColor: ' #78D0FF',
          pointBackgroundColor: '#78D0FF',
          backgroundColor: 'transparent',
          data: [10, 40, 30, 40, 20, 25, 20, 30, 50, 12, 40, 40],
          fill: false,
        },
      ],
    },
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
              labelString: '월',
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

  mounted() {
    this.renderChart(this.chartdata, this.options);
  },
};
</script>
