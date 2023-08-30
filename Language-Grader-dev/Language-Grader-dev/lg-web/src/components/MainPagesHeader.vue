<template>
  <div>
    <nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
      <div class="container">
        <a href="#" class="navbar-brand text-warning font-weight-bold">
          <img
            src="@/assets/TAT - Final LOGO White cropped.png"
            alt="TAT Logo"
            style="width:100px;height:80px;margin-right:12px"
          />
          <!-- <span>LANGUAGE GRADER</span> -->
        </a>
        <button
          class="navbar-toggler"
          type="button"
          data-toggle="collapse"
          data-target="#collapsenavbar"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collpase navbar-collapse text-end" id="collapsenavbar">
          <ul class="navbar-nav ml-auto font-weight-bold myclass">
            <li class="nav-item p-3">
              <a href="#home" class="nav-link text-warning">Home</a>
            </li>
            <li class="nav-item p-3">
              <a href="#services" class="nav-link text-white">Services</a>
            </li>
            <li class="nav-item p-3">
              <a href="#members" class="nav-link text-white">Team</a>
            </li>
            <li class="nav-item p-3">
              <a href class="nav-link text-white">About Us</a>
            </li>
            <li class="nav-item p-3">
              <a href class="nav-link text-white">{{ this.$store.state.user.name}}</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
export default {

}
</script>
