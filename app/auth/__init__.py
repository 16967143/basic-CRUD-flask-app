from flask import Blueprint

admin = Blueprint('auth', __name__)

from . import views
