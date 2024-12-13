<template>
  <p>Saisissez votre nom</p>
  <input type="text" v-model="username" />
  <button type="button" @click="launchNewQuiz">submit</button>
  <p>{{ username }}</p>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>

<script setup>
import { ref } from 'vue';
import participationStorageService from '@/services/ParticipationStorageService';
import { useRouter } from 'vue-router';

const username = ref('');
const router = useRouter();

function launchNewQuiz() {
  console.log('Launch new quiz with', this.username);
  participationStorageService.savePlayerName(username.value);
  router.push('/questions'); // Remplacez par votre route réelle
}
</script>
