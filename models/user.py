from models.base_model import BaseModel
from models import db
from sqlalchemy import Column, VARCHAR, TEXT, INTEGER


class User(BaseModel):
    __tablename__ = 'user'
    openid = Column('OpenID', VARCHAR(100), primary_key=True, comment='用户身份编号')
    nickName = Column('NickName', VARCHAR(75), comment='昵称')
    avatar_url = Column('Avatar Url', TEXT, comment='头像链接')
    country = Column('Country', VARCHAR(75), comment='国家')
    province = Column('Province', VARCHAR(75), comment='省份')
    city = Column('City', VARCHAR(75), comment='城市')
    gender = Column('Gender', INTEGER, comment='性别')
    language = Column('Language', VARCHAR(20))

    @staticmethod
    def insert(id, data):
        with db.auto_commit():
            user = User()
            user.openid = id
            user.avatar_url = data['avatarUrl']
            user.city = data['city']
            user.country = data['country']
            user.province = data['province']
            user.nickName = data['nickName']
            user.gender = data['gender']
            user.language = data['language']
            db.session.add(user)

    def update(self, data):
        with db.auto_commit():
            self.avatar_url = data['avatarUrl']
            self.city = data['city']
            self.country = data['country']
            self.province = data['province']
            self.nickName = data['nickName']
            self.gender = data['gender']
            self.language = data['language']
            self.update_time = self.generate_datetime



