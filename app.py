from flask.json import JSONEncoder as _JSONEncoder
from flask import Flask as _Flask
# ------------------------------------------
from init import create_app


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        return dict(o)


class Flask(_Flask):
    json_encoder = JSONEncoder


app = create_app(Flask(__name__))


if __name__ == '__main__':
    app.run(debug=True)
