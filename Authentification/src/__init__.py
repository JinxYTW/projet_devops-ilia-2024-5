from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)

db = SQLAlchemy(app)
jwt = JWTManager(app)