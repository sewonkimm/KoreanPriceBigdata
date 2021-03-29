<template>
  <div class="main">
<<<<<<< HEAD
=======
    <!-- 배경 그라데이션을 위한 div -->
    <div class="background" />

    <!-- 커서 -->
    <div class="cursor" id="cursor" />

>>>>>>> 4df971923c8d370e736444a62df9abdda52312a0
    <!-- 로고 -->
    <div class="logo">
      <Logo />
    </div>

<<<<<<< HEAD
=======
    <!-- 로그인 -->
    <div id="login">
      <router-link to="/login">로그인</router-link>
    </div>

>>>>>>> 4df971923c8d370e736444a62df9abdda52312a0
    <!-- 검색창 -->
    <v-toolbar class="search">
      <v-text-field hide-details prepend-icon="mdi-magnify" single-line></v-text-field>
    </v-toolbar>

    <!-- 카드 컴포넌트 -->
<<<<<<< HEAD
    <div class="cardContainer">
      <!-- data에서 n개 만큼 생성하여 테스트 -->
      <Card v-for="(item, index) in items(20)" :item="item" :index="index" :key="index" />
    </div>
=======
    <div class="cardContainer" id="cardContainer"></div>
>>>>>>> 4df971923c8d370e736444a62df9abdda52312a0
  </div>
</template>
<script>
import '@/components/css/main/style.scss';
<<<<<<< HEAD
import { Logo } from '@/assets/index.js';
import Card from '@/components/main/card';
=======
import '@/components/css/main/card.scss';
import { Logo, Hot, BookmarkGreen } from '@/assets/index.js';
import CMRotate from '@/components/main/CMRotate.js';
>>>>>>> 4df971923c8d370e736444a62df9abdda52312a0

export default {
  name: 'Main',
  components: {
    Logo,
<<<<<<< HEAD
    Card,
  },
  data() {
    return {
      items: function(n) {
        const item = {
          name: '양파',
          price: 3400,
          hot: false,
          warn: false,
          bookmark: false,
        };
        const list = [];
        for (let i = 0; i < n; i++) {
          list.push(item);
        }
        return list;
      },
    };
  },
=======
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
>>>>>>> 4df971923c8d370e736444a62df9abdda52312a0
};
</script>
