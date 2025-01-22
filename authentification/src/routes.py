<<<<<<< HEAD
from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from config import app, db
from models.example_model import User

=======
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from config import db, app
from models.user import User

route = Blueprint('routes', __name__, static_folder='static', template_folder='templates')
>>>>>>> a923ddb4265fa7fb55e2cf1284655155a0c2f14a

@jwt_required()
def refresh_token_if_needed():
    current_user = get_jwt_identity()
    new_token = create_access_token(identity=current_user)
    return jsonify({"new_token": new_token}), 200


# Endpoint pour l'incription
<<<<<<< HEAD
@app.route("/auth/sign_in", methods=["POST"])
=======
@route.route("/auth/sign_in", methods=["POST"])
>>>>>>> a923ddb4265fa7fb55e2cf1284655155a0c2f14a
def sign_in():
    data = request.get_json()
    if not data:
        return jsonify({"message": "Données manquantes"}), 400

<<<<<<< HEAD
    nom = data.get("nom")
    prenom = data.get("prenom")
=======
    nom = data.get("lastName")
    prenom = data.get("firstName")
>>>>>>> a923ddb4265fa7fb55e2cf1284655155a0c2f14a
    email = data.get("email")
    password = data.get("password")
    username = data.get("username")
    pseudo = data.get("pseudo")

    if not all([nom, prenom, email, password, username, pseudo]):
        return jsonify({"message": "Tous les champs sont obligatoires"}), 400

<<<<<<< HEAD
    if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        return jsonify({"message": "Nom d'utilisateur ou email déjà utilisé"}), 409

    new_user = User(nom=nom, prenom=prenom, email=email, password=password, username=username, pseudo=pseudo)
=======
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Nom d'utilisateur déjà utilisé"}), 409
    elif  User.query.filter_by(email=email).first():
        return jsonify({"message": "Email déjà utilisé"}), 409

    new_user = User(last_name=nom, first_name=prenom, email=email, username=username, pseudo=pseudo)
    new_user.set_password(password)
>>>>>>> a923ddb4265fa7fb55e2cf1284655155a0c2f14a
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Utilisateur créé avec succès"}), 200


# Endpoint pour la connexion
<<<<<<< HEAD
@app.route("/auth/login", methods=["POST"])
def login():
    data = request.get_json()
    username_or_email = data.get("username_or_email")
    password = data.get("password")

    if not username_or_email or not password:
        return jsonify({"message": "Nom d'utilisateur ou mot de passe requis"}), 400

    user = User.query.filter((User.username == username_or_email) | (User.email == username_or_email)).first()
    if user and user.password == password:
=======
@route.route("/auth/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    id = ""
    if not username and email:
        id = email
    elif not email and username:
        id = username
    else:
         return jsonify({"message": "Nom d'utilisateur (ou l'email) requis"}), 400

    password = data.get("password")

    if not password:
        return jsonify({"message": "Nom d'utilisateur ou mot de passe requis"}), 400

    user = User.query.filter((User.username == id) | (User.email == id)).first()
    if user and user.check_password(password):
>>>>>>> a923ddb4265fa7fb55e2cf1284655155a0c2f14a
        access_token = create_access_token(identity=user.username)
        return jsonify({"token": access_token}), 200

    return jsonify({"message": "Nom d'utilisateur ou mot de passe incorrect"}), 401


# Endpoint pour récupérer les informations d'un utilisateur
<<<<<<< HEAD
@app.route("/users/<username>", methods=["GET"])
@jwt_required()
=======
@route.route("/users/<username>", methods=["GET"])
@jwt_required(optional=True)
>>>>>>> a923ddb4265fa7fb55e2cf1284655155a0c2f14a
def get_user(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "Utilisateur non trouvé"}), 404

<<<<<<< HEAD
    return jsonify(user.basic_info()), 200


# Endpoint pour supprimer un utilisateur
@app.route("/users/<username>", methods=["DELETE"])
=======
    current_identity = get_jwt_identity()
    if current_identity:
        if current_identity != username:
            return jsonify({"message": "Accès non autorisé"}), 403
        return jsonify(user.to_dict()), 200
    else:
        return jsonify(user.to_dict_min()), 200

# Endpoint pour supprimer un utilisateur
@route.route("/users/<username>", methods=["DELETE"])
>>>>>>> a923ddb4265fa7fb55e2cf1284655155a0c2f14a
@jwt_required()
def delete_user(username):
    try:
        current_user = get_jwt_identity()
        if current_user != username:
            return jsonify({"message": "Accès non autorisé"}), 403

        user = User.query.filter_by(username=username).first()
        if not user:
            return jsonify({"message": "Utilisateur non trouvé"}), 404

        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "Utilisateur supprimé"}), 200
    except Exception as e:
        return jsonify({"message": "Erreur interne du serveur", "error": str(e)}), 500


# Endpoint pour mettre à jour les informations de l'utilisateur
<<<<<<< HEAD
@app.route("/users/<username>", methods=["PUT"])
=======
@route.route("/users/<username>", methods=["PUT"])
>>>>>>> a923ddb4265fa7fb55e2cf1284655155a0c2f14a
@jwt_required()
def update_user(username):
    try:
        current_user = get_jwt_identity()
        if current_user != username:
            return jsonify({"message": "Accès non autorisé"}), 403

        data = request.get_json()

<<<<<<< HEAD
=======
        app.logger.info(f"type data : {type(data)} | data : {data}")

>>>>>>> a923ddb4265fa7fb55e2cf1284655155a0c2f14a
        user = User.query.filter_by(username=username).first()
        if not user:
            return jsonify({"message": "Utilisateur non trouvé"}), 404

<<<<<<< HEAD
        # Mise à jour des informations de l'utilisateur
        user.nom = data.get("nom", user.nom)
        user.prenom = data.get("prenom", user.prenom)
        user.email = data.get("email", user.email)
        user.password = data.get("password", user.password)
        user.pseudo = data.get("pseudo", user.pseudo)

        db.session.commit()
        return jsonify(user.to_dict()), 200
=======
        for key in data.keys():
            if key not in ["lastName", "firstName", "email", "password", "pseudo"]:
                return jsonify({"message": "Mauvais paramètre fourni"}), 401

        # Mise à jour des informations de l'utilisateur
        
        if("lastName" in data.keys()):
            user.last_name = data.get("lastName", user.last_name) 
        if("firstName" in data.keys()):
            user.first_name = data.get("firstName", user.first_name)
        if("email" in data.keys()):
            user.email = data.get("email", user.email)
        if("password" in data.keys()):
            user.set_password(data.get("password", user.password))
        if("pseudo" in data.keys()):
            user.pseudo = data.get("pseudo", user.pseudo)



        db.session.commit()
        return jsonify({"message": "L'utilisation a bien été modifié"}), 200
>>>>>>> a923ddb4265fa7fb55e2cf1284655155a0c2f14a

    except Exception as e:
        return jsonify({"message": "Erreur interne du serveur", "error": str(e)}), 500
