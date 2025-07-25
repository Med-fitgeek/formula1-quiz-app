import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../views/HomePage.vue';
import NewQuizPage from '@/views/NewQuizPage.vue';
import QuestionsManager from '@/views/QuestionsManager.vue';
import VotreScore from '@/views/VotreScore.vue';
import Admin from '@/views/Admin.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'HomePage',
      component: HomePage,
    },
    {
      path: '/new-quiz',
      name: 'NewQuizPage',
      component: NewQuizPage,
    },
    {
      path: '/questions',
      name: 'QuestionsManager',
      component: QuestionsManager,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: "/votre-score",
      name: "VotreScore",
      component: VotreScore,
    },
    { path: "/admin",
      name: "Admin", 
      component: Admin },
  ],
});

export default router;
