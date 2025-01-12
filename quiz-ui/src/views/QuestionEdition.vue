<script setup>
import { ref } from "vue";
import ImageUploader from "@/components/ImageUploader.vue";
import quizApiService from "@/services/QuizApiService";
import { defineEmits } from "vue";

const emit = defineEmits(["cancel"]);


const props = defineProps({
  question: Object, // Si une question existe, elle est transmise en props
});

// Variables locales pour gérer les modifications
const localQuestion = ref({ ...props.question });
const imageBase64 = ref(localQuestion.value.image || "");

// Ajouter une réponse vide si aucune n'existe
if (!localQuestion.value.possibleAnswers) {
  localQuestion.value.possibleAnswers = [];
}

// Ajouter une nouvelle réponse
function addAnswer() {
  localQuestion.value.possibleAnswers.push({ text: "", isCorrect: false });
}

// Supprimer une réponse
function removeAnswer(index) {
  localQuestion.value.possibleAnswers.splice(index, 1);
}


function cancelForm() {
  emit("cancel");
}

// Valider les réponses
function validateQuestion() {
  if (localQuestion.value.possibleAnswers.length === 0) {
    alert("Veuillez ajouter au moins une réponse.");
    return false;
  }
  if (!localQuestion.value.possibleAnswers.some((answer) => answer.isCorrect)) {
    alert("Veuillez marquer au moins une réponse comme correcte.");
    return false;
  }
  return true;
}

import { toRaw } from 'vue';

async function saveQuestion() {
  if (!validateQuestion()) return;

  if (imageBase64.value) {
    localQuestion.value.image = imageBase64.value;
  } else {
    console.warn("Aucune image sélectionnée ou encodée"); // Debug
  }


  // Associer l'image
  localQuestion.value.image = imageBase64.value;

  try {
    // Convertir l'objet réactif en un objet JavaScript pur
    const plainQuestion = toRaw(localQuestion.value);

    if (plainQuestion.id) {
      const response = await quizApiService.updateQuestion(plainQuestion);
      alert("Question mise à jour !");
      console.log("Réponse API :", response.data);
    } else {
      const response = await quizApiService.createQuestion(plainQuestion);
      alert("Nouvelle question créée !");
      console.log("Réponse API :", response.data);
    }    
  } catch (error) {
    console.error("Erreur lors de la sauvegarde :", error);
    alert("Une erreur est survenue lors de la sauvegarde.");
  }
}

function handleFileChange(base64Image) {
  console.log("Image reçue (base64) :", base64Image); // Vérification
  imageBase64.value = base64Image;
}

</script>

<template>
  <div class="question-edition-container">
    <h2>Éditer une Question</h2>

    <!-- Titre de la question -->
    <label for="title">Titre</label>
    <input id="title" v-model="localQuestion.title" placeholder="Titre de la question" />

    <!-- Texte de la question -->
    <label for="text">Texte</label>
    <textarea id="text" v-model="localQuestion.text" placeholder="Texte de la question"></textarea>

    <!-- Position de la question -->
    <label for="position">Position de la question</label>
    <input id="position" v-model="localQuestion.position" placeholder="Position de la question" />

    <!-- Gestion de l'image -->
    <label>Image</label>
    <ImageUploader @file-change="handleFileChange" />


    <!-- Liste des réponses -->
    <h3>Réponses possibles</h3>
    <ul class="answers-list">
      <li v-for="(answer, index) in localQuestion.possibleAnswers" :key="index" class="answer-item">
        <input
          class="answer-text"
          v-model="answer.text"
          placeholder="Texte de la réponse"
        />
        <label class="correct-checkbox">
          <input
            type="checkbox"
            v-model="answer.isCorrect"
          />
          Correcte
        </label>
        <button @click="removeAnswer(index)" class="delete-btn">Supprimer</button>
      </li>
    </ul>
    <button @click="addAnswer" class="add-answer-btn">Ajouter une réponse</button>

    <!-- Bouton de sauvegarde -->
    <button @click="saveQuestion" class="save-btn">Sauvegarder</button>

    <!-- Bouton Annuler -->
    <button @click="cancelForm" class="delete-form-btn">Annuler</button>

  </div>
</template>

<style scoped>
.question-edition-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  background-color: #282828;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

h2 {
  text-align: center;
  margin-bottom: 20px;
  color: #918e8e;
}

label {
  font-weight: bold;
  display: block;
  margin-top: 10px;
  margin-bottom: 5px;
}

input,
textarea {
  width: 100%;
  padding: 8px;
  margin-bottom: 10px;
  border: 1px solid #918e8e;
  border-radius: 4px;
  font-size: 14px;
  background-color: #282828;
}

textarea {
  min-height: 80px;
}

.answers-list {
  list-style: none;
  padding: 0;
  margin: 10px 0;
}

.answer-item {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.answer-text {
  flex: 1;
  padding: 8px;
  margin-right: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.correct-checkbox {
  display: flex;
  align-items: center;
  gap: 5px;
  margin-right: 10px;
}

.add-answer-btn,
.save-btn,
.delete-btn,
.delete-form-btn {
  background-color: #ffde59;
  color: #000;
  border: none;
  border-radius: 4px;
  padding: 8px 12px;
  font-size: 14px;
  cursor: pointer;
  transition: background-color 0.2s ease;
  margin-right: 10px;
}

.add-answer-btn:hover,
.save-btn:hover,
.delete-btn:hover {
  background-color: #cba718;
}

.delete-btn, .delete-form-btn  {
  background-color: #dc3545;
}

.delete-btn:hover, .delete-form-btn:hover {
  background-color: #a71d2a;
}
</style>
