<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-12">
        <b-button type="button" size="lg" variant="success" v-b-modal.login-modal pill>
          Log in
        </b-button>
        <b-button type="button" size="lg" variant="primary" v-b-modal.signin-modal pill>
          Sign in
        </b-button>
        <br><br>
      </div>
    </div>
    <!-- LOG IN MODAL -->
    <b-modal ref="LogInModal"
            id="login-modal"
            title="Login"
            hide-footer>
      <b-form @submit="onSubmitLogin" class="w-100">
        <b-form-group id="form-user-group"
                    label="User:"
                    label-for="form-user-input">
          <b-form-input id="form-user-input"
                        type="text"
                        v-model="loginUserForm.user"
                        required
                        placeholder="Enter Username">
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
              :show=5
              dismissible
              variant="sucess"
              v-if="showMessage">
      </alert>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
    return {
      users: [],
      message: '',
      showMessage: false,
      loginUserForm: {
        user: '',
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
  components: {
    alert: Alert,
  },
  methods: {
    getUsers() {
      const path = 'http://localhost:5000/users';
      axios.get(path)
        .then((res) => {
          this.users = res.data.users;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addUser(payload) {
      const path = 'http://localhost:5000/users';
      axios.post(path, payload)
        .then(() => {
          this.getUsers();
          this.message = 'User added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getUsers();
        });
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
    onSubmitLogin(evt) {
      evt.preventDefault();
      this.$refs.LogInModal.hide();
      const payload = {
        user: this.loginUserForm.user,
        password: this.loginUserForm.password,
      };
      this.addUser(payload);
      this.initForm();
    },
    onSubmitSignin(evt) {
      evt.preventDefault();
      // this.$refs.SignInModal.hide();
      const payload = {
        user: this.signinUserForm.user,
        password: this.signinUserForm.password,
        email: this.signinUserForm.password,
        type: this.signinUserForm.type,
      };
      this.addUser(payload);
      this.initForm();
    },
  },
  created() {
    this.getUsers();
  },
};
</script>

<style scoped>

</style>
