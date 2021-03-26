<template>
  <div class="card">
    <BookmarkGreen class="bookmark" />
    <img src="../../assets/warning.png" />

    <p class="name">
      {{ item.name }}
    </p>
    <div class="priceWrapper">
      <div class="priceTitle">
        현재가격
      </div>
      <div class="price">{{ item.price }} 원</div>
    </div>
    <div class="num">
      {{ index }}
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
  props: {
    item: Object,
    index: Number,
  },
};
</script>
