<template>
  <div class="cardContainer" id="cardContainer"></div>
</template>
<script>
import { Login, BookmarkGreen, BookmarkBlue, BookmarkRed, Hot, Warning } from '@/assets/index.js';
import CMRotate from '@/components/main/CMRotate.js';

export default {
  name: 'CardContainer',
  data() {
    return {
      item: [],
    };
  },
  methods: {
    callIngredients() {
      // 비로그인시 전체 목록 조회
      this.$axios({
        url: '/ingredients/',
        method: 'GET',
      })
        .then((response) => {
          this.item = response.data.map((item) => {
            // 숫자 3자리 수에 맞춰 comma 표시
            item.ingredientAvg.ingredientAvgPrice = item.ingredientAvg.ingredientAvgPrice
              .toString()
              .replace(/\B(?<!\.\d*)(?=(\d{3})+(?!\d))/g, ',');

            // 상품 이미지 추가
            item.imageURL = `https://j4a301.p.ssafy.io/ingredients/ingredients_${item.ingredientId}.png`;

            // 유형에 따라 다른 색상으로 북마크 표시
            if (item.ingredientCategory === '농산') {
              item.bookmark = BookmarkGreen;
            } else if (item.ingredientCategory === '수산') {
              item.bookmark = BookmarkBlue;
            } else if (item.ingredientCategory === '축산') {
              item.bookmark = BookmarkRed;
            }

            // status 표시 (1: 인기상품, 2: 비추천상품)
            if (item.status === 1) {
              item.status = Hot;
            } else if (item.status === 2) {
              item.status = Warning;
            }
            return item;
          });

          if (this.$store.state.userId === '') {
            this.addLoginCard();
          }
          this.renderCards(this.item);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    renderCards(items) {
      // api로 불러온 목록을 card로 그리기(카드의 개수는 최소 13개)
      const clickCard = (id) => {
        this.$router.push({
          name: 'Detail',
          params: {
            id: id,
          },
        });
      };
      const radius = window.innerHeight >= 900 ? 1400 : 1200;
      CMRotate.init('cardContainer', 240, 320, 700, 8, radius, items, clickCard);
    },
    addLoginCard() {
      // 로그인 카드 추가
      const loginCard = {
        ingredientId: -1,
        title: '로그인',
        status: Login,
      };
      this.item.push(loginCard);
    },
  },
  created() {
    this.callIngredients();
  },
};
</script>
