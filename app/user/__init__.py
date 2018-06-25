from flask import Blueprint

users = Blueprint('user', __name__, template_folder='templates')
import app.user.views
