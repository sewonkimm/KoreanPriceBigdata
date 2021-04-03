<template>
  <div class="detail">
    <!-- header -->
    <Header />

    <!-- body -->
    <v-container class="justify-center align-center contents">
      <v-row class="row row-1">
        <v-col :cols="3">
          <v-card class="pa-2 flip-vertical-left" @mouseenter.stop="changePrice">
            <CurrentPrice v-if="isCurrentPrice" />
            <PredictPrice v-else />
          </v-card>
        </v-col>
        <v-col :cols="9">
          <v-card class="pa-2">
            <div class="lineChart">
              1년 가격 추이
              <LineChart :height="300" />
            </div>
          </v-card>
        </v-col>
      </v-row>
      <v-row class="row row-2">
        <v-col :cols="6">
          <v-card class="pa-2">
            <Shopping />
          </v-card>
        </v-col>
        <v-col :cols="6">
          <v-card class="pa-2">
            <Recommend />
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
<script>
import '@/components/css/detail/style.scss';
import Header from '@/components/detail/header';
import CurrentPrice from '@/components/detail/currentPrice';
import PredictPrice from '@/components/detail/predictPrice';
import LineChart from '@/components/detail/lineChart';
import Shopping from '@/components/detail/shopping';
import Recommend from '@/components/detail/recommend';

export default {
  name: 'Detail',
  components: {
    Header,
    CurrentPrice,
    PredictPrice,
    LineChart,
    Shopping,
    Recommend,
  },
  data() {
    return {
      isCurrentPrice: true,
    };
  },
  methods: {
    changePrice: function() {
      this.isCurrentPrice = !this.isCurrentPrice;
    },
  },
};
</script>
