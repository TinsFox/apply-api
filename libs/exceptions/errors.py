# -*- coding: utf8 -*-
from libs.exceptions.base import ApiFailed


class AuthFailed(ApiFailed):
    code = 401
    message = u"授权失败"
    errcode = 4000


class NotFound(ApiFailed):
    code = 404
    message = u'资源不存在不存在'
    errcode = 4001


class Forbidden(ApiFailed):
    code = 403
    message = u'该页面禁止访问'
    errcode = 4002


class ServerError(ApiFailed):
    code = 500
    message = u'服务器内部错误'
    errcode = 4003


class InvalidToken(ApiFailed):
    code = 422
    message = u"访问令牌无效"
    errcode = 4004


class ExpirationFailed(ApiFailed):
    code = 422
    message = u"访问令牌过期"
    errcode = 4005


class RegisterFailed(ApiFailed):
    """ 注册失败 """
    code = 406
    message = u'注册失败'
    errcode = 4006


class FormError(ApiFailed):
    """ 表单格式错误 """
    code = 400
    errcode = 4007


class EmptyError(ApiFailed):
    code = 400
    message = u'提交的信息不能为空值'
    errcode = 4008


class DeleteFailed(ApiFailed):
    code = 400
    message = u'删除失败'
    errcode = 4009


class RepeatError(ApiFailed):
    code = 200
    message = u'该用户已经存在'
    errcode = 4010
