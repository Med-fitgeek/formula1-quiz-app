<script setup>
import { ref } from "vue";
import QuestionList from "./QuestionList.vue";
import QuestionEdition from "./QuestionEdition.vue";
import { getAuthToken, saveAuthToken, removeAuthToken } from "@/services/AuthService";
import axios from "axios";

const adminMode = ref("list"); // Modes : "list" ou "edit"
const isAuthenticated = ref(!!getAuthToken());
const password = ref("");

async function login() {
  try {
    const response = await axios.post(`${import.meta.env.VITE_API_URL}/login`, {
      password: password.value,
    });

    if (response.status === 200 && response.data.token) {
      saveAuthToken(response.data.token); // Stocker le token dans localStorage
      isAuthenticated.value = true;
      alert("Connexion réussie !");
    } else {
      alert("Échec de la connexion.");
    }
  } catch (error) {
    if (error.response && error.response.status === 401) {
      alert("Mot de passe incorrect !");
    } else {
      console.error("Erreur lors de la connexion :", error);
      alert("Une erreur s'est produite.");
    }
  }
}

function logout() {
  removeAuthToken();
  isAuthenticated.value = false;
  password.value = ""; // Réinitialiser le mot de passe
}
</script>

<template>
  <div class="admin-container">
    <div v-if="!isAuthenticated">
      <h2>Connexion Administration</h2>
      <input v-model="password" type="password" placeholder="Mot de passe" />
      <button class="login-btn" @click="login">Connexion</button>
    </div>

    <div v-else>
      <button class="admin-buttons" @click="logout">Déconnexion</button>
      <button class="admin-buttons" :class="{ active: adminMode === 'list' }" @click="adminMode = 'list'">Liste des Questions</button>
      <button class="admin-buttons" :class="{ active: adminMode === 'edit' }" @click="adminMode = 'edit'">Créer une Question</button>

      <QuestionList v-if="adminMode === 'list'" />
      <QuestionEdition v-if="adminMode === 'edit'" @cancel="adminMode = 'list'" />

    </div>
  </div>
</template>

<style>

    .admin-container {
            padding-bottom: 15pxp;
        }
    .admin-buttons {
        background-color: #fff;
        color: #000;
        border: none;
        padding: 4px;
        margin-right: 8px;
        margin-bottom: 20px;
    }
    .login-btn {
        margin-top: 20px;
        padding: 5px 15px;
        font-size: 1.2em;
        background-color: #ffde59;
        color: black;
        border-radius: 5px;
        text-decoration: none;
        text-align: center;
        display: inline-block;
    }

    .login-btn:hover {
        background-color: #c09e18;
    }

    input {
        width: 50%;
        padding: 8px;
        margin-bottom: 10px;
        margin-right: 10px;
        border: 1px solid #918e8e;
        border-radius: 4px;
        font-size: 14px;
        color: #fff;
        background-color: #282828;
    }

    .admin-buttons.active {
    background-color: #fff; /* Couleur de fond jaune */
    border: 2px solid #d4ae14; /* Bordure jaune foncé */
    transform: scale(1.1); /* Agrandir légèrement */
    font-weight: bold; /* Rendre le texte gras */
    transition: all 0.2s ease-in-out; /* Animation fluide */
    margin-left: 5px;
    margin-right: 15px;

    }

    .admin-buttons.active:hover {
    background-color: #fff; /* Couleur plus foncée au survol */
    }
    
</style>
