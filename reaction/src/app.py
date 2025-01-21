from flask import Flask
from routes import blueprints
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Fonction pour charger dynamiquement les routes depuis le dossier `routes`
def load_routes():
    for bp in blueprints:
        app.register_blueprint(bp)

def create_app():

    return app

# Charger les routes
load_routes()

@app.route('/')
def index():
    return 'Bienvenue sur la page d\'accueil !'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
