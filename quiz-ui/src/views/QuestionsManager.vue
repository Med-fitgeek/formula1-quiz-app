<template>
  <div>
    <h1>
      Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestions }}
    </h1>
    <QuestionDisplay
      :currentQuestion="currentQuestion"
      @answer-selected="answerClickedHandler"
    />
    <button v-if="quizEnded" @click="endQuiz">Terminer le Quiz</button>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import QuestionDisplay from '@/components/QuestionDisplay.vue';
import quizApiService from '@/services/QuizApiService';

// Références réactives
const currentQuestion = ref(null);
const currentQuestionPosition = ref(1);
const totalNumberOfQuestions = ref(0);
const quizEnded = ref(false);

// Initialisation du composant
onMounted(async () => {
  const quizInfo = await quizApiService.getQuizInfo();
  totalNumberOfQuestions.value = quizInfo.totalQuestions;
  loadQuestionByPosition(currentQuestionPosition.value);
});

// Méthodes principales
async function loadQuestionByPosition(position) {
  currentQuestion.value = await quizApiService.getQuestion(position);
}

function answerClickedHandler(selectedAnswer) {
  console.log(`Réponse sélectionnée : ${selectedAnswer}`);
  if (currentQuestionPosition.value < totalNumberOfQuestions.value) {
    currentQuestionPosition.value++;
    loadQuestionByPosition(currentQuestionPosition.value);
  } else {
    quizEnded.value = true;
  }
}

function endQuiz() {
  console.log('Quiz terminé !');
  // Logique supplémentaire pour gérer la fin du quiz
}
</script>
