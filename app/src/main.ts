import Vue from 'vue'
import Chakra, { CThemeProvider, CReset } from '@chakra-ui/vue'

import App from './App.vue'
import router from './router'

import './assets/main.css'
Vue.use(Chakra)

new Vue({
  router,
  render: (h) => h(CThemeProvider, [h(CReset), h(App)])
}).$mount('#app')
