export default {
  // Efface les données du joueur et du score
  clear() {
    window.localStorage.removeItem('playerName');
    window.localStorage.removeItem('participationScore');
  },

  // Sauvegarde le nom du joueur dans le local storage
  savePlayerName(playerName) {
    window.localStorage.setItem('playerName', playerName);
  },

  // Récupère le nom du joueur depuis le local storage
  getPlayerName() {
    return window.localStorage.getItem('playerName');
  },

  // Sauvegarde le score de participation dans le local storage
  saveParticipationScore(participationScore) {
    window.localStorage.setItem('participationScore', participationScore);
  },

  // Récupère le score de participation depuis le local storage
  getParticipationScore() {
    const score = window.localStorage.getItem('participationScore');
    return score; // Convertit en nombre si possible
  },
};
