from models import db
from api import api_blueprint


def create_app(o):
    api = api_blueprint()
    o.config.from_object('config.config')
    o.config.from_object('config.secret_config')
    db.init_app(app=o)
    o.register_blueprint(blueprint=api)

    with o.app_context():
        db.create_all()
    return o
