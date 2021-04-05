<template>
  <div class="currentPrice">
    <p class="title">
      현재 시세
    </p>
    <div class="priceContainer">
      <p class="price">{{ price | comma }}원</p>
      <div :class="{ range: 'range', up: isUp, down: !isUp }">
        <span v-if="isUp">+</span>
        <span v-else></span>
        {{ rangePrice | comma }} ({{ rangePercent }}%)
        <Up v-if="isUp" class="arrow" />
        <Down v-else class="arrow" />
      </div>
    </div>
    <div class="message">
      <Eyes />
      <p>오늘 {{ count | comma }}명의 사람들이 조회했어요!</p>
    </div>
  </div>
</template>
<script>
import '@/components/css/detail/priceComponent.scss';
import { Up, Down, Eyes } from '@/assets/index.js';

export default {
  name: 'CurrentPrice',
  components: {
    Up,
    Down,
    Eyes,
  },
  created() {
    this.ingredientId = this.$route.params.id;

    this.getIngredientPrice(this.ingredientId);
    this.getIngredientPriceInterval(this.ingredientId);
    this.getIngredientPriceRate(this.ingredientId);
    this.getIngredientWatchs(this.ingredientId);
  },
  data() {
    return {
      price: '', // 현재가격
      rangePrice: '', // 등락 가격
      rangePercent: '', // 등락률
      isUp: false, // 상승, 하락에 따른 스타일 적용을 위한 state
      count: '',
      ingredientId: '',
    };
  },
  filters: {
    comma(val) {
      return String(val).replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    },
  },
  methods: {
    getIngredientPrice(ingredientId) {
      this.$axios({
        url: '/ingredientAvg/price/' + ingredientId,
        method: 'GET',
      })
        .then((response) => {
          this.price = response.data;
        })
        .catch(() => {});
    },
    getIngredientPriceInterval(ingredientId) {
      this.$axios({
        url: '/ingredientAvg/price/interval/' + ingredientId,
        method: 'GET',
      })
        .then((response) => {
          this.rangePrice = response.data;
        })
        .catch(() => {});
    },
    getIngredientPriceRate(ingredientId) {
      this.$axios({
        url: '/ingredientAvg/rate/' + ingredientId,
        method: 'GET',
      })
        .then((response) => {
          this.rangePercent = response.data;
          if (this.rangePercent > 0) {
            this.isUp = true;
          }
        })
        .catch(() => {});
    },
    getIngredientWatchs(ingredientId) {
      this.$axios({
        url: '/watches/' + ingredientId,
        method: 'GET',
      })
        .then((response) => {
          this.count = response.data;
        })
        .catch(() => {});
    },
  },
};
</script>
