<template>
  <div class="currentPrice">
    <p class="title">
      3일 후 예측 가격
    </p>
    <div class="priceContainer">
      <p class="price">{{ price | comma }}원</p>
      <div :class="{ range: 'range', up: isUp, down: !isUp }">
        <span v-if="isUp">+</span>
        <span v-else>-</span>
        {{ rangePrice | comma }} ({{ rangePercent }}%)
        <Up v-if="isUp" class="arrow" />
        <Down v-else class="arrow" />
      </div>
    </div>

    <div class="message">
      <p v-if="isUp">
        오늘보다 비싸질 것 같아요.<br />
        빨리 구매해야겠어요!
      </p>
      <p v-else>
        오늘보다 저렴해질 것 같아요.<br />
        조금 더 있다 구매하는 건 어떠세요?
      </p>
    </div>
  </div>
</template>
<script>
import '@/components/css/detail/priceComponent.scss';
import { Up, Down } from '@/assets/index.js';

export default {
  name: 'PredictPrice',
  components: {
    Up,
    Down,
  },
  data() {
    return {
      price: 1100, // 예측가격
      rangePrice: 1200, // 등락 가격
      rangePercent: 0.8, // 등락률
      isUp: false, // 상승, 하락에 따른 스타일 적용을 위한 state
      count: 1390,
    };
  },
  filters: {
    comma(val) {
      return String(val).replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    },
  },
};
</script>
