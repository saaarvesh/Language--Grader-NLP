import Vue from 'vue'
import Vuex from 'vuex'
import '@/server.config.js'
import router from '@/router/index.ts'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {},
  mutations: {},
  actions: {
    login ({ commit }, credentials) {
      console.log(credentials)
    },
    uploadText ({ commit }, textToGrade) {
      console.log('Hello from store!')
      console.log(textToGrade)
      return new Promise((resolve, reject) => {
        setTimeout(() => {
          router.push('DisplayGrade')
        }, 1500)
      })
    }
  },
  modules: {}
})
