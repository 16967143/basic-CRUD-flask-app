from flask import Blueprint

admin = Blueprint('home', __name__)

from . import views
