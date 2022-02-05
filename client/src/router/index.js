import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Host from '../views/HostView.vue';
import Guest from '../views/GuestView.vue';

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
  {
    path: '/guest',
    name: 'Guest',
    component: Guest,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
