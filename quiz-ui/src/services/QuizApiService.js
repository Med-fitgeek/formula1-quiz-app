import axios from 'axios';

console.log("Base URL utilisée par Axios :", import.meta.env.VITE_API_URL);

const instance = axios.create({
  baseURL: `${import.meta.env.VITE_API_URL}`,
  json: true,
});

export default {
  async call(method, resource, data = null, token = null) {
    var headers = {
      'Content-Type': 'application/json',
    };
    if (token != null) {
      headers.authorization = 'Bearer ' + token;
    }

    return instance({
      method,
      headers: headers,
      url: resource,
      data,
    })
      .then((response) => {
        return { status: response.status, data: response.data };
      })
      .catch((error) => {
        console.error(error);
      });
  },


  getQuizInfo() {
    return this.call('get', 'quiz-info');
  },

  


  // Récupérer une question par sa position
  getQuestionByPosition(position) {
    return this.call('get', `questions/${position}`); // Remplacez par le chemin correct
  },


  async getAllQuestions() {
    return await axios.get(`${import.meta.env.VITE_API_URL}/questions`);
  },
  async deleteQuestion(id) {
    return await axios.delete(`${import.meta.env.VITE_API_URL}/questions/${id}`);
  },
  async createQuestion(question) {
    return await axios.post(`${import.meta.env.VITE_API_URL}/questions`, question);
  },
  async updateQuestion(question) {
    return await axios.put(`${import.meta.env.VITE_API_URL}/questions/${question.id}`, question);
  },
};
