<template>
  <div class="header">
    <v-toolbar color="primary">
      <v-app-bar-nav-icon>
        <v-btn icon @click="goBack">
          <v-icon color="white">mdi-chevron-left</v-icon>
        </v-btn>
      </v-app-bar-nav-icon>
      <v-toolbar-title class="title">{{ ingredientName }}</v-toolbar-title>
      <v-btn icon @click="handleStarClick">
        <v-icon color="white" v-if="favorite">mdi-heart</v-icon>
        <v-icon color="white" v-else>mdi-heart-outline</v-icon>
      </v-btn>

      <v-spacer></v-spacer>

      <v-toolbar class="search" dense max-width="283px">
        <v-text-field
          hide-details
          prepend-icon="mdi-magnify"
          single-line
          label="상품 검색"
        ></v-text-field>
      </v-toolbar>
    </v-toolbar>
  </div>
</template>
<script>
import '@/components/css/detail/header.scss';

export default {
  name: 'Header',
  created() {
    // this.memberId = this.$store.state.userId;

    this.getFavorite(this.memberId, this.ingredientId);
    this.getIngredientName(this.ingredientId); // 찾은 ingredientId로 ingredientName 찾기
  },
  data() {
    return {
      ingredientId: this.$router.params.id, //  라우터에서 ingredientId 찾기
      ingredientName: '',
      memberId: 1,
      favorite: false,
    };
  },
  methods: {
    goBack() {
      this.$router.go(-1);
    },
    getIngredientName(ingredientId) {
      this.$axios({
        url: '/ingredients/detailId/' + ingredientId,
        method: 'GET',
      })
        .then((response) => {
          this.ingredientName = response.data.ingredientName;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    handleStarClick() {
      this.$axios({
        url: '/favorites',
        method: 'POST',
        data: {
          ingredientId: 1,
          memberId: 1,
        },
      })
        .then(() => {
          this.favorite = true;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getFavorite(memberId, ingredientId) {
      this.$axios({
        url: '/favorites/' + 1 + '/' + 1,
        method: 'GET',
      })
        .then((response) => {
          console.log(response);
          console.log(this.favorite);
          if (response.data == 1) {
            this.favorite = true;
          } else {
            console.log(this.favorite);
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>
