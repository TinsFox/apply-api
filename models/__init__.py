from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from flask_sqlalchemy import BaseQuery as _BaseQuery
from contextlib import contextmanager
import time
import hashlib
from libs.exceptions.errors import ServerError, NotFound


class BaseQuery(_BaseQuery):
    """ 重写类方法 """

    def first_or_404(self, description=None):
        rv = self.first()
        if rv is None:
            if not description:
                raise NotFound(u"该用户不存在")
            else:
                raise NotFound(description)
        return rv

    def get_or_404(self, ident, description=None):
        rv = self.get(ident)
        if rv is None:
            if not description:
                raise NotFound(u"该用户不存在")
            else:
                raise NotFound(description)
        return rv


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as error:
            print(error)
            db.session.rollback()
            raise ServerError(error)


def get_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())


def generate_id(data):
    md = hashlib.md5()
    md.update(data.encode('utf8'))
    return md.hexdigest()


db = SQLAlchemy(query_class=BaseQuery)

from models import admin, community
