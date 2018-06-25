from flask import Blueprint

shop = Blueprint('shop', __name__)

import app.shop.views
