<template>
  <div class="card">
    <div class="bookMarkBar">
      <BookmarkGreen />
    </div>
    <img src="../../assets/warning.png" class="charBar" />

    <div class="nameBar">
      <p class="boldText">
        양파
      </p>
    </div>
    <div class="priceBar">
      <div class="pb-0">
        현재가격
      </div>
      <div class="priceText">
        3,680원
      </div>
    </div>
    <div class="numBar">
      <div class="numText">
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
