import Vue from 'vue';
import Vuex from 'vuex';
import createPersistedState from 'vuex-persistedstate';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    splash: true, // 첫 방문시에만 splash 보기
    userId: '',
  },
  mutations: {
    SOCIALLOGIN: (state, id) => {
      state.userId = id;
    },
    LOGOUT: (state) => {
      state.userId = '';
    },
    READSPLASH: (state) => {
      state.splash = false;
    },
  },
  plugins: [createPersistedState()],
});
