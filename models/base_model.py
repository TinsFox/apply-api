import time
from sqlalchemy import Column, DATETIME
from models import db


class BaseModel(db.Model):
    __abstract__ = True
    create_time = Column('Create Time', DATETIME, comment='创建时间')
    update_time = Column('Update Time', DATETIME, comment='更新时间')

    def __init__(self):
        self.create_time = self.generate_datetime
        self.update_time = self.generate_datetime

    @property
    def generate_datetime(self):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    def __getitem__(self, item):
        return getattr(self, item)

    def delete(self):
        """ 删除数据 """
        with db.auto_commit():
            if isinstance(self, list):
                for data in self:
                    db.session.delete(data)
            else:
                db.session.delete(self)









