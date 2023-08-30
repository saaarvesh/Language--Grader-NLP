<template>
  <div class="home">
    <div class="bgimg">
      <main-pages-header />
      <!-- <nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
        <div class="container">
          <a href="#" class="navbar-brand text-warning font-weight-bold">
            <img
              src="@/assets/TAT - Final LOGO White cropped.png"
              alt="TAT Logo"
              style="width:100px;height:80px;margin-right:12px"
            />
            LANGUAGE GRADER
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
                <a href class="nav-link text-white">Contact Us</a>
              </li>
            </ul>
          </div>
        </div>
      </nav>-->
      <div class="container text-center headerset" id="home">
        <div class="bg-warning bgcol">
          <h2>Upload-Verify-Grade</h2>
          <h1>AUTOMATIC LANGUAGE GRADING</h1>
          <h3>We are creating this for enhancement of proper English language</h3>
          <br />
        </div>
        <br />
        <br />
        <b-button class="btn btn-warning text-dark font-weight-bold btn-lg" to="Upload">Text Upload</b-button>
        <b-button class="btn btn-warning text-dark font-weight-bold btn-lg">History</b-button>
      </div>
    </div>

    <section class="container-fluid ourservices text-center bg-light" id="services">
      <h1>SERVICES</h1>
      <p class="myfont">Text-checking and Grading</p>
      <div class="row rowsetting">
        <div class="col-lg-4 col-md-4 col-sm-4 col-12 d-block m-auto">
          <div class="imgsetting d-block m-auto">
            <img src="@/assets/upload.jpg" width="150px" height="150px" />
            <h2>Text-Upload</h2>
            <p>
              User can upload their content for grammar-checking and
              our product will parse it and give the grading to your content.
            </p>
          </div>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-4 col-12 d-block m-auto">
          <div class="imgsetting d-block m-auto">
            <img src="@/assets/check.jpg" width="150px" height="150px" />
            <h2>Text-Checking</h2>
            <p>
              The uploaded content will be checked grammatically and
              our product will parse it and give the grading to your content.
            </p>
          </div>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-4 col-12 d-block m-auto">
          <div class="imgsetting d-block m-auto">
            <img src="@/assets/grading.jpg" width="150px" height="150px" />
            <h2>Text-Grading</h2>
            <p>
              The content will be graded and displayed to the user
              and user can ask for any queries.
            </p>
          </div>
        </div>
      </div>
    </section>

    <section class="ourteam" id="members">
      <div class="container text-center">
        <h1>OUR AMAZING TEAM</h1>
        <div class="row teamsetting">
          <div class="col-lg-6 col-md-6 col-sm-6 col-12 d-block m-auto">
            <figure class="figure">
              <img
                src="@/assets/sarvesh.jpg"
                class="figure-img img-fluid rounded-circle"
                height="250px"
                width="250px"
              />
              <figcaption>
                <h4>Sarvesh Purohit</h4>
                <p class="figure-caption">TYCE-2(170410107091)</p>
              </figcaption>
            </figure>
          </div>
          <div class="col-lg-6 col-md-6 col-sm-6 col-12 d-block m-auto">
            <figure class="figure">
              <img
                src="@/assets/nirmal.jpg"
                class="figure-img img-fluid rounded-circle"
                height="250px"
                width="250px"
              />
              <figcaption>
                <h4>Nirmal Rabari</h4>
                <p class="figure-caption">TYCE-2(170410107092)</p>
              </figcaption>
            </figure>
          </div>
        </div>
        <div class="row">
          <div class="col-lg-6 col-md-6 col-sm-6 col-12 d-block m-auto">
            <figure class="figure">
              <img
                src="@/assets/mustan.jpg"
                class="figure-img img-fluid rounded-circle"
                height="250px"
                width="250px"
              />
              <figcaption>
                <h4>Mustanseer Sakerwala</h4>
                <p class="figure-caption">TYCE-2(170410107097)</p>
              </figcaption>
            </figure>
          </div>
          <div class="col-lg-6 col-md-6 col-sm-6 col-12 d-block m-auto">
            <figure class="figure">
              <img
                src="@/assets/avani.jpg"
                class="figure-img img-fluid rounded-circle"
                height="250px"
                width="250px"
              />
              <figcaption>
                <h4>Avani Sanghvi</h4>
                <p class="figure-caption">TYCE-2(170410107099)</p>
              </figcaption>
            </figure>
          </div>
        </div>
      </div>
    </section>

    <footer class="footer">
      <h5 class="text-center">Copyright @ 2020, Designed by TAT</h5>
    </footer>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import MainPagesHeader from '@/components/MainPagesHeader.vue'
export default {
  name: 'Home',
  components: {
    MainPagesHeader
    // HelloWorld
  }
}
</script>

<style scoped>
.bgimg {
  background-image: url("../assets/background.jpg");
  background-size: 100% 100%;
  background-attachment: fixed;
  width: 100%;
  height: 660px;
}
body {
  background-image: url("../assets/login-background.png");
  background-size: 100% 100%;
  background-attachment: fixed;
  color: black;
}
.headerset {
  padding-top: 230px;
  box-sizing: border-box;
}

.headerset h2 {
  font-size: 32px;
}
/* .bgcol{
    background-color:orange;
    background-size:50px 50px;
} */
.headerset h1 {
  font-size: 62px;
}

.ourservices {
  padding: 100px 0px 60px;
  height: 700px;
}

.ourservices p {
  font-size: 22px;
}

.ourservices h1 {
  font-weight: bold;
  font-size: 50px;
  color: orange;
}

.rowsetting {
  margin: 80px 0px !important;
}

.rowsetting h2 {
  /* color: orange; */
  margin-top: 24px;
  font-weight: bold;
  font-size: 30px;
}

.rowsetting p {
  padding: 10px;
  color: #6c757d;
}

.ourteam {
  height: 700px;
  padding: 100px 0px 60px;
  width: 100%;
}

.ourteam h1 {
  font-weight: bold;
  font-size: 50px;
  /* color: orange; */
}

.teamsetting {
  margin-top: 50px;
}

.footer {
  height: 250px;
}

.footer h5 {
  line-height: 250px;
  /* color: orange; */
}

/* figcaption {
  color: orange;
}
.figure-caption {
  color: orange !important;
} */
/*////////////Responsive////////

@media(min-width:992px){

}

@media(min-width:768px) and (max-width:991px){

}

@media(min-width:575px) and (max-width:767px){

}

@media(min-width:480px) and (max-width:574px){

}

@media(max-width:479px){
   .headerset h2{
    font-size:12px;
}

.headerset h1{
    font-size:32px;
}
}*/
</style>
