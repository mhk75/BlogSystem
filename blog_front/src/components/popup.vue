<template >
  <div class="ma-2">
    <v-dialog
        v-model="dialog"
        width="500"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
            color="primary"
            dark
            v-bind="attrs"
            v-on="on"
        >
          Edit
        </v-btn>
      </template>

      <v-card>
        <v-card-title class="text-h5 grey lighten-2">
          Edit Category
        </v-card-title>

        <v-form class="ma-3">
          <v-text-field v-model="cattitle" label="Title"></v-text-field>
        </v-form>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
              color="primary"
              text
              @click="$store.dispatch('update_category',{title:cattitle,id:catid})"
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
  name: "popup",
  data () {
    return {
      dialog: false,

    }
  },
  props:['cattitle','catid'],

}
</script>

<style scoped>

</style>