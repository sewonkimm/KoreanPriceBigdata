<template>
  <div class="main">
    <!-- splash 화면 -->
    <Splash v-if="!showOnboard" />

    <!-- on boarding 화면 -->

    <!-- splash가 끝나면 main화면을 보여준다 -->
    <div v-show="showMain">
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
  </div>
</template>
<script>
import '@/components/css/main/style.scss';
import '@/components/css/main/card.scss';
import { Logo } from '@/assets/index.js';
import Splash from '@/components/main/splash';
import CardContainer from '@/components/main/cardContainer';

export default {
  name: 'Main',
  components: {
    Logo,
    Splash,
    CardContainer,
  },
  data() {
    return {
      showOnboard: false,
      showMain: false,
    };
  },
  methods: {
    startOnboarding() {
      this.showOnboard = true;
    },
  },
  mounted() {
    setTimeout(this.startOnboarding, 2500);
  },
};
</script>
