<template>
  <div class="main">
    <div class="logo">
      <Logo />
    </div>

    <v-toolbar class="search">
      <v-text-field hide-details prepend-icon="mdi-magnify" single-line></v-text-field>
    </v-toolbar>

    <div class="cardContainer"></div>
  </div>
</template>
<script>
import '@/components/css/main/style.scss';
import { Logo } from '@/assets/index.js';

export default {
  name: 'Main',
  components: {
    Logo,
  },
};
</script>
