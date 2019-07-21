from flask import request, current_app
import requests
# ----------------------------------------------
from api import SmallBlueprint
from libs.token import generate_token, auth
from libs.exceptions.errors import AuthLoginFailed, AuthLoginSuccess

auth_api = SmallBlueprint('auth')


@auth_api.route('/auth-login', methods=['POST'])
def auth_login():
    """ 授权登录信息 """
    form = request.form
    print(form)
    app_id = current_app.config.get('APP_ID')
    app_secret = current_app.config.get('APP_SECRET')
    code = form.get('code')
    if not all((app_id, app_secret, code)):
        raise AuthLoginFailed()
    openid = request_wx_api(app_id, app_secret, code)
    token = generate_token(openid)
    print(token)
    return AuthLoginSuccess(token)


def request_wx_api(app_id, app_secret, code):
    """
    # 请求微信接口
    :param app_id:
    :param app_secret:　
    :param code: 用户登录凭证
    """
    errcode = {
        '-1': '系统繁忙，此时请开发者稍候再试',
        '40029': 'code无效',
        '45011': '频率限制，每个用户每分钟100次',
    }
    response = requests.get(current_app.config.get('AUTH_LOGIN_URL').format(app_id, app_secret, code))
    response.encoding = response.apparent_encoding
    content = response.json()
    if 'errcode' in content.keys() and content.get('errcode') == 0:
        raise AuthLoginFailed(msg=errcode[content.get('errcode')])
    return content.get('openid')
