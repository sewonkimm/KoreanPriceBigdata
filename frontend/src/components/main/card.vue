<template>
  <div class="card">
    {{ item.name }}
    {{ index }}
  </div>
</template>
<script>
export default {
  name: 'Card',
  props: {
    item: Object,
    index: Number,
  },
};
</script>
<style>
.card {
  width: 240px;
  height: 320px;
  background-color: blueviolet;
}
</style>
