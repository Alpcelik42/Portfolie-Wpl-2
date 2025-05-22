import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MijnVerhaalView from "@/views/MijnVerhaalView.vue";
import ExpertiseView from "@/views/ExpertiseView.vue";
import CreatiesView from "@/views/CreatiesView.vue";
import ContactView from "@/views/ContactView.vue";


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/mijn-verhaal',
      name: 'mijn-verhaal',
      component: MijnVerhaalView
    },
    {
      path: '/expertise',
      name: 'expertise',
      component: ExpertiseView
    },
    {
      path: '/creaties',
      name: 'creaties',
      component: CreatiesView
    },
    {
      path: '/contact',
      name: 'contact',
      component: ContactView
    },
  ],
})

export default router
