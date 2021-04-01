<template>
  <div class="currentPrice">
    <p class="title">
      현재 시세
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
    <div class="counter">
      <Eyes />
      <p>오늘 {{ count | comma }}명의 사람들이 조회했어요!</p>
    </div>
  </div>
</template>
<script>
import '@/components/css/detail/currentPrice.scss';
import { Up, Down, Eyes } from '@/assets/index.js';

export default {
  name: 'CurrentPrice',
  components: {
    Up,
    Down,
    Eyes,
  },
  data() {
    return {
      price: 2300, // 현재가격
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
