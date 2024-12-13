import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../views/HomePage.vue';
import NewQuizPage from '../views/NewQuizPage.vue';
import questions from '../views/FirstQuestions.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'HomePage',
      component: HomePage,
    },
    {
      path: '/NewQuizPage',
      name: 'NewQuizPage',

      component: NewQuizPage,
    },
    {
      path: '/questions',
      name: 'questions',
      component: questions,
    },
  ],
});

export default router;
