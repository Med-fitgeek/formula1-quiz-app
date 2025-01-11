from flask import Flask
from app.path.questions import bp as quiz_bp
from app.path.participations import bp as participations_bp
from app.models import initialize_database

def create_app():
    app = Flask(__name__)
    
    initialize_database()
    
    # Enregistrer le Blueprint
    app.register_blueprint(quiz_bp, url_prefix='/')
    app.register_blueprint(participations_bp, url_prefix='/')
    
    return app
