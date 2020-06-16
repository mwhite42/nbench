import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Benchmarks from '../views/Benchmarks.vue';
import Workloads from '../views/Workloads.vue';
import NewWorkload from '../views/NewWorkload.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/benchmarks',
    name: 'Benchmarks',
    component: Benchmarks,
  },
  {
    path: '/workloads',
    name: 'Workloads',
    component: Workloads,
  },
  {
    path: '/newworkload',
    name: 'NewWorkload',
    component: NewWorkload,
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
