// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'

import Vuex from 'vuex'
import router from './router'
import VueResource from 'vue-resource'
import VueSession from 'vue-session'

Vue.config.productionTip = false
Vue.use(VueResource)
Vue.use(Vuex)
Vue.use(VueSession)

const store = new Vuex.Store({
  state: {
    url: 'http://149.56.14.83:5000'
  },
  mutations: {
    increment (state) {
      state.count++
    }
  }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
