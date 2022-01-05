import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)


export default new Vuex.Store({
  state: {
    base_url: 'http://127.0.0.1:8000/api/',
    posts : [],
    categories : [],
  },
  mutations: {
    get_post(state,payload){
      state.posts = payload
    },
    get_category(state,payload){
      state.categories = payload
    }
  },
  actions: {
    get_post_data({commit,state}){
      let config = {
        method: "get",
        url:state.base_url + "news/list/"
      }
      return axios(config)
          .then(response => {commit("get_post",response.data)})

    },
    delete_post({state},payload){
      let config = {
        method: "delete",
        url:state.base_url + "news/delete/"+payload.id
      }
      return axios(config).then(()=>{
        this.dispatch('get_post_data')
      })
    },
    submit_category({state},payload){
      let data = new FormData();
      data.append('title',payload.title)
      let config = {
        method: "post",
        url:state.base_url + "category/submit/",
        data:data
      }
      return axios(config).then(response=>{
        console.log(response.data)

      })
    },
    update_category({state},payload){
      let data = new FormData();
      data.append('title',payload.title)
      let config = {
        method: "put",
        url: state.base_url+"category/update/"+payload.id,
        data:data
      }
      return axios(config).then(response =>{
        console.log(response.data)
        this.dispatch('get_category_data')
      })
    },
    get_category_data({commit,state}){
  let config = {
    method: "get",
    url:state.base_url + "category/list/"
  }
  return axios(config)
      .then(response => {commit("get_category",response.data)})
},
    delete_category({state},payload){
      let config = {
        method: "delete",
        url:state.base_url + "category/delete/"+payload.id
      }
      return axios(config).then(()=>{
        this.dispatch('get_category_data')
      })
    },

  },
  modules: {
  }
})
