<template>
  <v-container class="mt-5 blue lighten-4">
  <v-card flat  v-for="post in this.$store.state.posts.results" :key="post.id" cols = "8">
    <v-card-text>
      <v-row>
        <v-col cols="6" md="3">
          <div class="caption grey--text ">Title</div>
          <div> {{post.title}} </div>
        </v-col>
        <v-col cols="6" sm="4" md="2" >
          <div class="caption grey--text ">ID</div>
          <div> {{post.id}} </div>
        </v-col>
        <v-col cols="12" sm="4" md="4" >
          <div class="caption grey--text ">Created at</div>
          <div> {{post.created_at}} </div>
        </v-col>
        <v-col cols="5" sm="4" md="3" >
          <div class="right">
            <button @click="" style="margin: 2%"> edit</button>
            <v-btn color="red lighten-2 white--text" @click="$store.dispatch('delete_post',{id:post.id})" > delete</v-btn>
          </div>
        </v-col>
      </v-row>
      <v-divider class="mt-4"/>
    </v-card-text>
  </v-card>
    <br>
    <cat_add_popup/>
    <v-card flat  v-for="category in $store.state.categories.results" :key="category.id" cols = "8">
      <v-card-text>
        <v-row>
          <v-col cols="12" md="4">
            <div class="caption grey--text ">Title</div>
            <div> {{category.title}} </div>
          </v-col>
          <v-col cols="6" sm="4" md="4" >
            <div class="caption grey--text ">ID</div>
            <div> {{category.id}} </div>
          </v-col>
          <v-col cols="5" sm="4" md="4" >
            <div class="right">
              <popup
                :catid = category.id
                :cattitle = category.title
              />
              <v-btn color="red lighten-2 white--text" @click="$store.dispatch('delete_category',{id:category.id})" > delete</v-btn>
            </div>
          </v-col>
        </v-row>
        <v-divider class="mt-4"/>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import popup from "../components/popup.vue";
import cat_add_popup from "../components/cat_add_popup.vue";
export default {
  name: "admin_page",
  components:{
    popup,
    cat_add_popup
  },
  mounted() {
    this.$store.dispatch("get_post_data")
  },
  data() {
    return {

    }
  },

  methods:{
  },
}
</script>

<style scoped>

</style>