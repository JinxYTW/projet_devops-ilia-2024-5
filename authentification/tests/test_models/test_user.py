import pytest

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from models.user import User
from config import db

def test_user_creation():
    user = User(
        last_name="Doe",
        first_name="John",
        email="john@example.com",
        username="johndoe",
        pseudo="jd"
    )
    user.set_password("password123")
    assert user.last_name == "Doe"
    assert user.first_name == "John"
    assert user.email == "john@example.com"
    assert user.username == "johndoe"
    assert user.pseudo == "jd"
    assert user.check_password("password123")

def test_user_to_dict():
    user = User(
        last_name="Doe",
        first_name="John",
        email="john@example.com",
        username="johndoe",
        pseudo="jd"
    )
    user.set_password("password123")
    user_dict = user.to_dict()
    assert user_dict["lastName"] == "Doe"
    assert user_dict["firstName"] == "John"
    assert user_dict["email"] == "john@example.com"
    assert user_dict["username"] == "johndoe"
    assert user_dict["pseudo"] == "jd"
    assert "password" not in user_dict
