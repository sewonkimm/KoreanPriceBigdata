<template>
  <div class="cardContainer">
    <BookmarkGreen class="bookmark" />
    <img src="../../assets/warning.png" />

    <p class="name">
      양파
    </p>
    <div class="priceWrapper">
      <div class="priceTitle">
        현재가격
      </div>
      <div class="price">
        3,680원
      </div>
    </div>
    <div class="num">
      001
    </div>
  </div>
</template>

<script>
import '@/components/css/main/card.scss';
import { BookmarkGreen } from '@/assets/index.js';
export default {
  name: 'Card',
  components: {
    BookmarkGreen,
  },
};
</script>
