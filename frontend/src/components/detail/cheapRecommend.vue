<template>
  <v-simple-table>
    <template v-slot:default>
      <thead>
        <tr>
          <th>
            항목
          </th>
          <th>
            가격
          </th>
          <th>
            하락율
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in items" :key="index" @click="moveToRecommend(item.ingredientId)">
          <td v-if="item.ingredientDetailName == null">
            {{ item.ingredientName }}
          </td>
          <td v-else>{{ item.ingredientDetailName }}</td>
          <td>{{ item.ingredientAvgPrice }}</td>
          <td>{{ item.rate }}%</td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
</template>
<script>
export default {
  name: 'CheapRecommend',
  data() {
    return {
      items: [],
      ingredientId: this.$route.params.id,
    };
  },
  methods: {
    getFluctuationRecommand: function() {
      this.$axios({
        url: '/fluctuationRates/rate/' + this.ingredientId,
        method: 'GET',
      })
        .then((response) => {
          this.items = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    moveToRecommend: function(index) {
      this.$router.push({
        name: 'Detail',
        params: {
          id: index,
        },
      });
    },
  },
  created() {
    this.getFluctuationRecommand();
  },
};
</script>
