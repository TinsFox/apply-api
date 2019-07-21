from flask import Flask
from models import db
from api import api_blueprint


def create_app():
    app = Flask(__name__)
    api = api_blueprint()
    app.config.from_object('config.config')
    app.config.from_object('config.secret_config')
    db.init_app(app=app)
    app.register_blueprint(blueprint=api)

    with app.app_context():
        db.create_all()
    return app
