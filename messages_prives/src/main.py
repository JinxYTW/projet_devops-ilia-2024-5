from flask import Flask
from routes import blueprints
from flask_cors import CORS # type: ignore

app = Flask(__name__)
CORS(app)

# Fonction pour enregistrer les routes depuis le dossier ./routes
def load_routes():
    for bp in blueprints:
        app.register_blueprint(bp)
        
app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)
