import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Host from '../views/HostView.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/host',
    name: 'Host',
    component: Host,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;