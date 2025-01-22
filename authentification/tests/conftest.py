import pytest
from flask import Flask, json
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import sys
from datetime import timedelta

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/.env1'))

load_dotenv(env_path)

from models.user import User

token = ""

@pytest.fixture()
def app() -> Flask:
    app = Flask(__name__)

    db_ip = os.getenv("DATABASE_IP", "192.168.1.3")
    db_user = os.getenv("DATABASE_URL", "root")
    db_password = os.getenv("DATABASE_PASSWORD", "root")
    db_port = os.getenv("DATABASE_PORT", "3306")
    db_name = os.getenv("DATABASE_NAME", "polytex")

    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{db_user}:{db_password}@{db_ip}:{db_port}/{db_name}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY", "super-secret")
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=15)
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=1)
    app.config['JWT_TOKEN_LOCATION'] = ['headers']
    app.config['JWT_COOKIE_CSRF_PROTECT'] = False

    app.config['TESTING'] = True

    return app

@pytest.fixture()
def db(app: Flask) -> SQLAlchemy:
    db = SQLAlchemy(app)
    with app.app_context():
        db.create_all()
    yield db
    db.session.remove()
    db.drop_all()

# Fixture de l'application Flask
@pytest.fixture()
def client(app: Flask, db: SQLAlchemy):
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Création de la base de données en mémoire
        yield client
        db.session.remove()
        db.drop_all()

# Fixture d'un utilisateur pour les tests
@pytest.fixture
def test_user(db: SQLAlchemy):
    user = User(
        last_name="Doe",
        first_name="John",
        email="john@example.com",
        username="johndoe",
        pseudo="jd"
    )
    user.set_password("password123")
    db.session.add(user)
    db.session.commit()
    return user

def test_login_success(client, test_user):
    response = client.post('/auth/login', json={
        "username": "johndoe",
        "password": "password123"
    })
    assert response.status_code == 200
    data = json.loads(response.data)
    token = data["token"]
    assert "token" in data  # Vérifie que le token est dans la réponse