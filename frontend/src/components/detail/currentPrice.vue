<template>
  <div class="currentPrice">
    <p class="title">
      현재 시세
      <v-tooltip top>
        <template v-slot:activator="{ on, attrs }">
          <v-icon v-bind="attrs" v-on="on">mdi-help-circle-outline</v-icon>
        </template>
        <span>지자체 농수축산물 물가 정보에 따른 현재 시세 입니다.</span>
      </v-tooltip>
    </p>
    <div class="priceContainer">
      <p class="price">{{ price | comma }}원</p>
      <p class="unit">({{ unit }})</p>
      <div :class="{ range: 'range', up: isUp, down: !isUp }">
        <span v-if="isUp">+</span>
        <span v-else></span>
        {{ rangePrice | comma }} ({{ rangePercent }}%)
        <Up v-if="isUp" class="arrow" />
        <Down v-else class="arrow" />
      </div>
    </div>
  </div>
</template>
<script>
import '@/components/css/detail/priceComponent.scss';
import { Up, Down } from '@/assets/index.js';

export default {
  name: 'CurrentPrice',
  components: {
    Up,
    Down,
  },
  mounted() {
    this.getIngredientPrice(this.ingredientId);
    this.getIngredientPriceInterval(this.ingredientId);
    this.getIngredientPriceRate(this.ingredientId);
  },
  data() {
    return {
      price: '', // 현재가격
      unit: '', // 단위
      rangePrice: '', // 등락 가격
      rangePercent: '', // 등락률
      isUp: false, // 상승, 하락에 따른 스타일 적용을 위한 state
      ingredientId: this.$route.params.id,
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
          this.price = response.data.ingredientAvgPrice;
          this.unit = response.data.ingredientUnit;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getIngredientPriceInterval(ingredientId) {
      this.$axios({
        url: '/ingredientAvg/price/interval/' + ingredientId,
        method: 'GET',
      })
        .then((response) => {
          this.rangePrice = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
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
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>
