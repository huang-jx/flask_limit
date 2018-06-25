from flask import request, render_template
from app.ext import db
from app.homework_zsgc import homework
from app.user.models import Shop


@homework.route('/list/')
def list():
    # get 请求
    # request.args
    # post请求还有put请求
    # request.form
    page = request.values.get('page', default=1, type=int)
    #
    size = request.values.get('size', default=10, type=int)
    paginage = db.session.query(Shop.sid, Shop.name).paginage(page=page, per_page=size, error_out=False)
    shop = paginage.items
    return render_template('', shop)


