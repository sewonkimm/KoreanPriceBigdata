<template>
  <div class="header">
    <v-toolbar color="primary">
      <v-app-bar-nav-icon>
        <v-btn icon @click="goBack">
          <v-icon color="white">mdi-chevron-left</v-icon>
        </v-btn>
      </v-app-bar-nav-icon>
      <v-toolbar-title class="title">{{ ingredientName }}</v-toolbar-title>
      <v-btn icon>
        <v-icon color="white">mdi-heart-outline</v-icon>
      </v-btn>

      <v-spacer></v-spacer>

      <!-- 검색창 -->
      <v-toolbar class="search" dense max-width="283px">
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
      </v-toolbar>
    </v-toolbar>
  </div>
</template>
<script>
import '@/components/css/detail/header.scss';

export default {
  name: 'Header',
  created() {
    this.getIngredientName(this.ingredientId); // 찾은 ingredientId로 ingredientName 찾기
    this.getIngredients();
  },
  data() {
    return {
      ingredientId: this.$route.params.id, //  라우터에서 ingredientId 찾기
      ingredientName: '',
      // -- search 관련 state --
      loading: false,
      items: [], // 검색할 때마다 밑에 나오는 데이터
      searchIngredientName: [], // autocomplete 검색을 위해 이름만 있는 데이터
      search: null,
      select: null,
      ingredients: [
        {
          ingredientId: 0,
          ingredientName: '',
        },
      ],
      // --
    };
  },
  watch: {
    search(val) {
      val && val !== this.select && this.querySelections(val);
    },
    select: function() {
      // 검색한 카드 컴포넌트만 보여주기
      const selectId = this.getIngredientId(this.select);
      this.$router.push({
        name: 'Detail',
        params: {
          id: selectId,
        },
      });
    },
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
    // -- search 관련 method --
    querySelections(v) {
      this.loading = true;
      // Simulated ajax query
      setTimeout(() => {
        this.items = this.searchIngredientName.filter((e) => {
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
          this.ingredients = response.data.map((item) => {
            let ingredientName = item.ingredientName;
            if (item.ingredientDetailName !== null) {
              ingredientName += `(${item.ingredientDetailName})`;
            }
            item = {
              ingredientId: item.ingredientId,
              ingredientName: ingredientName,
            };
            return item;
          });

          this.searchIngredientName = this.ingredients.map((item) => {
            return item.ingredientName;
          });
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getIngredientId(name) {
      return this.ingredients.filter((item) => {
        return item.ingredientName === name;
      })[0].ingredientId;
    },
    // --
  },
};
</script>
