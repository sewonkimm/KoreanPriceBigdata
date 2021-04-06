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
    <CardContainer />
  </div>
</template>
<script>
import '@/components/css/main/style.scss';
import '@/components/css/main/card.scss';
import { Logo } from '@/assets/index.js';
import CardContainer from '@/components/main/cardContainer';

export default {
  name: 'Main',
  components: {
    Logo,
    CardContainer,
  },
  created() {
    // 첫 방문인 경우 -> splash 화면으로 분기
    if (this.$store.state.splash) {
      this.$router.push({ name: 'Splash' });
    }
  },
};
</script>
