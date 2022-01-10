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
          Create Post
        </v-btn>
      </template>

      <v-card>
        <v-card-title class="text-h5 grey lighten-2">
          Create Post
        </v-card-title>

        <v-form class="ma-3">
          <v-text-field v-model="posttitle" label="title"></v-text-field>
          <v-text-field v-model="postcontent" label="content"></v-text-field>
        </v-form>
        <p>{{ selected }}</p>
        <v-checkbox
            v-model="selected"
            label="John"
            value="John"
        ></v-checkbox>
        <v-checkbox
            v-model="selected"
            label="Jacob"
            value="Jacob"
        ></v-checkbox>
        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
              color="primary"
              text
              @click="$store.dispatch('submit_post',{title:posttitle,content:postcontent,created_at:datetime})"
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
  name: "post_add_popup",
  data () {
    return {
      dialog: false,
      posttitle:"",
      postcontent:"",
      datetime:"",
      selected: ['John'],
    }
  },
  methods:{
    printFullDate: function(){
      return new Date();
    }
  },
  mounted:function () {
    this.datetime = this.printFullDate()
  }
}
</script>

<style scoped>

</style>