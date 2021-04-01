<template>
  <div class="detail">
    <!-- header -->
    <Header />

    <!-- body -->
    <v-container class="red lighten-5 justify-center align-center contents">
      <v-row class="row">
        <v-col :cols="3">
          <v-card class="pa-2" outlined tile>
            현재시세
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
import Recommend from '@/components/detail/recommend';
import LineChart from '@/components/detail/lineChart';

export default {
  name: 'Detail',
  components: {
    Header,
    Recommend,
    LineChart,
  },
};
</script>
