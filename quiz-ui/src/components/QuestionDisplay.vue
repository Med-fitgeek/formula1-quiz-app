<template>
  <div class="container">
    <p>{{ currentQuestion.text }}</p>
    <img
      v-if="currentQuestion.image"
      :src="currentQuestion.image"
      alt="Image de la question"
      class="question-image"
    />
    <ul class="quiz-answers">
      <li
        v-for="answer in currentQuestion.possibleAnswers"
        :key="answer.id"
        :class="{ selected: selectedAnswerId === answer.id }"
        class="quiz-answer"
        @click="selectAnswer(answer.id)"
      >
        {{ answer.text }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref } from "vue";

const props = defineProps({
  currentQuestion: Object,
});

const emit = defineEmits(["answer-selected"]);

const selectedAnswerId = ref(null);

function selectAnswer(answerId) {
  selectedAnswerId.value = answerId;

  // Attendre un court délai pour le clignotement avant d'émettre l'événement
  setTimeout(() => {
    emit("answer-selected", answerId);
    selectedAnswerId.value = null; // Réinitialiser après la transition
  }, 300); // Durée du clignotement
}
</script>

<style scoped>

.container {

  max-height: 40%;
  padding-left: 10px;
  padding-right: 10px;
  text-align: center;
}


/* Liste des réponses */
.quiz-answers {
  list-style-type: none;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

img {
  margin-bottom: 12px;
  max-width: 250px;
  min-height: 250px;
}

/* Style des réponses comme des boutons */
.quiz-answer {
  padding: 0px;
  text-align: center;
  font-size: 1rem;
  font-weight: bold;
  color: white;
  background-color: rgba(255, 255, 255, 0.1);
  border: 2px solid rgba(255, 255, 255, 0.2);
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

/* Couleur de fond au survol */
.quiz-answer:hover {
  background-color: #ffde59; /* Fond jaune semi-transparent */
  transform: scale(1.05); /* Agrandir légèrement */
}

/* Effet lorsque la réponse est sélectionnée */
.quiz-answer.selected {
  background-color: rgba(255, 255, 0, 0.6); /* Fond jaune plus opaque */
  animation: flash 0.3s ease-in-out;
}

/* Animation de clignotement */
@keyframes flash {
  0% {
    background-color: rgba(255, 255, 0, 0.6);
  }
  50% {
    background-color: rgba(255, 255, 255, 1);
  }
  100% {
    background-color: rgba(255, 255, 0, 0.6);
  }
}
</style>
