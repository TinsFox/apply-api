from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from contextlib import contextmanager
from libs.exceptions.errors import SaveFailed


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as error:
            db.session.rollback()
            raise SaveFailed(msg=error)


db = SQLAlchemy()


from models import user
