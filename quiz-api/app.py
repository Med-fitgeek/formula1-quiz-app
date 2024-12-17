from flask import Flask, request, jsonify
import hashlib
from jwt_utils import build_token
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('DB.db')
    conn.row_factory = sqlite3.Row 
    return conn

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": 0, "scores": []}, 200

# Authentification
@app.route('/login', methods=['POST'])
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
  
        else : 
            return jsonify({"error": "Mauvais mot de passe"}), 401

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()