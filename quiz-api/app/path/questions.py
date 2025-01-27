from flask import Blueprint, request, jsonify
from app.jwt_utils import build_token, decode_token
from app.auth import authenticate
from app.questions_services import delete_question_by_id_from_db,get_question_by_id_from_db,add_question_to_db, delete_question_by_position_from_db, delete_all_questions_from_db, update_question_in_db,get_quiz_info_from_db, get_all_questions_from_db, get_question_by_position_from_db
import hashlib
from app.models import get_db_connection
from flask_cors import cross_origin


# Créer un Blueprint pour les routes
bp = Blueprint('quiz', __name__)

# 2 - Flask creation
@bp.route('/')
@cross_origin(origin='*')  # Permet toutes les origines

def hello_world():
    x = 'world'
    return f"Hello, {x}"

# 3 - Get Quiz
@bp.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
    try:
        info = get_quiz_info_from_db()
        return jsonify(info), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500



# 4 - Authentification
@bp.route('/login', methods=['POST'])
@cross_origin(origin='*')  # Permet toutes les origines
def post_login():
    try:
        payload = request.get_json()

        if "password" not in payload:
            return jsonify({"error": "Le champ 'password' est manquant"}), 400

        tried_password = payload["password"].encode('utf-8')
        hashed = hashlib.md5(tried_password).digest()


        if hashed == b'\xd8\x17\x06PG\x92\x93\xc1.\x02\x01\xe5\xfd\xf4_@':
            token = build_token()
            
            # Vérification si un objet d'erreur a été retourné
            if isinstance(token, Exception):
                return jsonify({"error": str(token)}), 500
            
            if isinstance(token, bytes):
                token = token.decode('utf-8')
            
            return jsonify({"token": token}), 200
        
        else:
            return jsonify({"error": "Mauvais mot de passe"}), 401

    except AttributeError as e:
        # Capture les erreurs spécifiques
        return jsonify({"error": f"Erreur d'attribut : {str(e)}"}), 500
    except Exception as e:
        # Ajout de la stack trace pour obtenir plus de détails
        import traceback
        error_details = traceback.format_exc()
        return jsonify({"error": f"Erreur inconnue : {error_details}"}), 500

# 5 - Add question (avec authentification)
@bp.route('/questions', methods=['POST'])
@cross_origin(origin='*')  # Permet toutes les origines
def add_question():
    try:
        # Vérifier l'authentification avant de procéder
        auth_response = authenticate()
        if auth_response:  # Si l'authentification échoue, renvoyer la réponse d'erreur
            return auth_response

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


from app.jwt_utils import decode_token
from flask import request, jsonify

# 6 - Delete question
@bp.route('/questions/<int:question_id>', methods=['DELETE'])
@cross_origin(origin='*')  # Permet toutes les origines
def delete_question(question_id):
    """
    Supprime une question par son ID.
    """
    try:
        # Vérifie l'authentification
        auth_response = authenticate()
        if auth_response:  # Si l'authentification échoue, renvoyer la réponse d'erreur
            return auth_response

        # Appelle la fonction pour supprimer la question par son ID
        delete_question_by_id_from_db(question_id)

        # Si la suppression réussit
        return jsonify({"message": f"Question avec l'ID {question_id} supprimée avec succès"}), 204

    except Exception as e:
        # Vérifie si l'erreur concerne une question non trouvée
        if "non trouvée" in str(e).lower():
            return jsonify({"error": f"Erreur lors de la suppression de la question : {str(e)}"}), 404

        # Pour toute autre erreur
        return jsonify({"error": "Une erreur interne est survenue"}), 500



# 7 - Delete all questions
@bp.route('/questions/all', methods=['DELETE'])
@cross_origin(origin='*')  # Permet toutes les origines
def delete_all_questions():
    try:
        # Vérifier l'authentification avant de procéder
        auth_response = authenticate()
        if auth_response:  # Si l'authentification échoue, renvoyer la réponse d'erreur
            return auth_response
        
        # Appeler la fonction du service pour supprimer toutes les questions
        delete_all_questions_from_db()

        return jsonify({"message": "Toutes les questions ont été supprimées avec succès"}), 204

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

# 6 - Update question at position (avec authentification)
@bp.route('/questions/<int:question_id>', methods=['PUT'])
@cross_origin(origin='*')  # Permet toutes les origines
def update_question(question_id):
    try:
        authenticate()  

        payload = request.get_json()
        required_fields = ['title', 'text', 'image', 'position', 'possibleAnswers']

        if not all(field in payload for field in required_fields):
            return jsonify({"error": "Champs manquants"}), 400

        title = payload['title']
        text = payload['text']
        image = payload['image']
        new_position = payload['position']
        possible_answers = payload['possibleAnswers']

        update_question_in_db(question_id, title, text, image, new_position, possible_answers)

        return '', 204

    except Exception as e:

        if "non trouvée" in str(e).lower():
            return jsonify({"error": f"Erreur dans la mise à jour de la question : {str(e)}"}), 404

        return jsonify({"error": "Une erreur interne est survenue"}), 500


@bp.route('/questions', methods=['GET'])
@cross_origin(origin='*')  
def get_questions():
    """
    Récupère toutes les questions ou une question spécifique par sa position.
    """
    position = request.args.get('position') 

    try:
        if position:  
            try:
                position = int(position)
            except ValueError:
                return jsonify({"error": "Le paramètre position doit être un entier valide"}), 400

            question = get_question_by_position_from_db(position)
            if not question:
                return jsonify({"error": f"Question avec la position {position} non trouvée"}), 404

            return jsonify(question), 200
        else:  
            questions = get_all_questions_from_db()
            return jsonify(questions), 200

    except Exception as e:
        if "non trouvée" in str(e):
            return jsonify({"error": str(e)}), 404
        
        return jsonify({"error": "Une erreur interne est survenue"}), 500




@bp.route('/questions/<int:question_id>', methods=['GET'])
@cross_origin(origin='*')  # Permet toutes les origines
def get_question_by_id(question_id):
    """
    Récupère une question spécifique par son id.
    """
    try:
        # Appeler le service pour récupérer une question par id
        question = get_question_by_id_from_db(question_id)
        if question:
            return jsonify(question), 200
        else:
            return jsonify({"error": f"Question avec l'id {question_id} non trouvée"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500
