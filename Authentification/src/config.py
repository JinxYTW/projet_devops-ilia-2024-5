import os
from dotenv import load_dotenv
from datetime import timedelta

from Authentification.src import app

load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite:///app.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY", "super-secret")
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=15)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=1)
app.config['JWT_TOKEN_LOCATION'] = ['headers']
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
