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
          <td>{{ item.ingredientName }}</td>
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
      items: [
        {
          ingredientId: 42,
          ingredientName: '새송이버섯',
          rate: -1.91,
        },
        {
          ingredientId: 42,
          ingredientName: '새송이버섯',
          rate: -1.91,
        },
        {
          ingredientId: 42,
          ingredientName: '새송이버섯',
          rate: -1.91,
        },
        {
          ingredientId: 42,
          ingredientName: '새송이버섯',
          rate: -1.91,
        },
        {
          ingredientId: 42,
          ingredientName: '새송이버섯',
          rate: -1.91,
        },
      ],
    };
  },
};
</script>
