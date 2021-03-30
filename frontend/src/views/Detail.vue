<template>
  <div class="detail">
    <!-- header -->
    <v-toolbar color="primary">
      <v-app-bar-nav-icon>
        <v-btn icon>
          <v-icon>mdi-chevron-left</v-icon>
        </v-btn>
      </v-app-bar-nav-icon>
      <v-toolbar-title>{{ $route.params.id }}</v-toolbar-title>
      <v-btn icon>
        <v-icon>mdi-heart-outline</v-icon>
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

    <!-- body -->
    <v-container class="red lighten-5 justify-center align-center contents">
      <v-row class="row">
        <v-col :cols="3">
          <v-card class="pa-2" outlined tile>
            현재시세
            <br />
            <div class="currentPrice">
              <CurrentPrice />
            </div>
          </v-card>
        </v-col>
        <v-col :cols="9">
          <v-card class="pa-2" outlined tile>
            <div class="lineChart">
              1년 가격 추이
              <LineChart />
            </div>
          </v-card>
        </v-col>
      </v-row>
      <v-row class="row">
        <v-col :cols="6">
          <v-card class="pa-2" outlined tile>
            쇼핑몰별 최저가
          </v-card>
        </v-col>
        <v-col :cols="6">
          <v-card class="pa-2" outlined tile>
            추천시스템
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
<script>
import '@/components/css/detail/style.scss';
import LineChart from '@/components/detail/lineChart.vue';
import CurrentPrice from '@/components/detail/currentPrice.vue';

export default {
  name: 'Detail',
  components: {
    LineChart,
    CurrentPrice,
  },
};
</script>
