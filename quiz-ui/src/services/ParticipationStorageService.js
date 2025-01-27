import axios
 from "axios";
export default {
  clear() {
    window.localStorage.clear();
  },
  savePlayerName(playerName) {
    window.localStorage.setItem('playerName', playerName);
  },
  getPlayerName() {
    return window.localStorage.getItem('playerName');
  },
  saveParticipationScore(participationScore) {
    window.localStorage.setItem('participationScore', participationScore);
  },


  async getParticipations() {
    try {
      const response = await axios.get(`${import.meta.env.VITE_API_URL}/participations`);
      return response.data; // Retourne les données du serveur
    } catch (error) {
      console.error("Erreur lors de la récupération des participations :", error);
      throw error; // Lance une exception pour permettre au composant de la gérer
    }
  },
  

  async sendParticipation(playerName, answers) {
    const payload = {
      playerName: playerName,
      answers: answers,
    };
  
    console.log("Payload envoyé :", payload);
  
    try {
      const response = await axios.post(`${import.meta.env.VITE_API_URL}/participations`, payload);
      console.log("Réponse reçue :", response.data);
      return response.data;
    } catch (error) {
      console.error("Erreur lors de l'envoi des participations :", error.response?.data || error);
      throw error;
    }
  }  
};
