import { createRouter, createWebHashHistory } from 'vue-router';

import Base from './components/Base.vue';
import Auth from './components/Auth.vue';
import Graf from './components/Graf.vue';
export default createRouter({
    history: createWebHashHistory(),
    routes: [
        {name: 'base', path: '', component: Base},
        {name: 'auth', path: '/auth/', component: Auth},
        {name: 'stat', path: '/stat/', component: Graf},
        
    ]
})