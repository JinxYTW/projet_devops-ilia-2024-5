from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# Base de données
users_db = {}
tokens_db = {}


# Token
def generate_token():
    return str(uuid.uuid4())


# Endpoint pour l'inscription
@app.route('/auth/sign_in', methods=['POST'])
def sign_in():
    data = request.get_json()
    nom = data.get('nom')
    prenom = data.get('prenom')
    email = data.get('email')
    password = data.get('password')
    username = data.get('username')
    pseudo = data.get('pseudo')

    if username in users_db:
        return jsonify({'message': 'Nom d\'utilisateur déjà pris'}), 400

    user = {
        'nom': nom,
        'prenom': prenom,
        'email': email,
        'password': password,
        'username': username,
        'pseudo': pseudo
    }

    users_db[username] = user
    token = generate_token()
    tokens_db[token] = username
    return jsonify({'token': token}), 200


# Endpoint pour la connexion
@app.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    username_or_email = data.get('username_or_email')
    password = data.get('password')

    for user in users_db.values():
        if ((user['email'] == username_or_email or user['username'] == username_or_email) and
                user['password'] == password):
            token = generate_token()
            tokens_db[token] = user['username']
            return jsonify({'token': token}), 200

    return jsonify({'message': 'Nom d\'utilisateur ou mot de passe incorrect'}), 400


if __name__ == '__main__':
    app.run(debug=True)
