from sqlalchemy import Column, VARCHAR, INTEGER
from werkzeug.security import check_password_hash, generate_password_hash
# --------------------------------------------------------------------------
from libs.exceptions import AuthFailed
from models.base_model import BaseModel
from models.community import Society
from models import db


class Admin(BaseModel):
    """ 定义管理员模型 """
    __tablename__ = 'admin'
    id = Column('ID', VARCHAR(64), primary_key=True, comment='管理员身份编号')
    account = Column('Account', VARCHAR(25), unique=True, nullable=False, comment='账户')
    password = Column('Password', VARCHAR(100), comment='密码')
    auth = Column('Scope', INTEGER, nullable=False, comment='权限')

    @staticmethod
    def register(id, account, password):
        """ 社团管理员注册 """
        with db.auto_commit():
            admin = Admin()
            admin.id = id
            admin.account = account
            admin.password = generate_password_hash(password)
            admin.auth = 1
            db.session.add(admin)

    @staticmethod
    def login_verify(account, pwd):
        """ 管理员登录验证 """
        admin = Admin.query.filter_by(account=account).first_or_404()
        if admin.auth == 1:
            society = Society.query.get_or_404(admin.id, description=u"该管理员账号对应的社团不存在")
            name = society.name
        else:
            name = '超级管理员'
        if not check_password_hash(admin.password, pwd):
            raise AuthFailed('密码错误')
        return {'society_id': admin.id, 'scope': admin.auth, 'name': name}

    @staticmethod
    def change_password(account, old_pwd, new_pwd):
        """ 修改密码 """
        admin = Admin.query.filter_by(account=account).first_or_404()
        if not check_password_hash(admin.password, old_pwd):
            raise AuthFailed(msg=u'旧密码错误')
        admin.password = generate_password_hash(new_pwd)
        admin.update_time = admin.generate_datetime
        db.session.commit()





