# -*- coding: utf-8 -*-
from extension import db

class Guest(db.Model):
    __tablename__ = 'guest'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    card_number = db.Column(db.String(255), nullable=False)
    guest_name = db.Column(db.String(255), nullable=False)
    guest_type = db.Column(db.String(255), nullable=False)
    guest_time = db.Column(db.String(255), nullable=False)
    guest_login_type = db.Column(db.Float, nullable=False)

    @staticmethod
    def init_db():
        rets = [
            (1, '114514', '王爷', 'vip', '2011-01-01 00:00:00', 1),
            (2, '1919810', '小人', 'temp', '2021-01-01 00:00:00', 0)
        ]
        for ret in rets:
            guest = Guest()
            guest.id = ret[0]
            guest.card_number = ret[1]
            guest.guest_name = ret[2]
            guest.guest_type = ret[3]
            guest.guest_time = ret[4]
            guest.guest_login_type = ret[5]
            db.session.add(guest)
        db.session.commit()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    card_number = db.Column(db.String(255), nullable=False)
    guest_name = db.Column(db.String(255), nullable=False)
    guest_type = db.Column(db.String(255), nullable=False)

    @staticmethod
    def init_db():
        users = [
            (1, '114514', '王爷', 'vip'),
        ]
        for user in users:
            u = User()
            u.id = user[0]
            u.card_number = user[1]
            u.guest_name = user[2]
            u.guest_type = user[3]
            db.session.add(u)
        db.session.commit()

# 请阅读下面的代码，解释`id = db.Column(db.Integer, primary_key=True, autoincrement=True)`的作用
# 修改下面的代码，alarm_photo 是一个 BLOB 类型，用于存储图片数据
# 请阅读下面的代码，在 alarms 中，请生成一行表格作为例子

class Alarm(db.Model):
    __tablename__ = 'alarm'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    alarm_time = db.Column(db.String(255), nullable=False)
    alarm_photo = db.Column(db.BLOB, nullable=False) # 修改为BLOB类型

    @staticmethod
    def init_db():
        alarms = [
            (1, '2021-01-01 00:00:00', '5555'),
        ]
        for alarm in alarms:
            a = Alarm()
            a.id = alarm[0]
            a.alarm_time = alarm[1]
            a.alarm_photo = alarm[2]
            db.session.add(a)
        db.session.commit()

