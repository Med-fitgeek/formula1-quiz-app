<script setup>
import { ref, onMounted } from 'vue';
import quizApiService from '@/services/QuizApiService';
const registeredScores = ref([]);
onMounted(async () => {
  console.log('Home page mounted');
  try {
    // Appel du service pour récupérer les scores
    const scores = await quizApiService.getScores(); // Remplacez 'getScores' par la méthode réelle du service
    registeredScores.value = scores; // Met à jour la valeur
  } catch (error) {
    console.error('Erreur lors du chargement des scores :', error);
  }
});
</script>
<style></style>
<template>
  <h1>Home page</h1>
  <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
    {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
  </div>
  <Routerlink to="/new-quiz">Démarrer le quiz !</Routerlink>
</template>
