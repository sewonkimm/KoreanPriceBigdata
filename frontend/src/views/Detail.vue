<template>
  <div class="detail">
    <!-- header -->
    <Header />

    <!-- body -->
    <v-container class="justify-center align-center contents">
      <v-row class="row row-1">
        <v-col :cols="4">
          <v-card class="pa-2 infoCard" :style="cssVars">
            <Information />
          </v-card>
        </v-col>
        <v-col :cols="4">
          <v-card class="pa-2">
            <CurrentPrice />
          </v-card>
        </v-col>
        <v-col :cols="4">
          <v-card class="pa-2">
            <PredictPrice />
          </v-card>
        </v-col>
      </v-row>
      <v-row class="row row-2">
        <v-col :cols="12">
          <v-card class="pa-2">
            <div class="lineChart">
              1년 가격 추이
              <LineChart :height="270" />
            </div>
          </v-card>
        </v-col>
      </v-row>
      <v-row class="row row-3">
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
import Information from '@/components/detail/information';
import CurrentPrice from '@/components/detail/currentPrice';
import PredictPrice from '@/components/detail/predictPrice';
import LineChart from '@/components/detail/lineChart';
import Shopping from '@/components/detail/shopping';
import Recommend from '@/components/detail/recommend';

export default {
  name: 'Detail',
  components: {
    Header,
    Information,
    CurrentPrice,
    PredictPrice,
    LineChart,
    Shopping,
    Recommend,
  },
  data: function() {
    return {
      userId: '',
      ingredientId: '',
    };
  },
  computed: {
    cssVars() {
      return {
        '--bg-url': `url('https://j4a301.p.ssafy.io/ingredients/ingredients_${this.$route.params.id}.png')`,
      };
    },
  },
  created() {
    this.userId = this.$store.state.userId;
    this.ingredientId = this.$route.params.id;
    handleInsertWatch();
  },
  methods: {
    handleInsertWatch() {
      this.$axios({
        url: '/watches',
        method: 'POST',
        data: {
          ingredientId: this.ingredientId,
          memberId: this.userId,
        },
      })
        .then(() => {})
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
