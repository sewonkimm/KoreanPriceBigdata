<template>
  <div class="card">
    <div class="bookMarkBar">
      <img src="../../assets/bookmark.png" width="50" height="50" class="charBar" />
    </div>
    <img src="../../assets/main/warning.png" width="39" height="39" class="charBar" />

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

<style lang="scss">
@import '../css/main/card';
</style>

<script>
export default {
  name: 'Card',
};
</script>
