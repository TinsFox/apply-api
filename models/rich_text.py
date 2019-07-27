from sqlalchemy import Column, VARCHAR, PickleType, DATETIME

from models import db, get_time


class RichText(db.Model):
    __tablename__ = 'rich_text'
    id = Column('ID', VARCHAR(64), primary_key=True, comment='编号')
    body = Column('Rich Text', PickleType, comment='简介')
    create_time = Column('Create Time', DATETIME, comment='创建时间')
    update_time = Column('Update Time', DATETIME, comment='更新时间')

    @staticmethod
    def insert(s_id, body):
        time = get_time()
        with db.auto_commit():
            rich_text = RichText()
            rich_text.society_id = s_id
            rich_text.body = body
            rich_text.create_time = time
            rich_text.update_time = time

    @staticmethod
    def update(s_id, body):
        with db.auto_commit():
            rich_text = RichText.query.filter_by(id=s_id).first()
            rich_text.body = body
            rich_text.update_time = get_time()

    @staticmethod
    def delete(o):
        """ 删除报名信息 """
        with db.auto_commit():
            if isinstance(o, list):
                for single in o:
                    db.session.delete(single)
            else:
                db.session.delete(o)

    def keys(self):
        return ['body', 'update_time']

    def __getitem__(self, item):
        return getattr(self, item)







