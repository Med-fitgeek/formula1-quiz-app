from flask import Blueprint, request, jsonify
from app.jwt_utils import build_token, decode_token
from app.auth import authenticate
from app.questions_services import add_question_to_db, get_all_questions_from_db, get_question_by_position_from_db, update_question_in_db, delete_question_from_db, delete_all_questions_from_db
import hashlib

# Créer un Blueprint pour les routes
bp = Blueprint('quiz', __name__)

# 2 - Flask creation
@bp.route('/')
def hello_world():
    x = 'world'
    return f"Hello, {x}"

# 3 - Get Quiz
@bp.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
    return {"size": 0, "scores": []}, 200

# 4 - Authentification
@bp.route('/login', methods=['POST'])
def post_login():
    try:
        payload = request.get_json()

        if "password" not in payload:
            return jsonify({"error": "Le champ 'password' est manquant"}), 400

        tried_password = payload["password"].encode('utf-8')
        hashed = hashlib.md5(tried_password).digest()

        if hashed == b'\xd8\x17\x06PG\x92\x93\xc1.\x02\x01\xe5\xfd\xf4_@':
            token = build_token()
            return jsonify({"token": token}), 200

        else:
            return jsonify({"error": "Mauvais mot de passe"}), 401

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 5 - Add question (avec authentification)
@bp.route('/questions', methods=['POST'])
def add_question():
    try:
        authenticate()

        payload = request.get_json()

        # Vérification des champs requis
        if not all(key in payload for key in ['title', 'text', 'image', 'position', 'possibleAnswers']):
            return jsonify({"error": "Champs manquants"}), 400

        # Extraire les données
        title = payload['title']
        text = payload['text']
        image = payload['image']
        position = payload['position']
        possible_answers = payload['possibleAnswers']

        # Appeler la fonction du service pour ajouter la question
        question_id = add_question_to_db(title, text, image, position, possible_answers)

        # Retourner l'ID de la question créée
        return jsonify({"id": question_id}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@bp.route('/questions', methods=['GET'])
def get_all_questions():
    """
    Récupère toutes les questions avec leurs réponses associées.
    """
    try:
        # Appeler le service pour récupérer toutes les questions
        questions = get_all_questions_from_db()
        return jsonify(questions), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@bp.route('/questions/<int:position>', methods=['GET'])
def get_question_by_position(position):
    """
    Récupère une question spécifique par sa position.
    """
    try:
        # Appeler le service pour récupérer une question par position
        question = get_question_by_position_from_db(position)
        return jsonify(question), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500



@bp.route('/questions/<int:id>', methods=['PUT'])
def update_question(id):
    """
    Met à jour une question spécifique avec ses réponses associées.
    """
    try:
        authenticate()

        payload = request.get_json()

        # Vérification des champs requis
        if not all(key in payload for key in ['title', 'text', 'image', 'position', 'possibleAnswers']):
            return jsonify({"error": "Champs manquants"}), 400

        # Extraire les données
        title = payload['title']
        text = payload['text']
        image = payload['image']
        position = payload['position']
        possible_answers = payload['possibleAnswers']

        # Appeler le service pour mettre à jour la question
        update_question_in_db(id, title, text, image, position, possible_answers)

        return jsonify({"message": f"Question avec ID {id} mise à jour avec succès"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# 6 - Delete question
@bp.route('/questions/<int:id>', methods=['DELETE'])
def delete_question(id):
    try:
        authenticate()

        # Appeler la fonction du service pour supprimer la question
        delete_question_from_db(id)

        return jsonify({"message": f"Question avec id {id} supprimée avec succès"}), 204

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 7 - Delete all questions
@bp.route('/questions/all', methods=['DELETE'])
def delete_all_questions():
    try:
        authenticate()

        # Appeler la fonction du service pour supprimer toutes les questions
        delete_all_questions_from_db()

        return jsonify({"message": "Toutes les questions ont été supprimées avec succès"}), 204

    except Exception as e:
        return jsonify({"error": str(e)}), 500
