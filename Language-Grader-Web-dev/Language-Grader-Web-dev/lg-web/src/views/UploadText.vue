<template>
  <div class="upload">
    <main-pages-header />
    <div class="uploadForm" v-if="!submitComplete">
      <b-form @submit.prevent="onSubmit">
        <b-form-group id="text-to-grade-group">
          <label class="label" for="text-to-grade"
            >Select the type of text:</label
          >
          <b-form-select
            id="text-to-grade"
            v-model="textToGrade.textType"
            :options="textTypes"
            required
          ></b-form-select>
        </b-form-group>
        <b-form-group id="subject-group">
          <label class="label" for="subject-of-text"
            >Enter the subject of the text:</label
          >
          <b-form-input
            id="subject-of-text"
            v-model="textToGrade.subject"
            required
          ></b-form-input>
        </b-form-group>
        <b-form-group id="text-group">
          <label class="label" for="text-to-upload"
            >Enter the text:</label
          >
          <b-form-textarea
            id="text-to-upload"
            v-model="textToGrade.text"
            rows="12"
            placeholder="Enter the text"
            no-resize
            required
          ></b-form-textarea>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
      </b-form>
    </div>
    <div class="loading-screen" v-if="submitComplete">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <b-spinner style="width: 3rem; height: 3rem;" label="Large Spinner" type="grow"></b-spinner>
            <b-spinner style="width: 3rem; height: 3rem;" label="Large Spinner" type="grow"></b-spinner>
            <b-spinner style="width: 3rem; height: 3rem;" label="Large Spinner" type="grow"></b-spinner>
            <b-spinner style="width: 3rem; height: 3rem;" label="Large Spinner" type="grow"></b-spinner>
            <b-spinner style="width: 3rem; height: 3rem;" label="Large Spinner" type="grow"></b-spinner>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MainPagesHeader from '@/components/MainPagesHeader.vue'
export default {
  name: 'UploadText',
  data: () => ({
    textToGrade: {
      textType: null,
      subject: '',
      text: ''
    },
    textTypes: [
      {
        text: 'Essay',
        value: 'Essay'
      },
      {
        text: 'Short-Story',
        value: 'Short-Story'
      },
      {
        text: 'Story',
        value: 'Story'
      }
    ],
    submitComplete: false
  }),
  components: {
    MainPagesHeader
  },
  methods: {
    onSubmit (evt) {
      evt.preventDefault()
      console.log(JSON.stringify(this.textToGrade))
      this.$store.dispatch('uploadText', this.textToGrade)
      this.submitComplete = true
      // alert(JSON.stringify(this.textToGrade))
    }
  }
}
</script>

<style scoped>
.upload {
  margin: 150px 24px 150px 24px;
}
label {
  color: black;
  display: block;
  text-align: start;
}
.container {
  margin: 150px 0 0 0;
}
</style>
