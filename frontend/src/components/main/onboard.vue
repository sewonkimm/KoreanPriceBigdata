<template>
  <div class="onboard">
    <img src="@/assets/logoWname2.png" class="logo" />
    <div v-show="page === 1" class="page">
      <OnboardImg1 />
      <div class="textContainer">
        <h1>똑똑하게 살림하세요!</h1>
        <p>
          혹시 지금 당근<img src="@/assets/carrot.png" />이 얼마인지 아시나요?
          <br />
          물가를 모르면 평소보다 비싸더라도
          <br />
          잘 모르고 사게 됩니다.
        </p>
        <v-btn color="#608F58" large class="nextButton" width="634" height="100" @click="nextPage">
          농수산물 물가, 이젠 쉽게 알 수 있습니다!
        </v-btn>
      </div>
    </div>

    <div v-show="page === 2" class="page">
      <OnboardImg1 />
      <div class="textContainer">
        <h1>농수산물 물가를 한눈에!</h1>
        <p>
          가장 많은 관심을 받고 있는 83가지의
          <br />
          농수산물을 인기순으로 조회할 수 있어요.
        </p>
        <v-btn color="#4B6EB2" large class="nextButton" width="634" height="100" @click="nextPage">
          상세정보를 알고싶다면? 클릭!
        </v-btn>
      </div>
    </div>

    <div v-show="page === 3" class="page">
      <OnboardImg1 />
      <div class="textContainer">
        <h1>빅데이터로 정확하게!</h1>
        <p>
          혹시 지금 당근<img src="@/assets/carrot.png" />이 얼마인지 아시나요?
          <br />
          물가를 모르면 평소보다 비싸더라도
          <br />
          잘 모르고 사게 됩니다.
        </p>
        <v-btn
          color="#D73F32"
          large
          class="nextButton"
          width="634"
          height="100"
          @click="endOnboard"
        >
          장보러 가기
        </v-btn>
      </div>
    </div>
  </div>
</template>
<script>
import '@/components/css/main/onbaord.scss';
import { OnboardImg1 } from '@/assets/index.js';

export default {
  name: 'Onboard',
  components: {
    OnboardImg1,
  },
  data() {
    return {
      page: 1,
    };
  },
  methods: {
    nextPage() {
      // 다음 온보딩 페이지로 이동
      this.page += 1;
    },
    endOnboard() {
      // 온보딩 페이지 끝
      this.$emit('endOnboard');
    },
  },
};
</script>
