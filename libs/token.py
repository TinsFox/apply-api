from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from flask import current_app
# --------------------------------------------------
from libs.exceptions.errors import InvalidToken, ExpirationFailed


auth = HTTPTokenAuth()


def generate_token(openid):
    """ 生成 token 令牌 """
    serializer = Serializer(current_app.config['APP_SECRET'], expires_in=current_app.config['EXPIRATION'])
    acess_token = serializer.dumps({
        'appid': current_app.config.get('APP_ID'),
        'appsceret': current_app.config.get('APP_SECRET'),
        'openid': openid
    })
    return acess_token.decode('ascii')


@auth.verify_token
def verify_token(token):
    """ 验证 token 令牌 """
    serializer = Serializer(current_app.config['APP_SECRET'])
    try:
        data = serializer.loads(token)
    except SignatureExpired:
        raise ExpirationFailed()
    except BadSignature:
        raise InvalidToken()
    else:
        return True
