<script setup>
import { ref, onMounted } from 'vue';
import participationStorageService from '@/services/ParticipationStorageService';

const registeredParticipations = ref([]);

onMounted(async () => {
  try {
    const response = await participationStorageService.getParticipations();
    console.log("Participations récupérées :", response);

    if (response && response.length > 0) {
      registeredParticipations.value = response;
    } else {
      console.warn("Aucune participation trouvée.");
    }
  } catch (error) {
    console.error("Erreur lors de la récupération des scores :", error);
  }
});

</script>

<template>
  <div class="container mt-4">
    <h1 class="text-center">Accueil</h1>
    <h2 class="text-secondary">Les meilleurs scores enregistrés :</h2>
    <div v-if="registeredParticipations.length > 0" class="list-group">
      <div
        v-for="scoreEntry in registeredParticipations"
        v-bind:key="scoreEntry.date"
        class="list-group-item d-flex justify-content-between align-items-center"
      >
        <span>{{ scoreEntry.playerName }}</span>
        <span class="badge bg-success">score : {{ scoreEntry.score }}</span>
      </div>
    </div>
    <div v-else class="alert alert-warning mt-3">
      Aucun score enregistré pour le moment.
    </div>
    <router-link to="/new-quiz" class="start-quiz-btn btn btn-primary mt-4">
      Démarrer le quiz !
    </router-link>
  </div>
</template>

<style scoped>
.text-center {
  color: #ffde59;
}
.score-entry {
  margin-bottom: 10px;
  font-size: 1.2em;
}

.start-quiz-btn {
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

.start-quiz-btn:hover {
  background-color: #c09e18;
}
</style>
