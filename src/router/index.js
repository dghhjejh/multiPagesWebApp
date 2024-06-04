import { createRouter, createWebHistory } from 'vue-router';
import MyHome from '../components/MyHome.vue';
import AboutSite from '../components/AboutSite.vue';
import CardGrids from '../components/CardGrids.vue';
const routes = [
  {
    path: '/',
    name: 'myhome',
    component: MyHome
  },
  {
    path: '/AboutSite',
    name: 'AboutSite',
    component: AboutSite
  },
  {
    path: '/CardGrids',
    name: 'CardGrids',
    component: CardGrids
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;