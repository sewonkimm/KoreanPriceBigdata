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
import axios from 'axios';

export default {
  name: 'CFRecommend',
  components: {
    CFRecommendCard,
  },
  data() {
    return {
      items: [],
    };
  },
  methods: {
    getCFRecommand: function() {
      const instance = axios.create({
        baseURL: 'http://localhost:8000',
      });
      instance
        .get('/recommand/latent/' + this.$route.params.id)
        .then((response) => {
          console.log('추천');
          console.log(response);
          this.items = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getCFRecommand();
  },
};
</script>
