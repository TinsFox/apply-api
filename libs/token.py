# -*- coding: utf8 -*-
from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from flask import current_app, request, g
# --------------------------------------------------
from libs.exceptions.errors import InvalidToken, ExpirationFailed, Forbidden
from libs.scope import scope


auth = HTTPTokenAuth()


def generate_token():
    """ 生成 token 令牌 """
    serializer = Serializer(current_app.config['APP_SECRET'], expires_in=current_app.config['EXPIRATION'])
    acess_token = serializer.dumps({
        'appid': current_app.config.get('APP_ID'),
        'appsceret': current_app.config.get('APP_SECRET'),
        'scope': g.info['scope'],
        'society_id': g.info['society_id'],
    })
    return acess_token.decode()


@auth.verify_token
def verify_token(token):
    """ 验证 token 令牌 """
    serializer = Serializer(current_app.config['APP_SECRET'])
    try:
        data = serializer.loads(token)
    except SignatureExpired:
        raise ExpirationFailed()
    except BadSignature:
        if not request.headers.get('Authorization', False):
            raise Forbidden()
        raise InvalidToken()
    else:
        auth_status = scope(data['scope'], request.endpoint)
        if auth_status:
            g.society_id = data['society_id']
            g.scope = data['scope']
            return True
        raise Forbidden()

