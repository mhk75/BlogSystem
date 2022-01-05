<template>
<v-container class="my-5">
  <v-card v-for="post in this.$store.state.posts.results" :key="post.id" class="mt-5">
    <v-card-title>
      <span>item title:</span>
      <span> {{post.title}} </span>
    </v-card-title>
    <v-card-text>
      <span> {{post.content}} </span>
    </v-card-text>
    <v-card-actions>
      <span>categories:</span>
      <v-spacer></v-spacer>
      <span v-for="category in post.category">
        {{category}},
      </span>
    </v-card-actions>
  </v-card>
</v-container>
</template>

<script>
export default {
  name: "items",
  mounted() {
    this.$store.dispatch("get_post_data")
  },


}
</script>

<style scoped>

</style>