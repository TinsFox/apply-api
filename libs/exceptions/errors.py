# -*-coding:utf8 -*-
from libs.exceptions.base import ApiHttpException


class AuthFailed(ApiHttpException):
    code = 401
    message = "授权失败"
    errcode = 4000


class NotFound(ApiHttpException):
    code = 404
    message = '资源不存在不存在'
    errcode = 4001


class Forbidden(ApiHttpException):
    code = 403
    message = '该页面禁止访问'
    errcode = 4002


class ServerError(ApiHttpException):
    code = 500
    message = '服务器内部错误'
    errcode = 4003


class InvalidToken(ApiHttpException):
    code = 422
    message = "访问令牌无效"
    errcode = 4004


class ExpirationFailed(ApiHttpException):
    code = 422
    message = "访问令牌过期"
    errcode = 4005


class RegisterFailed(ApiHttpException):
    """ 注册失败 """
    code = 406
    message = '注册失败'
    errcode = 4006


class FormError(ApiHttpException):
    """ 表单格式错误 """
    code = 400
    errcode = 4007


class EmptyError(ApiHttpException):
    code = 400
    message = '提交的信息不能为空值'
    errcode = 4008


class DeleteFailed(ApiHttpException):
    code = 400
    message = '删除失败'
    errcode = 4009

