import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    splash: true,
    userId: '1',
  },
  mutations: {
    SOCIALLOGIN: (state, id) => {
      state.userId = id;
    },
    LOGOUT: (state) => {
      state.userId = '';
    },
  },
});
