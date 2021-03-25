<template>
  <div class="cardContainer">
    <div class="bookmarkWrapper">
      <BookmarkGreen />
    </div>
    <img src="../../assets/warning.png" class="characterWrapper" />

    <div class="nameWrapper">
      <p class="name">
        양파
      </p>
    </div>
    <div class="priceWrapper">
      <div class="curPrice">
        현재가격
      </div>
      <div class="price">
        3,680원
      </div>
    </div>
    <div class="numWrapper">
      <div class="num">
        001
      </div>
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
