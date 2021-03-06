# -*- coding: utf8 -*-
from werkzeug.exceptions import HTTPException
from flask import json


class ApiHttpException(HTTPException):
    message = "服务器繁忙"
    errcode = None
    data = []

    def __init__(self, msg=None, data=None, others=None):
        super(ApiHttpException, self).__init__(msg)
        if msg is not None:
            self.message = msg
        if data is not None:
            self.data = data
        self.others = others


    @property
    def generate_body(self):
        return {
            'code': self.errcode,
            'msg': self.message,
        }

    def get_body(self, environ=None):
        return json.dumps(self.generate_body)

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]


class ApiSuccess(ApiHttpException):
    @property
    def generate_body(self):
        t = {
            'code': self.errcode,
            'msg': self.message,
            'data':
                {
                    'list': []
                }
        }

        if self.data:
            t = dict(t, **{'data': {'list': self.data if isinstance(self.data, list) else [self.data]}})
        if self.others is not None and isinstance(self.others, dict):
            t['data'].update(self.others)
        return t


class ApiFailed(ApiHttpException):
    @property
    def generate_body(self):
        t = {
            'code': self.errcode,
            'msg': self.message,
            'data':
                {
                    'errlist': []
                }
        }
        if self.data:
            return dict(t, **{'data': {'errlist': self.data if isinstance(self.data, list) else [self.data]}})
        else:
            return t


class AuthSuccess(ApiSuccess):
    """ 授权 """
    code = 200
    errcode = 0


class UpdateSuccess(ApiSuccess):
    """ 更新 """
    code = 200
    errcode = 0


class RegisterSuccess(ApiSuccess):
    """ 添加 """
    code = 200
    errcode = 0


class DeleteSuccess(ApiSuccess):
    """ 删除 """
    code = 200
    message = u'删除成功'
    errcode = 0


class ViewSuccess(ApiSuccess):
    code = 200
    errcode = 0
