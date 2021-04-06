<template>
  <div class="CFRecommend">
    <h1 class="title">이런 상품은 어때요?</h1>
    <div class="cardContainer">
      <tbody class="table">
        <tr class="table">
          <CFRecommendCard v-for="(item, index) in itemsFirst" :key="index" :ingredient="item" />
        </tr>
        <tr class="table">
          <CFRecommendCard v-for="(item, index) in itemsSecond" :key="index" :ingredient="item" />
        </tr>
        <tr class="table">
          <CFRecommendCard v-for="(item, index) in itemsThird" :key="index" :ingredient="item" />
        </tr>
      </tbody>
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
      itemsFirst: [],
      itemsSecond: [],
      itemsThird: [],
    };
  },
  methods: {
    getCFRecommand: function() {
      const instance = axios.create({
        baseURL: 'http://j4a301.p.ssafy.io:8000',
      });
      instance
        .get('/cf/' + this.$store.state.userId)
        .then((response) => {
          this.itemsThird = response.data;
          this.itemsFirst = this.itemsThird.splice(0, 2);
          this.itemsSecond = this.itemsThird.splice(0, 2);
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
