<template>
  <div class="main">
    <!-- 배경 그라데이션을 위한 div -->
    <div class="background" />

    <!-- 커서 -->
    <div class="cursor" id="cursor" />

    <!-- 로고 -->
    <div class="logo">
      <Logo />
    </div>

    <!-- 로그인 -->
    <div id="login">
      <router-link to="/login">로그인</router-link>
    </div>

    <!-- 검색창 -->
    <v-toolbar class="search">
      <v-toolbar-title>
        <v-icon>mdi-magnify</v-icon>
      </v-toolbar-title>
      <v-autocomplete
        v-model="select"
        :loading="loading"
        :items="items"
        :search-input.sync="search"
        cache-items
        class="mx-4"
        flat
        hide-no-data
        hide-details
        label="상품 검색"
        solo
      ></v-autocomplete>
      <!-- <v-text-field hide-details prepend-icon="mdi-magnify" single-line></v-text-field> -->
    </v-toolbar>

    <!-- 카드 컴포넌트 -->
    <CardContainer />
  </div>
</template>
<script>
import '@/components/css/main/style.scss';
import '@/components/css/main/card.scss';
import { Logo } from '@/assets/index.js';
import CardContainer from '@/components/main/cardContainer';

export default {
  name: 'Main',
  components: {
    Logo,
    CardContainer,
  },
  data() {
    return {
      loading: false,
      items: [],
      search: null,
      select: null,
      ingredients: {
        ingredientName: [],
        ingredientId: [],
      },
      ingredientsId: [],
    };
  },
  watch: {
    search(val) {
      val && val !== this.select && this.querySelections(val);
    },
    select: function() {
      // 검색한 카드 컴포넌트만 보여주기
      this.$router.push({
        name: 'Detail',
        params: {
          id: this.ingredientsId,
        },
      });
    },
  },
  methods: {
    querySelections(v) {
      this.loading = true;
      // Simulated ajax query
      setTimeout(() => {
        this.items = this.ingredients.ingredientName.filter((e) => {
          return (e || '').toLowerCase().indexOf((v || '').toLowerCase()) > -1;
        });
        this.loading = false;
      }, 500);
    },
    getIngredients() {
      // ingredients 받아오기
      this.$axios({
        url: '/ingredients/ingredientName',
        method: 'GET',
      })
        .then((response) => {
          // this.ingredientsId = response;
          this.ingredients.ingredientName = response.data.map((item) => {
            item = item.ingredientName;
            return item;
          });
        })
        .catch(() => {});
    },
  },
  created() {
    this.getIngredients();
  },
};
</script>
