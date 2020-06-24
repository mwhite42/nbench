import Vue from 'vue';
import axios from 'axios';
import Notifications from 'vue-notification';
import App from './App.vue';
import router from './router';
import './assets/luci.css';

axios.defaults.baseURL = 'http://localhost:5000';
Vue.config.productionTip = false;
Vue.use(Notifications);

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
