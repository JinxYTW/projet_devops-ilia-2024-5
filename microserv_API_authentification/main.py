from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
import os
from dotenv import load_dotenv



load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite:///app.db")  # URL à modifier 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY", "super-secret")
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=15) 
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=1)  
app.config['JWT_TOKEN_LOCATION'] = ['headers'] 
app.config['JWT_COOKIE_CSRF_PROTECT'] = False 

db = SQLAlchemy(app)
jwt = JWTManager(app)


# Callback pour rafraîchir automatiquement les tokens à chaque requête
@jwt_required()
def refresh_token_if_needed():
    current_user = get_jwt_identity()
    # Réémettre un token d'accès
    new_token = create_access_token(identity=current_user)
    return jsonify({"new_token": new_token}), 200

class User(db.Model):
    __tablename__ = 'users'

    nom = db.Column(db.String(50), nullable=False)
    prenom = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    pseudo = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            "nom": self.nom,
            "prenom": self.prenom,
            "email": self.email,
            "username": self.username,
            "pseudo": self.pseudo
        }
    
    def basic_info(self):
        return {
            "username":self.username,
            "pseudo":self.pseudo
        }
    
#--------------SIGN IN--------------------


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
        return jsonify({"message": "Tous les champs sont obligatoires"}), 401
    if User.query.filter(User.username == username).first():
        return jsonify({"message": "Nom d'utilisateur déjà pris"}), 401
    if User.query.filter(User.email == email).first():
        return jsonify({"message": "Email déjà pris"}), 401

    new_user = User(nom=nom, prenom=prenom, email=email, password=password, username=username, pseudo=pseudo)
    db.session.add(new_user)
    db.session.commit()

    access_token = create_access_token(identity=username)
    return jsonify({"token": access_token}), 200


#--------------LOGIN--------------------


@app.route("/auth/login", methods=["POST"])
def login():
    data = request.get_json()
    username_or_email = data.get("username_or_email")
    password = data.get("password")

    if not username_or_email or not password:
        return jsonify({"message": "Nom d'utilisateur ou mot de passe requis"}), 401

    user = User.query.filter((User.username == username_or_email) | (User.email == username_or_email)).first()
    if user and user.password == password:
        access_token = create_access_token(identity=user.username)
        return jsonify({"token": access_token}), 200

    return jsonify({"message": "Nom d'utilisateur ou mot de passe incorrect"}), 401


@app.route("/users/<userName>", methods=["GET"])
def get_user(userName):
    user = User.query.filter(User.username == userName).first()
    if not user:
        return jsonify({"message": "Utilisateur non trouvé"}), 404
    return jsonify(user.to_dict()), 200


@app.route("/users/<userName>", methods=["Delete"])
def delete_user(userName):
    user = User.query.filter(User.username == userName).first()
    if not user:
        return jsonify({"message": "Utilisateur non trouvé"}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "Utilisateur supprimé"}), 200


@app.route("/users/<userName>", methods=["PUT"])
def update_user(userName):
    user = User.query.filter(User.username == userName).first()
    if not user:
        return jsonify({"message": "Utilisateur non trouvé"}), 404
    data = request.get_json()
    user.nom = data.get("nom", user.nom)
    user.prenom = data.get("prenom", user.prenom)
    user.email = data.get("email", user.email)
    user.password = data.get("password", user.password)
    user.username = data.get("username", user.username)
    user.pseudo = data.get("pseudo", user.pseudo)
    db.session.commit()
    return jsonify(user.to_dict()), 200

#--------------GET INFO--------------------
@app.route("/users/<string:username>", methods=["GET"])
def get_user(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "Utilisateur non trouvé"}), 404

    return jsonify(user.basic_info()), 200

#--------------GET PRIVATE INFO--------------------

@app.route("/users/information/<string:username>", methods=["GET"])
@jwt_required() 
def get_user_info(username):
    
    current_user = get_jwt_identity()
    if current_user != username:
        return jsonify({"message": "Accès non autorisé"}), 403

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "Utilisateur non trouvé"}), 404

    return jsonify(user.to_dict()), 200


#--------------DELETE-------------------- 

@app.route("/users/<string:username>", methods=["DELETE"])
@jwt_required() 
def delete_user(username):

    current_user = get_jwt_identity()
    if current_user != username:
        return jsonify({"message": "Accès non autorisé"}), 403

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "Utilisateur non trouvé"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "Utilisateur supprimé"}), 200

#--------------UPDATE--------------------

@app.route("/users/<string:username>", methods=["PUT"])
@jwt_required() 
def update_user(username):
    current_user = get_jwt_identity()
    if current_user != username:
        return jsonify({"message": "Accès non autorisé"}), 403
    
    data = request.get_json()

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "Utilisateur non trouvé"}), 404

    # Mise à jour des informations de l'utilisateur
    user.nom = data.get("nom", user.nom)
    user.prenom = data.get("prenom", user.prenom)
    user.email = data.get("email", user.email)
    user.password = data.get("password", user.password)
    user.pseudo = data.get("pseudo", user.pseudo)

    db.session.commit()
    return jsonify(user.to_dict()), 200

if __name__ == "__main__":
    app.run(debug=True)
