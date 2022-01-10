<template>
<v-container class="my-5">
  <v-form>
    <v-row>
      <v-col cols="2" align-self="center">
        <v-btn color="red lighten-2 white--text" @click="$store.dispatch('get_post_search_data',{value:search_value})" > search</v-btn>
      </v-col>
      <v-col cols="6" >
        <v-text-field v-model="search_value" placeholder="search here" ></v-text-field>
      </v-col>
    </v-row>
  </v-form>
  <v-card v-for="post in this.$store.state.posts.results" :key="post.id" class="mt-5">
    <v-card-title>
      <span>item title:</span>
      <span> {{post.title}} </span>
    </v-card-title>
    <v-card-text v-html="post.content">
    </v-card-text>
    <v-card-actions>
      <span>categories:</span>
      <v-spacer></v-spacer>
      <span v-for="category in post.category">
        {{category}},
      </span>
    </v-card-actions>
  </v-card>
  <v-pagination v-model="pagination.current_page" :length="total_page" @input="next"></v-pagination>
</v-container>
</template>

<script>
import {mapGetters} from "vuex";

export default {
  name: "items",
  mounted() {
    this.$store.dispatch("get_post_data",{page:this.pagination.current_page})

  },
  data(){
    return{
      search_value:"",
      pagination:{
        current_page:1,
        per_page:2,
      },
    }
  },
  computed:{
    ...mapGetters({
      total_page:"per_page"
    })
  },
  methods:{
    next(){
    this.$store.dispatch("get_post_data",{page:this.pagination.current_page})

    }
  }


}
</script>

<style scoped>

</style>