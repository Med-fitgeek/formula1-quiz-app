<template>
    <div class="score-container">
      <h1>Votre Score</h1>
      <p>Félicitations {{ playerName }} !</p>
      <p>Votre score : {{ score }} / {{ totalQuestions }}</p>
      <div class="actions">
        <button @click="restartQuiz" class="btn-rejouer">Rejouer</button>
        <button @click="goHome" class="btn-home">Retour à l'accueil</button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { useRouter, useRoute } from "vue-router";
  
  const router = useRouter();
  const route = useRoute();
  
  // Récupération des données passées via la route
  const score = route.query.score || 0; // Le score passé par la route
  const totalQuestions = route.query.totalQuestions || 10; // Exemple de total
  const playerName = route.query.playerName || "Anonyme"; // Nom du joueur par défaut
  
  // Méthode pour rejouer
  function restartQuiz() {
    router.push("/"); // Redirige vers la page d'accueil ou de démarrage du quiz
  }
  
  // Méthode pour retourner à l'accueil
  function goHome() {
    router.push("/"); // Redirige vers la page d'accueil
  }
  </script>
  
  <style scoped>
  .score-container {
    text-align: center;
    padding: 20px;
    background: #222;
    color: white;
    border-radius: 10px;
    max-width: 500px;
    margin: 0 auto;
  }
  
  h1 {
    color: #ffd700; 
  }
  
  .actions {
    margin-top: 20px;
  }
  
  .btn-rejouer,
  .btn-home {
    margin: 10px;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
  }
  
  .btn-rejouer {
    background-color: #28a745;
    color: white;
  }
  
  .btn-rejouer:hover {
    background-color: #218838;
  }
  
  .btn-home {
    background-color: #007bff;
    color: white;
  }
  
  .btn-home:hover {
    background-color: #0056b3;
  }
  </style>
  