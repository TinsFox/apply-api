# -*- coding: utf8 -*-
from flask import request, g, jsonify
from models.admin import Admin
from api import SmallBlueprint
from libs.token import generate_token
from libs.forms.admin import AdminRegisterForm, AdminLoginForm, AdminChangePwdForm
from libs.exceptions import RegisterSuccess, UpdateSuccess, RegisterFailed


api = SmallBlueprint('client', url_prefix='/open')


@api.route('/register/<string:id>', methods=['POST'])
def register(id):
    """
    # 社团管理员注册
    # status: OVER
    :param id: 管理员身份编号
    """
    if Admin.query.get(id):
        raise RegisterFailed(u'该社团已注册管理员')
    form = AdminRegisterForm(data=request.json).validate_or_error()
    Admin.register(id, form.account.data, form.password.data)
    return RegisterSuccess()


@api.route('/login', methods=['POST'])
def login():
    """
    # 社团管理员登录
    # status: OVER
    """
    form = AdminLoginForm(data=request.json).validate_or_error()
    g.info = Admin.login_verify(form.account.data, form.password.data)
    token = {
        'acess_token': generate_token(),
        'scope': g.info['scope'],
        'message': '登录成功',
        'errcode': 0
    }
    return jsonify(token)


@api.route('/change', methods=['PUT'])
def change_password():
    """ 修改密码 """
    form = AdminChangePwdForm(data=request.json).validate_or_error()
    Admin.change_password(form.account.data, form.old_pwd.data, form.new_pwd.data)
    return UpdateSuccess()
