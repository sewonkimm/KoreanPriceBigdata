<template>
  <div class="CFRecommend">
    <h1 class="title">이런 상품은 어때요?</h1>
    <div class="cardContainer">
      <CFRecommendCard v-for="(item, index) in items" :key="index" :ingredient="item" />
    </div>
  </div>
</template>
<script>
import CFRecommendCard from './CFRecommendCard';

export default {
  name: 'CFRecommend',
  components: {
    CFRecommendCard,
  },
  data() {
    return {
      items: [
        {
          ingredientId: 1,
          ingredientName: '감자',
          ingredientCategory: '농산',
        },
        {
          ingredientId: 2,
          ingredientName: '고등어',
          ingredientCategory: '수산',
        },
        {
          ingredientId: 11,
          ingredientName: '쇠고기',
          ingredientCategory: '축산',
        },
      ],
    };
  },
};
</script>
