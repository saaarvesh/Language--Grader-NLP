<template>
  <div class="registration">
    <registration-form />
    <entry-level-footer />
  </div>
</template>
<script>
import EntryLevelFooter from '@/components/EntryLevelFooter.vue'
import RegistrationForm from '@/components/RegistrationForm.vue'

export default {
  components: {
    EntryLevelFooter,
    RegistrationForm
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
}
.registration {
  background-image: url("../assets/login-background.png");
  background-size: 100% 100%;
  background-attachment: fixed;
  color: black;
}
</style>
