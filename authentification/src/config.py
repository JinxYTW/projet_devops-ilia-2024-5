import os
from dotenv import load_dotenv
from datetime import timedelta

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)

<<<<<<< HEAD
db = SQLAlchemy(app)
jwt = JWTManager(app)

load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite:///app.db")
=======
load_dotenv()

db_ip = os.getenv("DATABASE_IP", "192.168.1.3")
db_user = os.getenv("DATABASE_URL", "root")
db_password = os.getenv("DATABASE_PASSWORD", "root")
db_port = os.getenv("DATABASE_PORT", "3306")
db_name = os.getenv("DATABASE_NAME", "polytex")

app.config['SQLALCHEMY_DATABASE_URI'] =f"mysql+pymysql://{db_user}:{db_password}@{db_ip}:{db_port}/{db_name}"
>>>>>>> a923ddb4265fa7fb55e2cf1284655155a0c2f14a
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY", "super-secret")
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=15)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=1)
app.config['JWT_TOKEN_LOCATION'] = ['headers']
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
<<<<<<< HEAD
=======

db = SQLAlchemy(app)

jwt = JWTManager(app)
>>>>>>> a923ddb4265fa7fb55e2cf1284655155a0c2f14a
