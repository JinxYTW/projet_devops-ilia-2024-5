from flask import Flask
import os
import importlib

app = Flask(__name__)

# Fonction pour charger dynamiquement les routes depuis le dossier `routes`
def load_routes():
    routes_folder = 'routes'
    for filename in os.listdir(routes_folder):
        if filename.endswith('.py') and filename != '__init__.py':
            # Récupérer le nom du fichier sans l'extension `.py`
            route_name = filename[:-3]
            # Importer le module correspondant à la route
            module = importlib.import_module(f'routes.{route_name}')
            # Enregistrer les routes de ce module dans l'application Flask
            module.init_app(app)

# Charger les routes
load_routes()

@app.route('/')
def index():
    return 'Bienvenue sur la page d\'accueil !'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
