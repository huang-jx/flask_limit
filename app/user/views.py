from flask import render_template, request, redirect, url_for

from app.ext import db
from app.user import users
from .models import User, Shop, Cate, Role, Permission


@users.route('/show/')
def show():
    # 过滤列
    query = db.session.query(User.name).all()
    users = User.query.all()
    user = User.query.filter_by(name='test1').first()
    return '查询'


@users.route('/save/')
def save_all():
    objects = []
    for i in range(1, 101):
        objects.append(User(name='name' + str(i), weight='10' + str(i), money='3485' + str(i), msg='message' + str(i)))
    db.session.bulk_save_objects(objects)
    db.session.commit()
    return '批量保存'


@users.route('/limit/')
# @users.route('/limit/<int:page>/<int:size>/')
# def query_limit(page, size):
def query_limit():
    page = request.values.get('page', default=1, type=int)
    size = request.values.get('size', default=10, type=int)
    paginate = User.query.order_by(User.uid).paginate(page=page, per_page=size, error_out=False)
    users = paginate.items
    print(users)
    print(paginate.total)
    print(paginate.pages)
    print(paginate.page)
    print(paginate.has_prev)
    print(paginate.has_next)
    # print(user.query_limit)
    return render_template('user/users.html', users=users, paginate=paginate)


@users.route('/insert/', methods=['get', 'post'])
def add():
    if request.method == 'GET':
        return render_template('zsgc/add.html')
    elif request.method == 'POST':
        name = request.values.get('name')
        weight = request.values.get('weight')
        money = request.values.get('money')
        message = request.values.get('msg')
        user = User(name=name, weight=float(weight), money=money, msg=message)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('user.query_limit'))


@users.route('/update/', methods=['get', 'post'])
def update():
    if request.method == 'GET':
        uid = request.values.get('uid', type=int)
        user = User.query.get(uid)
        return render_template('zsgc/update.html', user=user)
    elif request.method == 'POST':
        uid = request.values.get('uid', type=int)
        name = request.values.get('name', type=str)
        weight = request.values.get('weight', type=float)
        money = request.values.get('money')
        create_date = request.values.get('create_date')
        msg = request.values.get('msg')
        User.query.filter(User.uid == uid).update(
            {User.name: name, User.weight: weight, User.money: money, User.create_date: create_date, User.msg: msg})
        db.session.commit()
        return redirect('/user/limit/')


# 分类菜单
@users.route('/1/')
def test():
    # 通过一的一方查询多的一方
    cates = Cate.query.all()
    for cate in cates:
        # shops = Shop.query.filter(Shop.cid == cate.cid).all()
        print(cate.cname)
        print(cate.shops[0].name)
    # 通过多的一方查询一的一方
    shop = Shop.query.first()
    print(shop.cate.cname)
    Cate.query.filter(Cate.cid == shop.cid)


# ==========多对多=============
@users.route('/add/role/')
def add_role():
    role = Role('admin', '超级管理员')
    db.session.add(role)
    db.session.add_all([Permission('insert', '添加操作'),
                        Permission('delete', '删除操作'),
                        Permission('update', '更新操作'),
                        Permission('select', '查看操作')])
    db.session.commit()
    return '添加权限角色'


@users.route('/add/role/per/')
def add_role_per():
    admin = Role.query.get(1)
    admin.permissions = Permission.query.all()
    db.session.commit()
    return '添加权限角色'


@users.route('/find/role/')
def find_role():
    role = Role.query.get(1)
    for per in role.permissions:
        print(per.per_name)
    return '通过角色查询对象'


@users.route('/del/msg/')
def del_msg():
    if has_per():
        return '删除成功'
    else:
        return '没有相关数据，请与管理员联系'


def has_per():
    role = Role.query.get(1)
    for per in role.permissions:
        if per.per_name == 'delete':
            return True
    return False


@users.route('/del/per/')
def del_per(per):
    return
