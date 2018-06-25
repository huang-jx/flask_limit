from flask import Flask

from app.ext import init_ext
from app.homework_zsgc import homework
from app.shop import shop
from app.user import users

app = Flask(__name__)
app.debug = True


def create_app():
    init_ext(app=app)
    register_blue()
    return app


def register_blue():
    app.register_blueprint(users, url_prefix='/user')
    app.register_blueprint(shop, url_prefix='/shop')
    app.register_blueprint(homework, url_prefix='/work')
