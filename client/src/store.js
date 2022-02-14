import Vue from 'vue';

export const store = Vue.observable({
  userLogged: '',
});

export const mutations = {
  setEmailSession(passedEmail) {
    store.userLogged = passedEmail;
  },
};
