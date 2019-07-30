# -*-coding:utf8 -*-
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Regexp
# -------------------------
from libs.forms import BaseForm
from libs.exceptions import RegisterFailed
from models.admin import Admin


class AdminRegisterForm(BaseForm):
    """ 管理员注册表单 """
    account = StringField(validators=[DataRequired(), Regexp('^[a-zA-Z0-9_]{4,12}$')])
    password = StringField(validators=[DataRequired(), Length(6, 18)])

    def validate_account(self, field):
        if Admin.query.filter_by(account=field.data).first():
            raise RegisterFailed(u'该账号已被注册')


class AdminLoginForm(AdminRegisterForm):
    """ 管理员登录 """
    def validate_account(self, field):
        Admin.query.filter_by(account=field.data).first_or_404(description=u'该账号不存在')


class AdminChangePwdForm(BaseForm):
    """ 修改密码 """
    account = StringField(validators=[DataRequired(), Length(4, 12)])
    old_pwd = PasswordField(validators=[DataRequired(), Length(6, 18)])
    new_pwd = PasswordField(validators=[DataRequired(), Length(6, 18),
                                        EqualTo('confirm_pwd')])
    confirm_pwd = PasswordField(validators=[DataRequired(), Length(6, 18)])

    def validate_account(self, field):
        Admin.query.filter_by(account=field.data).first_or_404()
