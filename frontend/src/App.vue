<template>
  <div>
    <HelloWorld msg="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
import './components/css/style.scss';
import HelloWorld from './components/HelloWorld.vue';

export default {
  name: 'App',
  components: {
    HelloWorld,
  },
};
</script>
