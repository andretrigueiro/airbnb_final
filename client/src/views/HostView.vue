<template>
  <div class="host-interface">
    <h1>Host Interface</h1>
    <h2>{{ user_logged }}</h2>
    <div>
      <b-button variant="primary" size="lg">Cadastrar nova casa</b-button>
    </div>
    <hr><br><br>
  </div>
</template>

<script>
// @ is an alias to /src
import { store } from '../store';

export default {
  data() {
    return {
      user_email_logged: '',
    };
  },
  computed: {
    user_logged() {
      return store.userLogged;
    },
  },
};
</script>
