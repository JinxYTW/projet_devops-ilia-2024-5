from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from datetime import timedelta
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
jwt = JWTManager(app)

users_db = {}


# Endpoint pour l'inscription
@app.route("/auth/sign_in", methods=["POST"])
def sign_in():
    data = request.get_json()
    nom = data.get("nom")
    prenom = data.get("prenom")
    email = data.get("email")
    password = data.get("password")
    username = data.get("username")
    pseudo = data.get("pseudo")

    if not all([nom, prenom, email, password, username, pseudo]):
        return jsonify({"message": "Tous les champs sont obligatoires"}), 400

    if username in users_db:
        return jsonify({"message": "Nom d'utilisateur déjà pris"}), 400

    user = {
        "nom": nom,
        "prenom": prenom,
        "email": email,
        "password": password,
        "username": username,
        "pseudo": pseudo,
    }

    users_db[username] = user
    access_token = create_access_token(identity=username)
    return jsonify({"token": access_token}), 200


# Endpoint pour la connexion
@app.route("/auth/login", methods=["POST"])
def login():
    data = request.get_json()
    username_or_email = data.get("username_or_email")
    password = data.get("password")

    if not username_or_email or not password:
        return jsonify({"message": "Nom d'utilisateur ou mot de passe requis"}), 400

    for user in users_db.values():
        if (
                (user["email"] == username_or_email or user["username"] == username_or_email)
                and user["password"] == password
        ):
            access_token = create_access_token(identity=user["username"])
            return jsonify({"token": access_token}), 200

    return jsonify({"message": "Nom d'utilisateur ou mot de passe incorrect"}), 400


if __name__ == "__main__":
    app.run(debug=True)
