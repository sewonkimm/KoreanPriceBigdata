<template>
  <div class="cardContainer" id="cardContainer"></div>
</template>
<script>
import { Login } from '@/assets/index.js';
import CMRotate from '@/components/main/CMRotate.js';

export default {
  name: 'CardContainer',
  data() {
    return {
      item: [],
      //   item: {
      //     ingredientId: 3,
      //     ingredientName: '배추',
      //     ingredientNameCode: '211',
      //     ingredientDetailName: null,
      //     ingredientDetailNameCode: null,
      //     ingredientCategory: '농산',
      //     ingredientAvg: {
      //       ingredientId: 3,
      //       ingredientAvgDate: '2021-03-19',
      //       ingredientAvgPrice: 3794,
      //       ingredientAvgPredictPrice: 0,
      //     },
      //     bookmark: BookmarkGreen,
      //     status: Hot,
      //   },
    };
  },
  methods: {
    callIngredients() {
      // 비로그인시 전체 목록 조회
      this.$axios({
        url: '/ingredients/',
        method: 'GET',
      })
        .then((response) => {
          this.item = response.data.map((item) => {
            item.ingredientAvg.ingredientAvgPrice = item.ingredientAvg.ingredientAvgPrice
              .toString()
              .replace(/\B(?<!\.\d*)(?=(\d{3})+(?!\d))/g, ',');
            return item;
          });

          if (this.$store.state.userId === '') {
            this.addLoginCard();
          }
          this.renderCards(this.item);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    renderCards(items) {
      // api로 불러온 목록을 card로 그리기(카드의 개수는 최소 13개)
      const clickCard = (no) => {
        alert('click no - ' + (no + 1));
      };
      const radius = window.innerHeight >= 900 ? 1400 : 1200;
      CMRotate.init('cardContainer', 240, 320, 700, 8, radius, items, clickCard);
    },
    addLoginCard() {
      // 로그인 카드 추가
      const loginCard = {
        ingredientId: -1,
        title: '로그인',
        status: Login,
      };
      for (let index = 0; index < 12; index++) {
        this.item.push(loginCard);
      }
    },
  },
  created() {
    this.callIngredients();
  },
};
</script>
