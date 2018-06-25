import datetime

from app.ext import db

"""
单项引用
双向引用
商品 ---》 主表      详情表 ---》 字表

一对一关系 
在商品中有详情的对象，在详情表中没有商品的对象 这种叫
"""


# 约束
# 主键约束  唯一约束  非空约束  默认约束
# 外键约束 关联关系

# 常用的数据类型
# 数字相关
# 字符串
# 日期时间
# 大文本  二进制数据

# 1000.00
# 100000

class User(db.Model):
    # __tablename__ = 't_user'
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True, nullable=True)
    weight = db.Column(db.Float(10, 2))
    # # decimal
    money = db.Column(db.Numeric(10, 2))
    create_date = db.Column(db.DateTime, default=datetime.datetime.now())
    # # 不要在text字段上面加索引
    msg = db.Column(db.Text())


#    外键

# 1>在主表建立外键连接的关系
# 2>在子表建立外键
class Cate(db.Model):
    cid = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(64), index=True, unique=True, nullable=True)
    # 建立关联关系的对象 懒加载
    """
    参数一 argument 关联的对象的类名
    参数二 lazy
            可选项：
            1·select 默认值 一条sql一条把所有相关的数据全部查出来
            2·dynamic 只查询主表的数据， 生成查询子表的sql 当我们需要使用字表的数据数据的时候再去查询
            3·immediate 等主表数据查询完成之后再去查询自标的数据
           
    back_populates 方向引用（当两个对象需要双向引用的时候使用） 值对应双向引用对象的字段 
    order_by=False  指定查询字表的排序字段
    uselist=None
    
    back-ref    backref='cate '    例如可以使用 shop.cate
    
    """
    shops = db.relationship('Shop', back_populates='cate', lazy='dynamic', uselist=True)


class Shop(db.Model):
    sid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True, nullable=True)
    # 类名小写.关联字段
    cid = db.Column(db.Integer, db.ForeignKey(Cate.cid))
    cate = db.relationship('Cate', back_populates='shops')
    # 多对多肯定会有第三张表


# 角色 === 权限     增删该查的权限
# 管理员角色     增删改查的权限
# 普通用户      增查的权限
"""
参数  表的名称
"""
relation = db.Table('role_permission_relation',
                    db.Column('id', db.Integer, primary_key=True),
                    db.Column('per_id', db.Integer, db.ForeignKey('permission.per_id')),
                    db.Column('role_id', db.Integer, db.ForeignKey('role.role_id'))
                    )


# secondary 用于多对多， 指向第三张表
class Role(db.Model):
    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(64), nullable=False, index=True, unique=True)
    desc = db.Column(db.Text)
    permissions = db.relationship('Permission', secondary=relation)

    def __init__(self, role_name, desc):
        self.role_name = role_name
        self.desc = desc


# 权限
class Permission(db.Model):
    per_id = db.Column(db.Integer, primary_key=True)
    per_name = db.Column(db.String(64), nullable=False, index=True, unique=True)
    desc = db.Column(db.Text)

    def __init__(self, per_name, desc):
        self.per_name = per_name
        self.desc = desc
