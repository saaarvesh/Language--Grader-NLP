import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
// import "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css"
import { BootstrapVue } from 'bootstrap-vue'
// import vuetify from '@/plugins/vuetify' // path to vuetify export
import VueGraph from 'vue-graph'

Vue.use(VueGraph)
// Install BootstrapVue
Vue.use(BootstrapVue)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  // vuetify,
  render: h => h(App)
}).$mount('#app')
