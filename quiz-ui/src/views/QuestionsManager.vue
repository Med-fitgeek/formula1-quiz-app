<template>
  <div class="quiz-container">
    <h1 class="quiz-title">Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestions }}</h1>
    <div class="quiz-content">
      <QuestionDisplay
        v-if="currentQuestion"
        :currentQuestion="currentQuestion"
        @answer-selected="answerClickedHandler"
      />
      
      <p v-else class="loading-text">Chargement de la question...</p>
    </div>
    <button
      v-if="quizEnded"
      class="quiz-button"
      @click="handleQuizEnd"
    >
      Terminer le quiz
    </button>
  
  </div>
</template>


<script setup>
import { ref, onMounted } from "vue";
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";
import QuestionDisplay from "@/components/QuestionDisplay.vue";
import { useRouter } from "vue-router";


const router = useRouter();

// Variables réactives
const questions = ref([]);
const selectedAnswers = ref([]); // IDs des réponses sélectionnées
const currentQuestion = ref(null);
const currentQuestionPosition = ref(1);
const totalNumberOfQuestions = ref(0);
const quizEnded = ref(false);

// Charger toutes les questions
onMounted(async () => {
  const response = await quizApiService.getAllQuestions();
  questions.value = response.data;
  totalNumberOfQuestions.value = questions.value.length;
  loadQuestionByPosition(currentQuestionPosition.value);
});

// Charger une question par sa position
async function loadQuestionByPosition(position) {
  const response = await quizApiService.getQuestionByPosition(position);
  currentQuestion.value = response.data;
}



function answerClickedHandler(selectedAnswerId) {
  selectedAnswers.value[currentQuestionPosition.value - 1] = selectedAnswerId;
  

  console.log(`Question ${currentQuestionPosition.value} : Réponse sélectionnée :`, selectedAnswerId);

  if (currentQuestionPosition.value < totalNumberOfQuestions.value) {
    currentQuestionPosition.value++;
    loadQuestionByPosition(currentQuestionPosition.value);
  } else {
    quizEnded.value = true;
  }
}

async function handleQuizEnd() {
  const playerName = localStorage.getItem("playerName") || "Anonyme";

  console.log("Réponses sélectionnées :", selectedAnswers.value);

  try {
    const result = await participationStorageService.sendParticipation(playerName, selectedAnswers.value);
    console.log("Réponse de l'API :", result);

    router.push({
      name: "VotreScore",
      query: {
        score: result.score,
        totalQuestions: totalNumberOfQuestions.value,
        playerName: result.playerName,
      },
    });
  } catch (error) {
    console.error("Erreur lors de la sauvegarde de la participation :", error);
  }
}

</script>




<style scoped>
/* Conteneur principal pour la partie quiz */
.quiz-container {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  background-image: url('@/assets/bg.jpg'); /* Chemin vers votre image */
  background-size: cover; /* L'image couvre tout le conteneur */
  background-position: center; /* Centrer l'image */
  background-repeat: no-repeat; /* Empêche la répétition */
  color: white;
  padding-top: 20px;
  padding-bottom: 20px;
  padding-left: 90px;
  padding-right: 90px;
  border-radius: 10px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
  margin: 20px auto;
  max-width: 700px;
  height: auto;
}


/* Titre de la question */
.quiz-title {
  font-size: 1.8rem;
  margin-bottom: 10px;
  padding-left: 5px;
  padding-right: 5px;
  color: #000;
  text-align: left;
  background-color: #ffde59;
}

/* Contenu du quiz (affichage des questions et réponses) */
.quiz-content {
  background: #333;
  padding: 20px;
  border-radius: 10px;
  margin-bottom: 20px;
  width: 100%;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3);
}

/* Bouton terminer le quiz */
.quiz-button {
  background-color: white;
  color: black;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
  align-self: flex-end;
}

.quiz-button:hover {
  background-color: yellow;
}

/* Texte de chargement */
.loading-text {
  color: #ffcc00;
  font-style: italic;
}
</style>
