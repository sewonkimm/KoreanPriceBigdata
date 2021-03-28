<template>
  <div class="main">
    <!-- 배경 그라데이션을 위한 div -->
    <div class="background" />

    <!-- 로고 -->
    <div class="logo">
      <Logo />
    </div>

    <!-- 검색창 -->
    <v-toolbar class="search">
      <v-text-field hide-details prepend-icon="mdi-magnify" single-line></v-text-field>
    </v-toolbar>

    <!-- 카드 컴포넌트 -->
    <div class="cardContainer" id="cardContainer"></div>
  </div>
</template>
<script>
import '@/components/css/main/style.scss';
import '@/components/css/main/card.scss';
import { Logo, Hot, BookmarkGreen } from '@/assets/index.js';
import CMRotate from '@/components/main/CMRotate.js';

export default {
  name: 'Main',
  components: {
    Logo,
  },
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
      console.log(this.item);
      const cardList = [];
      for (let index = 0; index < num; index++) {
        cardList.push(this.item);
      }
      return cardList;
    },
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
