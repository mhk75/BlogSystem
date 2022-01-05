<template>
  <div class="ma-2">
    <v-dialog
        v-model="dialog"
        width="500"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
            color="success"
            dark
            v-bind="attrs"
            v-on="on"
        >
          Create Category
        </v-btn>
      </template>

      <v-card>
        <v-card-title class="text-h5 grey lighten-2">
          Create Category
        </v-card-title>

        <v-form class="ma-3">
          <v-text-field v-model="cattitle" label="title"></v-text-field>
        </v-form>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
              color="primary"
              text
              @click="$store.dispatch('submit_category',{title:cattitle})"
          >
            Submit
          </v-btn>
          <v-btn
              color="red lighten-2"
              text
              @click="dialog = false"
          >
            Cancel
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
export default {
  name: "cat_add_popup",
  data () {
    return {
      dialog: false,
      cattitle:""
    }
  },
}
</script>

<style scoped>

</style>