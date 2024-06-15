import './assets/main.css'
import router from './router';

import { createApp } from 'vue'
import App from './App.vue'
import VueCookies from 'vue3-cookies'
const app = createApp(App);
app.use(router);
app.use(VueCookies);

app.mount('#app');
