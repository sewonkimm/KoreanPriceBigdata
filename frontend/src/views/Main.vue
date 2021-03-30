<template>
  <div class="main">
    <!-- 배경 그라데이션을 위한 div -->
    <div class="background" />

    <!-- 커서 -->
    <div class="cursor" id="cursor" />

    <!-- 로고 -->
    <div class="logo">
      <Logo />
    </div>

    <!-- 로그인 -->
    <div id="login">
      <router-link to="/login">로그인</router-link>
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
import { Logo } from '@/assets/index.js';
// import CMRotate from '@/components/main/CMRotate.js';

export default {
  name: 'Main',
  components: {
    Logo,
  },
  data() {
    return {
      item: [],
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
    this.$axios({
      url: '/ingredients',
      method: 'GET',
    })
      .then((response) => {
        this.item = response.data;
      })
      .catch(() => {});
  },
  mounted() {
    console.log('mounted');
    console.log(this.item);
    // const cardList = this.makeCardList(83);
    // const clickCard = (no) => {
    //   alert('click no - ' + (no + 1));
    // };
    // const radius = window.innerHeight >= 900 ? 1400 : 1200;
    // CMRotate.init('cardContainer', 240, 320, 700, 8, radius, this.item, clickCard);
  },
};
</script>
