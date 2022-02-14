<template>
  <div id="main-header">
    <b-navbar toggleable="lg" sticky id="nav-header">
      <b-navbar-brand class="text-modifier" to="/">AirBNB</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="ml-auto">
          <b-nav-item class="text-modifier" to="/guest" active>Guest</b-nav-item>
          <b-nav-item class="text-modifier" to="/host">Host</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-item-dropdown right>
            <!-- Using 'button-content' slot -->
            <template #button-content>
              <p v-if="user_logged">
                {{ user_logged }}
              </p>
              <p v-else>
                <strong class="text-modifier">User</strong>
              </p>
            </template>
            <b-dropdown-item>
              <b-button type="button" size="sm" variant="success" v-b-modal.login-modal>
                Log in
              </b-button>
            </b-dropdown-item>
            <b-dropdown-item>
              <b-button type="button" size="sm" variant="primary" v-b-modal.signin-modal>
                Sign in
              </b-button>
            </b-dropdown-item>
            <!-- LOG IN MODAL -->
            <b-modal ref="LogInModal"
                    id="login-modal"
                    title="Login"
                    hide-footer>
              <b-form @submit="onSubmitLogin" class="w-100">
                <b-form-group id="form-email-group"
                            label="Email:"
                            label-for="form-email-input">
                  <b-form-input id="form-email-input"
                                type="text"
                                v-model="loginUserForm.email"
                                required
                                placeholder="Enter Email">
                  </b-form-input>
                </b-form-group>
                <b-form-group id="form-password-group"
                              label="Password:"
                              label-for="form-password-input">
                  <b-form-input id="form-password-input"
                                type="text"
                                v-model="loginUserForm.password"
                                required
                                placeholder="Enter Password">
                  </b-form-input>
                </b-form-group>
                <b-button-group>
                  <b-button type="submit" variant="primary">Submit</b-button>
                </b-button-group>
              </b-form>
              <alert  :message=message
                      v-if="showMessage"
              >
              </alert>
            </b-modal>
            <!-- SIGN IN MODAL -->
            <b-modal ref="SignInModal"
                    id="signin-modal"
                    title="Sign In"
                    hide-footer>
              <b-form @submit="onSubmitSignin" class="w-100">
                <b-form-group id="form-user-group"
                            label="User:"
                            label-for="form-user-input">
                  <b-form-input id="form-user-input"
                                type="text"
                                v-model="signinUserForm.user"
                                required
                                placeholder="Enter Username">
                  </b-form-input>
                </b-form-group>
                <b-form-group id="form-password-group"
                              label="Password:"
                              label-for="form-password-input">
                  <b-form-input id="form-password-input"
                                type="text"
                                v-model="signinUserForm.password"
                                required
                                placeholder="Enter Password">
                  </b-form-input>
                </b-form-group>
                <b-form-group id="form-confirm-password-group"
                              label="Confirm Password:"
                              label-for="form-confirm-password-input">
                  <b-form-input id="form-confirm-password-input"
                                type="text"
                                v-model="signinUserForm.confirmPassword"
                                required
                                placeholder="Enter Password Again">
                  </b-form-input>
                </b-form-group>
                <b-form-group id="form-email-group"
                              label="Email:"
                              label-for="form-email-input">
                  <b-form-input id="form-email-input"
                                type="text"
                                v-model="signinUserForm.email"
                                required
                                placeholder="Enter Email">
                  </b-form-input>
                </b-form-group>
                <b-button-group>
                  <b-button type="submit" variant="primary">Submit</b-button>
                </b-button-group>
              </b-form>
              <alert  :message=message
                      v-if="showMessage"
              >
              </alert>
            </b-modal>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>

  </div>
</template>

<script>
import axios from 'axios';
import { mutations } from '../store';
import Alert from './Alert.vue';

export default {
  name: 'Header',
  data() {
    return {
      users: [],
      user_email_logged: '',
      message: '',
      showMessage: true,
      loginUserForm: {
        email: '',
        password: '',
      },
      signinUserForm: {
        user: '',
        password: '',
        confirmPassword: '',
        email: '',
        type: 'guest',
      },
    };
  },
  computed: {
    user_logged() {
      return this.user_email_logged;
    },
  },
  components: {
    alert: Alert,
  },
  methods: {
    setEmailLogger() {
      mutations.setEmailSession(this.user_email_logged);
    },
    getUsers() {
      const path = 'http://localhost:5000/users/all_users';
      axios.get(path)
        .then((res) => {
          this.users = res.data.users;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    registerUser(payload) {
      const path = 'http://localhost:5000/auth/register';
      axios.post(path, payload)
        .then((res) => {
          this.message = res.data.message;
          this.getUsers();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getUsers();
        });
    },
    loginUser(payload) {
      const path = 'http://localhost:5000/auth/login';
      axios.post(path, payload)
        .then((res) => {
          this.message = res.data.message;
          this.user_email_logged = res.data.user_email;
          this.$cookies.set('user_email', this.user_email_logged);
          this.setEmailLogger();
          // console.log(this.user_email_logged);
          // console.log(store.userLogged);
          this.getUsers();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getUsers();
        });
    },
    onSubmitLogin(evt) {
      evt.preventDefault();
      // this.$refs.LogInModal.hide();
      const payload = {
        email: this.loginUserForm.email,
        password: this.loginUserForm.password,
      };
      this.loginUser(payload);
      this.initForm();
    },
    matchPassword(password, confirmPassword) {
      if (password === confirmPassword) {
        return true;
      }
      return false;
    },
    onSubmitSignin(evt) {
      evt.preventDefault();
      // this.$refs.SignInModal.hide();
      if (!this.matchPassword(this.signinUserForm.password, this.signinUserForm.confirmPassword)) {
        this.message = 'Password doesnt match. Try again';
      } else {
        const payload = {
          user: this.signinUserForm.user,
          password: this.signinUserForm.password,
          email: this.signinUserForm.email,
          type: this.signinUserForm.type,
        };
        this.registerUser(payload);
      }
      this.initForm();
    },
    initForm() {
      this.loginUserForm.user = '';
      this.loginUserForm.password = '';
      this.signinUserForm.user = '';
      this.signinUserForm.password = '';
      this.signinUserForm.confirmPassword = '';
      this.signinUserForm.email = '';
      this.signinUserForm.type = 'guest';
    },
  },
  created() {
    this.getUsers();
    this.$cookies.set('user_email', this.user_email_logged);
  },
  updated() {
    this.$cookies.set('user_email', this.user_email_logged);
  },
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

.space{
  margin-left: 10px;
  margin-right: 10px;
}

</style>
