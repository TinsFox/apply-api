from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from contextlib import contextmanager
import time
import hashlib
from libs.exceptions.errors import ServerError


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as error:
            print(error)
            db.session.rollback()
            raise ServerError()


def get_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())


def create_id(data):
    md5 = hashlib.md5()
    md5.update(data.encode())
    return md5.hexdigest()


db = SQLAlchemy()

from models import admin, community
