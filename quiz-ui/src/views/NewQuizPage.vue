<template>
  <div class="container mt-5">
    <h1 class="text-center">Démarrer un nouveau quiz</h1>
    <form class="mt-4">
      <div class="mb-3">
        <label for="username" class="form-label">Nom du joueur :</label>
        <input
          type="text"
          id="username"
          class="form-control"
          placeholder="Entrez votre nom"
          v-model="username"
        />
        <p>{{ username }}</p>
      </div>
      <button type="button" class="btn" @click="launchNewQuiz">
        Démarrer le quiz
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import participationStorageService from '@/services/ParticipationStorageService';
import { useRouter } from 'vue-router';

const router = useRouter();

const username = ref(''); // Variable pour stocker le nom du joueur

function launchNewQuiz() {
  if (username.value.trim()) {
    participationStorageService.savePlayerName(username.value.trim());
    console.log('Nom du joueur sauvegardé :', username.value);
    router.push('/questions');
  } else {
    alert('Veuillez entrer un nom !');
  }
}
</script>

<style>
.btn {
  margin-top: 20px;
  padding: 10px 20px;
  font-size: 1.2em;
  background-color: #ffde59;
  color: black;
  border-radius: 5px;
  text-decoration: none;
  text-align: center;
  display: inline-block;
}

.btn:hover {
  background-color: #ffde59;
}
</style>
