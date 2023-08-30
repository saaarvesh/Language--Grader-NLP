<template>
  <div>
    <div id="footer">
      <div class="support" style="float:left;width: 100%;">
        <h5>
          <b>Support</b>
        </h5>
        <div class="link-holder">
          <div class="inside-links">
            <i class="fa fa-user" aria-hidden="true"></i>
            <a href="#">About Us</a>
          </div>
          <br />
          <div class="inside-links">
            <i class="fa fa-address-card" aria-hidden="true"></i>
            <a href="#">Contact Us</a>
          </div>
          <br />
          <div class="inside-links">
            <i class="fa fa-file-text-o" aria-hidden="true"></i>
            <a href="#">Terms And Conditions</a>
          </div>
        </div>
      </div>
      <br />
      <div style="float:left;width: 100%;">
        <h5>
          <b>Community</b>
        </h5>
        <div class="link-holder">
          <div class="inside-links">
            <i class="fa fa-facebook-official" aria-hidden="true"></i>
            <a href="#">&nbsp;&nbsp;&nbsp;&nbsp; Facebook</a>
            <br />
          </div>
          <div class="inside-links">
            <i class="fa fa-instagram" aria-hidden="true"></i>&nbsp;&nbsp;&nbsp;&nbsp;
            <a href="#">Instagram</a>
            <br />
          </div>
          <div class="inside-links">
            <i class="fa fa-linkedin-square" aria-hidden="true"></i>&nbsp;&nbsp;&nbsp;&nbsp;
            <a href="#">Linkedln</a>
            <br />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
#footer {
  color: white;
  width: 100%;
  margin-top: 5em;
  margin-bottom: 0px;
  display: flex;
  padding: 10px;
  border-top: 1px solid white;
}
.inside-links {
  align-content: center;
  float: left;
  margin: 5px;
  width: 30%;
}
.link-holder {
  display: flex;
  align-content: center;
}
.support {
  border-right: 1px solid white;
}
</style>
