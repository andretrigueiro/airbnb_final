<template>
  <div id="main-header">
    <b-navbar toggleable="lg" sticky="true" id="nav-header">
      <b-navbar-brand class="text-modifier" href="#">AirBNB</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="ml-auto">
          <b-nav-item class="text-modifier" href="http://localhost:8080/guest">Guest</b-nav-item>
          <b-nav-item class="text-modifier" href="http://localhost:8080/host">Host</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <!-- <b-nav-form>
            <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
            <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
          </b-nav-form> -->

          <!-- <b-nav-item-dropdown text="Lang" right>
            <b-dropdown-item href="#">EN</b-dropdown-item>
            <b-dropdown-item href="#">PT</b-dropdown-item>
          </b-nav-item-dropdown> -->

          <b-nav-item-dropdown right>
            <!-- Using 'button-content' slot -->
            <template #button-content>
              <div v-if="user_logged_email">
                <strong class="text-modifier">{{ user_logged_email }}</strong>
              </div>
              <div v-else>
                <strong class="text-modifier">User</strong>
              </div>
            </template>
            <b-dropdown-item href="#">Log In</b-dropdown-item>
            <b-dropdown-item href="#">Sign In</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: 'Header',
};
</script>

<style scoped>

#main-header {
  background-color: white;
  margin-bottom: 20px;
  padding-bottom: 5px;
  padding-top: 10px;
  border-bottom: dimgrey;
  border-bottom-width: 1px;
  border-bottom-style: solid;
}

#nav-header {
  margin-left: 5%;
  margin-right: 5%;
  font-size: 18px !important;
  font-weight: 600 !important;
}

.text-modifier{
  color: red !important;
}

.nav-link{
  color: red !important;
}

</style>
