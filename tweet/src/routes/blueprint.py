from flask import Blueprint

bp = Blueprint('routes', __name__)

from src.routes.meta import meta