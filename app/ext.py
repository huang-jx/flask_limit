from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

migrate = Migrate()


def init_ext(app: Flask):
    # 初始化数据库相关操作
    init_db_config(app)


def init_db_config(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:888888@127.0.0.1:3306/flask_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)
    migrate.init_app(app, db)
