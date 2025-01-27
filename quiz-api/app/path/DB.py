from flask import Blueprint, jsonify
from app.models import rebuild_database  # Assurez-vous que rebuild_database est importé correctement
from flask_cors import cross_origin

# Création du Blueprint pour la gestion de la base de données
db_bp = Blueprint('database', __name__)

@db_bp.route('/rebuild-db', methods=['POST'])
@cross_origin(origin='*')  # Permettre les requêtes Cross-Origin
def rebuild_db_route():
    """
    Route pour reconstruire la base de données.
    """
    try:
        rebuild_database()
        return "Ok", 200

    except Exception as e:
        return jsonify({"error": f"Erreur lors de la reconstruction de la base de données : {str(e)}"}), 500
