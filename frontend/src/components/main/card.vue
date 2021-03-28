<template>
  <div class="card">
    <!-- <div class="circle"></div> -->
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
      {{ index + 1 }}
    </div>
  </div>
</template>
<script>
import '@/components/css/main/card.scss';
import { BookmarkGreen } from '@/assets/index.js';

const docStyle = document.documentElement.style;
document.addEventListener('mousemove', function(e) {
  docStyle.setProperty('--mouse-x', e.clientX);
  docStyle.setProperty('--mouse-y', e.clientY);
});

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
