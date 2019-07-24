from flask import request, jsonify, g
# ----------------------------------------------
from api import SmallBlueprint
from libs.token import generate_token
from libs.exceptions.errors import FormError, ServerError
from libs.exceptions.base import RegisterSuccess
from libs.forms.admin import AdminRegisterForm, AdminLoginForm
from models.admin import Admin


api = SmallBlueprint('admin', url_prefix='/admin')


@api.route('/register', methods=['POST'])
def admin_register():
    """ 管理员注册 """
    status = AdminRegisterForm(request.form).validate()
    if not status:
        raise FormError('提交表单格式错误')
    try:
        Admin.register(request.form)
    except Exception:
        raise ServerError()
    return RegisterSuccess()


@api.route('/login', methods=['POST'])
def admin_login():
    """ 管理员登录 """
    status = AdminLoginForm(request.form).validate()
    if not status:
        raise FormError('提交表单格式错误')
    g.info = Admin.login_verify(request.form['account'], request.form['password'])
    token = {
        'acess_token': generate_token(),
        'message': '登录成功',
        'errcode': 0
    }
    return jsonify(token)

