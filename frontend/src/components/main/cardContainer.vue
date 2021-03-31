<template>
  <div class="cardContainer" id="cardContainer"></div>
</template>
<script>
import { BookmarkGreen, Hot } from '@/assets/index.js';
import CMRotate from '@/components/main/CMRotate.js';

export default {
  name: 'CardContainer',
  data() {
    return {
      item: {
        ingredientId: 3,
        ingredientName: '배추',
        ingredientNameCode: '211',
        ingredientDetailName: null,
        ingredientDetailNameCode: null,
        ingredientCategory: '농산',
        ingredientAvg: {
          ingredientId: 3,
          ingredientAvgDate: '2021-03-19',
          ingredientAvgPrice: 3794,
          ingredientAvgPredictPrice: 0,
        },
        bookmark: BookmarkGreen,
        status: Hot,
      },
    };
  },
  methods: {
    makeCardList(num) {
      const cardList = [];
      for (let index = 0; index < num; index++) {
        cardList.push(this.item);
      }
      return cardList;
    },
  },
  created() {
    // this.$axios({
    //   url: '/ingredients/',
    //   method: 'GET',
    // })
    //   .then((response) => {
    //     this.item = JSON.parse(response.data);
    //     console.log(JSON.parse(response.data));
    //   })
    //   .catch((error) => {
    //     console.error(error);
    //   });
  },
  mounted() {
    const cardList = this.makeCardList(83);
    const clickCard = (no) => {
      alert('click no - ' + (no + 1));
    };
    const radius = window.innerHeight >= 900 ? 1400 : 1200;
    CMRotate.init('cardContainer', 240, 320, 700, 8, radius, cardList, clickCard);
  },
};
</script>
