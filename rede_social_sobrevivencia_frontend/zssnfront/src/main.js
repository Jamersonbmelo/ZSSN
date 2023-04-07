import { createApp } from 'vue'
import App from './App.vue'

import './assets/main.css'
import axios from 'axios'

import Vue3EasyDataTable from 'vue3-easy-data-table';
import 'vue3-easy-data-table/dist/style.css';

const app = createApp(App);
app.config.globalProperties.$http = axios
app.component('EasyDataTable',Vue3EasyDataTable);

app.mount('#app')
