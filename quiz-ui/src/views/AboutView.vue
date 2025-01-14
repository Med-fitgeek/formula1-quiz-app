<template>
  <div class="about">
  <h1>À Propos de <span class="game-title">Pole Position</span></h1>
  <p class="intro-text">
    Bienvenue dans le monde palpitant de <strong>Pole Position</strong>, le jeu de quiz ultime pour les passionnés de Formule 1 ! Testez vos connaissances, affrontez vos amis, et découvrez qui mérite la première place sur la grille de départ.
  </p>

  <div class="cta-section">
    <h2>Rejoignez la Course !</h2>
    <p>
      Préparez-vous à prendre la pole position. Chaque question vous rapproche un peu plus de la victoire. Êtes-vous prêt à relever le défi ?
    </p>
    <router-link to="/new-quiz" class="play-now-btn">
      Jouer maintenant !
    </router-link>
  </div>
</div>

</template>

<style>

.about {
  max-width: 800px;
  margin: 0 auto;
  padding-top: 60px;
  padding-bottom: 50px;
  padding-left: 30px;
  padding-right: 30px;
  background-color: #1c1c1c;
  color: #ffffff;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  font-family: 'Arial', sans-serif;
  text-align: center;
}

.game-title {
  color: #ffde59;
  font-size: 2rem;
}

.intro-text {
  margin-bottom: 20px;
  font-size: 1.2rem;
  line-height: 1.6;
}

.team-section, .cta-section {
  margin-top: 50px;
  margin-bottom: 30px;
  padding: 15px;
  background-color: #282828;
  border-radius: 8px;
}

.team-section h2, .cta-section h2 {
  color: #ffde59;
  margin-bottom: 10px;
}

.features-list {
  text-align: left;
  list-style: none;
  padding: 0;
}

.features-list li {
  margin-bottom: 10px;
  line-height: 1.5;
}

.features-list strong {
  color: #ff4b5c;
}


.cta-section {
  background-color: #ff4b5c;
  color: #ffffff;
  border: 2px solid #ffde59;
}

.play-now-btn {
  margin-top: 20px;
  padding: 10px 20px;
  background-color: #ffde59;
  color: #000;
  font-size: 1.1rem;
  font-weight: bold;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.play-now-btn:hover {
  background-color: #d4ae14;
}



</style>
