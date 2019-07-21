from werkzeug.exceptions import HTTPException
from flask import json


class ApiHttpException(HTTPException):
    message = None
    errcode = None

    def __init__(self, msg=None):
        super(ApiHttpException, self).__init__(msg)
        if msg is not None:
            self.message = msg

    @property
    def generate_body(self):
        return {
            'message': self.message,
            'errcode': self.errcode,
        }

    def get_body(self, environ=None):
        return json.dumps(self.generate_body)

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]

