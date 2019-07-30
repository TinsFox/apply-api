# -*- coding: utf8 -*-
from sqlalchemy import Column, VARCHAR, PickleType
# -----------------------------------------------------------
from models import db
from models.base_model import BaseModel


class RichText(BaseModel):
    """ 存储富文本模型 """
    __tablename__ = 'rich_text'
    id = Column('ID', VARCHAR(64), primary_key=True, comment='编号')
    body = Column('Rich Text', PickleType, comment='简介')

    @staticmethod
    def insert(id, body):
        with db.auto_commit():
            rich_text = RichText()
            rich_text.id = id
            rich_text.body = body
            db.session.add(rich_text)

    @staticmethod
    def update(id, body):
        with db.auto_commit():
            rich_text = RichText.query.get_or_404(id)
            rich_text.body = body
            rich_text.update_time = rich_text.generate_datetime

    def keys(self):
        return ['body', 'update_time']
