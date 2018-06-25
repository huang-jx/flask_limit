from flask import Blueprint

homework = Blueprint('homework', __name__, template_folder='templates')

import app.homework_zsgc.views
