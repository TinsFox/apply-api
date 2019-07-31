# -*- coding: utf8 -*-
from flask import Flask
from werkzeug.security import generate_password_hash
from models.admin import Admin
from init import create_app
from models import db, generate_id


app = create_app(Flask(__name__))


with app.app_context():
    with db.auto_commit():
        # 创建一个超级管理员
        user = Admin()
        user.account = 'super'
        user.password = generate_password_hash('123456')
        user.id = generate_id(u'超级管理员')
        user.auth = 2
        db.session.add(user)
