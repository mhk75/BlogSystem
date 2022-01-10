<template>
  <nav >
    <v-toolbar flat app class="indigo">
      <!-- <button @click="debug"> test button</button>   -->
      <v-app-bar-nav-icon @click="drawer= !drawer" class="white--text"></v-app-bar-nav-icon>
      <v-toolbar-title class="text-uppercase white--text">
        <span>blog</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn flat @click="go_to_home" class="mr-4">Home</v-btn>
      <v-btn flat @click="go_to_admin">
        <span>Admin</span>
        <v-icon right>mdi-exit-to-app</v-icon>
      </v-btn>
    </v-toolbar>
    <v-navigation-drawer
        v-model="drawer"
        absolute
        bottom
        temporary

    >

      <v-layout>
        <v-flex class="mt-5">
          <span>Categories</span>
        </v-flex>
      </v-layout>
      <v-list
          nav
          dense
      >
        <v-list-item-group
            active-class="deep-purple--text text--accent-4"
        >
          <v-list-item v-for="category in this.$store.state.categories.results" :key="category.id">
            <v-list-item-title> {{category.title}} </v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </nav>

</template>

<script>
export default {
  name: "navbar",
  data() {
    return {
      drawer: false,
    }
  },
  methods: {
    debug() {
      console.log(this.$store.state.posts.results)
    },
    go_to_admin(){
      this.$router.push('/admin')
    },
    go_to_home(){
      this.$router.push('/')
    }
  },
  mounted() {
    this.$store.dispatch("get_category_data")
  },
}
</script>

<style scoped>

</style>