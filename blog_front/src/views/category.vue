<template>
<v-container class="mt-5 white">
  <h2>Create Category</h2>
  <form class="mt-3">
    <div class="form-group">
      <label>Title</label>
      <input type="text" class="form-control ml-4 " v-model="cattitle" style="background-color: lightcyan">
        </div>
    <div class="mt-3">
      <button type="submit" @click="$store.dispatch('submit_category',{title:cattitle})" >Create Post</button>
    </div>
  </form>
</v-container>
</template>

<script>
export default {
  name: "category",
  data(){
    return{
      cattitle: ''
    }
  }
}
</script>

<style scoped>

</style>