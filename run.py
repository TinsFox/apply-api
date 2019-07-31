# -*-coding:utf8 -*-
from flask.json import JSONEncoder as _JSONEncoder
from flask import Flask as _Flask
from datetime import datetime
from flask_cors import CORS
# ------------------------------------------
from init import create_app


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%d')
        return dict(o)


class Flask(_Flask):
    json_encoder = JSONEncoder


init_app = Flask(__name__)
CORS(init_app)
app = create_app(init_app)


if __name__ == '__main__':
    app.run(debug=True)
