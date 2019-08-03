# -*- coding: utf8 -*-
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
            'data': self.message,
            'code': self.errcode,
        }

    def get_body(self, environ=None):
        return json.dumps(self.generate_body)

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]


class AuthSuccess(ApiHttpException):
    code = 200
    message = '登录成功'
    errcode = 0


class UpdateSuccess(ApiHttpException):
    code = 200
    message = '密码修改成功'
    errcode = 0


class RegisterSuccess(ApiHttpException):
    code = 200
    message = '管理员注册成功'
    errcode = 0


class AuthLoginSuccess(ApiHttpException):
    code = 201
    message = "授权成功"
    errcode = 0

    def __init__(self, token):
        super(AuthLoginSuccess, self).__init__()
        self.token = token

    @property
    def generate_body(self):
        return {
            'message': self.message,
            'errcode': self.errcode,
            'access_token': self.token,
        }


class DeleteSuccess(ApiHttpException):
    code = 200
    message = u'删除成功'
    errcode = 0
