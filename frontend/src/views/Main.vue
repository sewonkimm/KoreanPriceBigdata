<template>
  <div class="main">
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
    <div class="cardContainer">
      <!-- data에서 n개 만큼 생성하여 테스트 -->
      <Card v-for="(item, index) in items(1)" :item="item" :index="index" :key="index" />
    </div>
  </div>
</template>
<script>
import '@/components/css/main/style.scss';
import { Logo } from '@/assets/index.js';
import Card from '@/components/main/card';

export default {
  name: 'Main',
  components: {
    Logo,
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
};
</script>
