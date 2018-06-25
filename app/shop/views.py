from flask import logging, request

from app.ext import db
from app.shop import shop
from app.user.models import Cate, Shop


@shop.route('/add_cate/')
def add_cate():
    cates = []
    for i in range(1, 101):
        cates.append(Cate(cname='分类' + str(i)))
    db.session.bulk_save_objects(cates)
    db.session.commit()
    return '添加成功'


@shop.route('/add_shop/')
def add_shop():
    shops = []
    for i in range(1, 101):
        shops.append(Shop(name='商品' + str(i), cid=str(i)))
    db.session.bulk_save_objects(shops)
    db.session.commit()
    return '添加成功'


# 通过一的一方查多的一方
"""
优点 一次查询就把数据加载出来
缺点 当数据足够大的时候会拖慢服务器运行速率
"""


@shop.route('/find/')
def find():
    cates = Cate.query.all()

    for cate in cates:
        print(type(cate.shops))
        db.session.query(Shop.name).filter(cid=cate.cid).all()
        logging.debug(shop.name)

    # 通过多的一方查多的一方
    # shop = db.session.query(Shop.sid, Shop.name, Shop.cid).filter(Shop.sid == 1).first()
    # Cate.query.get(shop.cid)

    return '通过一的一方查询多的一方'


# /shop?sid=1
@shop.route('/find_id/', methods=['get', 'method', 'put'])
def find_id():
    sid = request.values.get('sid', default=0, type=int)
    shop = Shop.query.get(sid)
    print(shop.name)
    print(shop.cate.cid)

    return '通过一的方查多的一方 shop->name=%s cate->cid=%s' % ((shop.name), (shop.cate.cid))
