<template>
  <div>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css">
    <br />
    <br />
    <h2 style="text-align: center; color:white">
      <strong>LANGUAGE GRADER</strong>
    </h2>
    <br />
    <!-- <p style="color:cyan; text-align: center; font-size:25px;">This is the first login page <br>created for learning.</p> -->
    <form>
      <div class="myform">
        <br />
        <br />
        <div class="form">
          <img src="@/assets/login-logo.png" height="150px" width="150px" />
          <br />
          <br />
          <label>
            <b>User Name</b>
          </label>
          <br />
          <div class="input-icons">
            <i class="fa fa-user icon"></i>
            <input
              type="text"
              class="input-field"
              placeholder="Enter user name"
              title="Enter in block"
            />
          </div>
          <label>
            <b>Email</b>
          </label>
          <div class="input-icons">
            <i class="fa fa-envelope icon"></i>
            <input
              type="email"
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
              type="password"
              class="input-field"
              placeholder="Enter password"
              title="Enter valid Password"
            />
            <br />
          </div>
          <label>
            <b>Phone Number</b>
          </label>
          <br />
          <div class="input-icons">
            <i class="fa fa-phone icon"></i>
            <input
              type="text"
              class="input-field"
              placeholder="Enter Phone No."
              title="Enter only digits"
            />
          </div>
          <label>
            <b>Select the Category:</b>
          </label>
          <br />
          <div>
            <select name="category" class="input-field">
              <option value="student">Student</option>
              <option value="faculty">Faculty</option>
              <option value="HR">HR</option>
            </select>
          </div>
          <br />
          <br />
          <button
            type="submit"
            class="button2"
            onclick="alert('Your Response has been submitted')"
          >Sign Up</button>
          <br />
          <br />
        </div>
      </div>
    </form>
  </div>
</template>

<style >
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
</style>
