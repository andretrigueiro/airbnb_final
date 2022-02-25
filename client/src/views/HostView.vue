<template>
  <div class="host-interface">
    <h1>Host Interface</h1>
    <h2>{{ user_logged }}</h2>
    <div>
      <b-button type="button" variant="primary" size="lg" v-b-modal.registerPlace-modal>
        Cadastrar nova casa</b-button>
    </div>
    <!-- REGISTER PLACE -->
    <b-modal ref="RegisterPlaceModal"
            id="registerPlace-modal"
            title="Register Place"
            hide-footer>
      <b-form @submit="onSubmitRegisterPlace" class="w-100">
        <b-form-group id="form-name-group"
                    label="Name:"
                    label-for="form-name-input">
          <b-form-input id="form-name-input"
                        type="text"
                        v-model="registerPlaceForm.placeName"
                        required
                        placeholder="Enter Name">
          </b-form-input>
        </b-form-group>
        <b-form-group label="Type:" v-slot="{ ariaDescribedby }">

          <b-form-radio name="place-type"
          v-model="registerPlaceForm.type"
          :aria-describedby="ariaDescribedby"
          value="House">
            House
          </b-form-radio>

          <b-form-radio name="place-type"
          v-model="registerPlaceForm.type"
          :aria-describedby="ariaDescribedby"
          value="Apartment">
            Apartment
          </b-form-radio>

        </b-form-group>

        <b-form-file
          v-model="file1"
          :state="Boolean(file1)"
          placeholder="Choose a file or drop it here..."
          drop-placeholder="Drop file here..."
        >
        </b-form-file>

        <b-form-file
          v-model="file2"
          :state="Boolean(file2)"
          placeholder="Choose a file or drop it here..."
          drop-placeholder="Drop file here..."
        >
        </b-form-file>

        <b-form-file
          v-model="file3"
          :state="Boolean(file3)"
          placeholder="Choose a file or drop it here..."
          drop-placeholder="Drop file here..."
        >
        </b-form-file>

        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
        </b-button-group>
      </b-form>
      <alert  :message=message
              v-if="showMessage"
      >
      </alert>
    </b-modal>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios';
import Alert from '@/components/Alert.vue';
import { store } from '../store';

export default {
  data() {
    return {
      user_email_logged: '',
      file1: null,
      file2: null,
      file3: null,
      message: '',
      showMessage: true,
      registerPlaceForm: {
        placeName: '',
        placeOnwer: '',
        type: '',
        adress: '',
        number: '',
      },
    };
  },
  computed: {
    user_logged() {
      return store.userLogged;
    },
  },
  components: {
    alert: Alert,
  },
  methods: {
    checkUser() {
      if (!this.$cookies.get('user_email')) {
        return false;
      }
      return true;
    },
    uploadPlaceFile(payload) {
      const path = 'http://localhost:5000/files/upload';
      axios.post(path, payload)
        .then((res) => {
          this.message = res.data.message;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    uploadPlaceFileTest() {
      const path = 'http://localhost:5000/files/upload';
      console.log(this.file1);
      axios.post(path, this.file1)
        .then((res) => {
          this.message = res.data.message;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    onSubmitRegisterPlace(evt) {
      evt.preventDefault();
      // this.$refs.LogInModal.hide();
      const payload = {
        onwer: this.$cookies.get('user_email'),
        name: this.registerPlaceForm.placeName,
        type: this.registerPlaceForm.type,
        file: this.file1,
        // file2: this.file2,
        // file3: this.file3,
      };
      console.log(payload);
      // this.uploadPlaceFile(payload);
      this.uploadPlaceFileTest();
      this.initForm();
    },
    initForm() {
      this.registerPlaceForm.placeName = '';
      this.registerPlaceForm.placeOnwer = '';
      this.registerPlaceForm.type = '';
      this.registerPlaceForm.adress = '';
      this.registerPlaceForm.number = '';
      this.file1 = null;
      this.file2 = null;
      this.file3 = null;
    },
  },
};
</script>

<style scoped>

.b-form-file{
  margin-bottom: 5px;
}

</style>
