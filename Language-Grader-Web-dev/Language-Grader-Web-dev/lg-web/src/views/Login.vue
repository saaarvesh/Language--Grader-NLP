<template>
  <div class="login">
    <login-form />
    <entry-level-footer />
  </div>
</template>

<script>
import EntryLevelFooter from '@/components/EntryLevelFooter.vue'
import LoginForm from '@/components/LoginForm.vue'

export default {
  components: {
    EntryLevelFooter,
    LoginForm
  }
}
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}
.login {
  background-image: url("../assets/login-background.png");
  background-size: 100% 100%;
  background-attachment: fixed;
  color: black;
}
</style>
