<script setup>
import { ref, onMounted } from "vue";
import quizApiService from "@/services/QuizApiService";
import QuestionEdition from "./QuestionEdition.vue";

const questions = ref([]);
const editingQuestion = ref(null); // Question actuellement en cours d'édition

// Charger toutes les questions à l'initialisation
onMounted(async () => {
  const response = await quizApiService.getAllQuestions();
  if (response && response.data) {
    questions.value = response.data;
  }
});

// Supprimer une question
function deleteQuestion(id) {
  if (confirm("Supprimer cette question ?")) {
    quizApiService.deleteQuestion(id).then(() => {
      questions.value = questions.value.filter((q) => q.id !== id);
      window.location.reload();
    });
  }
}

// Activer le mode édition
function editQuestion(question) {
  editingQuestion.value = { ...question }; // Créer une copie locale pour l'édition
}

// Annuler le mode édition
function cancelEdit() {
  editingQuestion.value = null;
}

// Sauvegarder une question après édition
async function saveQuestion(updatedQuestion) {
  await quizApiService.updateQuestion(updatedQuestion);
  const index = questions.value.findIndex((q) => q.id === updatedQuestion.id);
  if (index !== -1) {
    questions.value[index] = { ...updatedQuestion }; // Mettre à jour la liste des questions
  }
  editingQuestion.value = null; // Quitter le mode édition
}
</script>

<template>
  <div class="questions-list-container">
    <h2>Liste des Questions</h2>

    <ul class="questions-list">
      <li v-for="question in questions" :key="question.id" class="question-item">
        <!-- Mode édition -->
        <div v-if="editingQuestion && editingQuestion.id === question.id">
          <QuestionEdition
            :question="editingQuestion"
            @save="saveQuestion"
            @cancel="cancelEdit"
          />
        </div>
        
        <!-- Mode affichage -->
        <div class="question-line" v-else>
          <div class="question-line-element">
            <span class="question-text">{{ question.text }}</span>
          </div>
          <div class="question-line-element">
            <button class="edit-btn" @click="editQuestion(question)"><i class="fas fa-pencil-alt"></i> <!-- Icône de crayon --></button>
            <button class="delete-btn" @click="deleteQuestion(question.position)"> <i class="fas fa-trash"></i> <!-- Icône de poubelle --></button>
          </div>       
        </div>
      </li>
    </ul>
  </div>
</template>

<style scoped>
.questions-list-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: #282828;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

h2 {
  text-align: center;
  color: #918e8e;
}

.questions-list {
  list-style: none;
  padding: 0;
  margin: 20px 0;
}

.question-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 5px;
  margin-bottom: 5px;
  background-color: #282828;
  border: 1px solid #000;
  border-radius: 4px;
}

.question-text {
  flex: 1;
  margin-right: 10px;
}

.edit-btn,
.delete-btn {
  background-color: #ffde59;
  color: #000;
  border: none;
  border-radius: 4px;
  padding: 4px;
  font-size: 11px;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.edit-btn:hover {
  background-color: #d4ae14;
}

.delete-btn {
  background-color: #dc3545;
  margin-left: 10px;
}

.delete-btn:hover {
  background-color: #a71d2a;
}

.question-line {
  display: flex;
  width: 100%;
  flex-direction: row;
  justify-content: space-between;
  align-items: center; /* Assure l'alignement vertical des éléments */
  margin-top: 2px;
  margin-bottom: 2px;
}


</style>
