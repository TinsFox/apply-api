from sqlalchemy import Column, VARCHAR, INTEGER, DATETIME
from werkzeug.security import check_password_hash, generate_password_hash
# --------------------------------------------------------------------------
from libs.exceptions import AuthFailed, NotFound
from models import db, create_id, get_time


class Admin(db.Model):
    """ 定义管理员模型 """
    __tablename__ = 'admin'
    society_id = Column('Society ID', VARCHAR(64), primary_key=True, comment='社团编号')
    account = Column('Account', VARCHAR(25), unique=True, nullable=False, comment='账户')
    password = Column('Password', VARCHAR(100), comment='密码')
    auth = Column('Scope', INTEGER, nullable=False, comment='权限')
    create_time = Column('Create Time', DATETIME, comment='创建时间')
    update_time = Column('Update Time', DATETIME, comment='更新时间')

    @staticmethod
    def register(s_id, data):
        """ 管理员注册(社团) """
        time = get_time()
        with db.auto_commit():
            admin = Admin()
            admin.society_id = s_id
            admin.create_time = time
            admin.update_time = time
            admin.account = data.get('account')
            admin.password = generate_password_hash(data.get('password'))
            admin.auth = 1 if s_id != create_id('超级管理员') else 2
            db.session.add(admin)

    @staticmethod
    def login_verify(account, pwd):
        """ 管理员登录验证 """
        admin = Admin.query.filter_by(account=account).first()
        if not check_password_hash(admin.password, pwd):
            raise AuthFailed('密码错误')
        return {'society_id': admin.society_id, 'scope': admin.auth}

    @staticmethod
    def change_password(account, old_pwd, new_pwd):
        """ 修改密码 """
        with db.auto_commit():
            admin = Admin.query.filter_by(account=account).first()
            if not admin:
                raise NotFound('修改失败, 该账号不存在')
            if not check_password_hash(admin.password, old_pwd):
                raise AuthFailed('旧密码错误')
            admin.password = generate_password_hash(new_pwd)
            admin.update_time = get_time()





