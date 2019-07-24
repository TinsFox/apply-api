from libs.exceptions.base import ApiHttpException


class AuthFailed(ApiHttpException):
    """ 授权失败 """
    code = 401
    message = '登录失败'
    errcode = 4111


class RegisterFailed(ApiHttpException):
    """ 注册失败 """
    code = 400
    message = '注册失败'
    errcode = 4112



