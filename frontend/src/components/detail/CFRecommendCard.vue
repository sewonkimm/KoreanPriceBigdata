<template>
  <td class="table">
    <div :class="['CFRecommendCard', 'border', ingredient.ingredientCategory]">
      <GreenIcon v-if="ingredient.ingredientCategory === '농산'" class="icon" />
      <BlueIcon v-if="ingredient.ingredientCategory === '수산'" class="icon" />
      <RedIcon v-if="ingredient.ingredientCategory === '축산'" class="icon" />
      {{ ingredient.ingredientName }}
    </div>
  </td>
</template>
<script>
import { RedIcon, BlueIcon, GreenIcon } from '@/assets/index.js';

export default {
  name: 'CFRecommendCard',
  components: {
    RedIcon,
    BlueIcon,
    GreenIcon,
  },
  props: {
    ingredient: Object,
  },
};
</script>
