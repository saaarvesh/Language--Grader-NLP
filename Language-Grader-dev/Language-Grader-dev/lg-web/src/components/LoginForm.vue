<template>
    <div>
<link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css"
    />
    <br />
    <br />
    <h2 style="text-align: center; color:white">
      <strong>LANGUAGE GRADER</strong>
    </h2>
    <br />
    <!-- <p style="color:cyan; text-align: center; font-size:25px;">This is the first login page <br>created for learning.</p> -->
    <form name="f1" @submit.prevent="loginMethod">
      <div class="myform">
        <br />
        <br />
        <div class="form">
          <img src="../assets/login-logo.png" height="150px" width="150px" />
          <br />
          <br />
          <label>
            <b>Email</b>
          </label>
          <div class="input-icons">
            <i class="fa fa-envelope icon"></i>
            <input
              v-model="form.email"
              type="email"
              name="user_email"
              id="user_email"
              pattern="[^ @]*@[^ @]*"
              placeholder="Enter Email"
              class="input-field"
              required
            />
          </div>
          <label>
            <b>Password</b>
          </label>
          <br />
          <div class="input-icons">
            <i class="fa fa-key icon"></i>
            <input
              v-model="form.password"
              type="password"
              name="user_pass"
              id="user_pass"
              class="input-field"
              placeholder="Enter password"
              title="Enter valid Password"
            />
            <br />
          </div>
          <div width="100%">
            <input type="checkbox" class="button1" style="margin:5px;" />
            <label style="color: blanchedalmond;margin:5px">Remember Me</label>
            <br />
          </div>
          <a href="#" class="button1">
            <p style="font-size:15px;margin:5px;">Forgot Password ?</p>
          </a>
          <br />
          <br />
          <button
            type="submit"
            class="button2"
            onclick="alert('Your Response Has Been Submitted"
          >Login</button>
          <br />
          <br />
            <b-button type="button" class="button2" to="Register">Create New Account</b-button>
          <!-- <p style="color:white">Already have an account?<a href="#"> Sign In</a></p> -->
        </div>
      </div>
    </form>
    </div>
</template>

<script>
export default {
  name: 'loginForm',
  data () {
    return {
      form: {
        email: '',
        password: ''
      }
    }
  },
  methods: {
    loginMethod () {
      console.log(this.form.email)
      this.$store.dispatch('login', this.form)
    }
  }

}
</script>
<style scoped>
.form {
  text-align: center;
}
.input-icons {
  width: 100%;
  margin-bottom: 30px;
}
.icon {
  padding: 5px;
  color: black;
  min-width: 30px;
}
.input-icons i {
  position: absolute;
}
.input-field {
  width: 20%;
  text-align: center;
}
label {
  color: white;
}
input[type="checkbox"] {
  color: white;
}
.button2 {
  width: 20%;
  background-color: white;
  color: black;
  padding: 5px;
  border: 0.1em solid white;
  margin: 0;
  border-radius: 1em;
  font-family: Times New Roman;
  font-size: 17;
  font-weight: 600;
}
.button2:hover {
  background-color: rgb(196, 196, 196);
}
</style>
