from flask import Flask
from src.routes.blueprint import bp

def create_app():
    app = Flask(__name__)

    with app.app_context():
        app.register_blueprint(bp)

    return app