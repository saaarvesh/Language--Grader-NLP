import Vue from 'vue'
import Vuex from 'vuex'
import { baseurl, basedomain } from '@/server.config.js'
import axios from 'axios'

import router from '@/router/index.ts'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: {
      name: ''
      // email: ''
    }
  },
  mutations: {
    SET_USER (state, username) {
      state.user.name = username
    }
  },
  actions: {
    async login ({ commit }, credentials) {
      // const basedomain = 'http://127.0.0.1'
      console.log(credentials)
      console.log('Hello from store!' + baseurl)
      const constructedUrl = baseurl + '/tat/auth'
      // body = 'email=' + credentials.email + '&pass=' + credentials.password
      await axios({
        method: 'post',
        url: constructedUrl,
        responseType: 'json',
        data: {
          email: credentials.email,
          pass: credentials.password
        }
      })
        .then(function (response) {
          console.log(typeof response.data)
          if (response.data.auth === true) {
            commit('SET_USER', response.data.username)
            router.push('Home')
          } else if (response.data.auth === false) {
            alert('login failed')
          }
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    async register ({ commit }, credentials) {
      // const basedomain = 'http://127.0.0.1'
      console.log(credentials)
      console.log('Hello from store!' + baseurl)
      const constructedUrl = baseurl + '/tat/register'
      await axios({
        method: 'post',
        url: constructedUrl,
        responseType: 'json',
        data: {
          name: credentials.name,
          email: credentials.email,
          pass: credentials.password,
          phone: credentials.phone,
          category: credentials.category
        }
      })
        .then((response) => {
          console.log(response.data)
          if (response.data.registration === true) {
            return this.dispatch('login', {
              email: credentials.email,
              password: credentials.password
            })
          }
        })
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
