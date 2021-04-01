import Vue from 'vue';
import App from './App.vue';
import router from './router';
import vuetify from './plugins/vuetify';
import axios from 'axios';
import store from './store';

Vue.config.productionTip = false;

Vue.prototype.$axios = axios;
axios.defaults.baseURL = 'http://localhost:8080';
axios.defaults.headers.post['Content-Type'] = 'application/json';

new Vue({
  router,
  vuetify,
  store,
  render: (h) => h(App),
}).$mount('#app');
