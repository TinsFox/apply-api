from wtforms import StringField, PasswordField, Form
from wtforms.validators import DataRequired, Length, EqualTo, Regexp
# -------------------------
from models.admin import Admin
from libs.exceptions import RegisterFailed, NotFound


class AdminRegisterForm(Form):
    """ 管理员注册表单 """
    account = StringField(validators=[DataRequired(), Regexp('^[a-zA-Z0-9_]{4,12}$')])
    password = StringField(validators=[DataRequired(), Length(6, 18)])

    def validate_account(self, field):
        if Admin.query.filter_by(account=field.data).first():
            raise RegisterFailed('该账户已被注册')


class AdminLoginForm(Form):
    """ 管理员登录 """
    account = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])

    def validate_account(self, field):
        if not Admin.query.filter_by(account=field.data).first():
            raise NotFound('该管理员账户不存在')


class AdminChangePwdForm(Form):
    """ 修改密码 """
    account = StringField(validators=[DataRequired(), Length(4, 10)])
    old_pwd = PasswordField(validators=[DataRequired(), Length(6, 18)])
    new_pwd = PasswordField(validators=[DataRequired(), Length(6, 18),
                                        EqualTo('confirm_pwd')])
    confirm_pwd = PasswordField(validators=[DataRequired(), Length(6, 18)])

    def validate_account(self, field):
        if not Admin.query.filter_by(account=field.data).first():
            raise NotFound('该管理员账户不存在')
