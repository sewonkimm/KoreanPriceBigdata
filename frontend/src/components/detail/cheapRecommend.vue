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
        <tr v-for="(item, index) in items" :key="index">
          <td v-if="item.ingredientDetailName == null">
            {{ item.ingredientName }}
          </td>
          <td v-else>{{ item.ingredientDetailName }}</td>
          <td>2300</td>
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
    };
  },
  methods: {
    getFluctuationRecommand: function() {
      this.$axios({
        url: '/fluctuationRates/rate/' + this.$route.params.id,
        method: 'GET',
      })
        .then((response) => {
          console.log('등락률');
          console.log(response);
          this.items = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getFluctuationRecommand();
  },
};
</script>
