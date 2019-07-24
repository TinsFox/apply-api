from sqlalchemy import Column, VARCHAR, INTEGER
from werkzeug.security import check_password_hash, generate_password_hash
# --------------------------------------------------------------------------
from libs.exceptions.failed import AuthFailed
from libs.exceptions.errors import NotFound
from libs.exceptions.base import UpdateSuccess
from models import db


class Admin(db.Model):
    """ 定义管理员模型 """
    __tablename__ = 'formsp'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    account = Column('账户名', VARCHAR(25), unique=True, nullable=False)
    password = Column('密码', VARCHAR(100))
    society = Column('社团', VARCHAR(50), nullable=False, unique=True)
    auth = Column('权限', INTEGER, nullable=False)

    @staticmethod
    def change_password(account, new_pwd):
        """ 修改密码 """
        admin = Admin.query.filter_by(account=account).first()
        if not admin:
            raise NotFound('该管理员账户不存在')
        admin.password = generate_password_hash(new_pwd)
        return UpdateSuccess()

    @staticmethod
    def register(forms):
        """ 管理员注册(社团) """
        with db.auto_commit():
            society = forms.get('society')
            admin = Admin()
            admin.society = society
            admin.account = forms.get('account')
            admin.password = generate_password_hash(forms.get('password'))
            admin.auth = 1 if society != '超级管理员' else 2
            db.session.add(admin)

    @staticmethod
    def login_verify(account, pwd):
        """ 管理员登录验证 """
        admin = Admin.query.filter_by(account=account).first()
        if not check_password_hash(admin.password, pwd):
            raise AuthFailed()
        return {'society': admin.society, 'scope': admin.auth}
