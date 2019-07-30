# -*- coding: utf8 -*-
from flask import jsonify, request, current_app
import requests
# ------------------------------------------------
from api import SmallBlueprint
from models.community import Society, Apply
from models.user import User
from models.rich_text import RichText
from libs.exceptions import EmptyError, UpdateSuccess, RegisterSuccess, AuthFailed
from libs.forms.apply import ApplyFrom


api = SmallBlueprint('open', url_prefix='open')


@api.route('/society-list', methods=['GET'])
def society_list():
    """
    # 获取社团列表
    # status: OVER
    :return:
    """
    society = Society.query
    if not society.all():
        raise EmptyError(u'当前社团列表为空')
    return jsonify({
        'message': society.all(),
        'count': society.count(),
        'errcode': 0
    })


@api.route('/section-list/<string:id>', methods=['GET'])
def section_list(id):
    """
    # 获取部门列表
    # status: OVER
    :param id: 社团唯一身份标识
    :return:
    """
    society = Society.query.get_or_404(id)
    return jsonify({
            'message': [section for section in society.sections],
            'errcode': 0,
            'count': len(society.sections)
        })


@api.route('/get-brief/<string:id>', methods=['GET'])
def get_brief(id):
    """
    # 获取社团简介
    # status: OVER
    :param id: 社团/部门唯一身份标识
    :return:
    """
    rich_text = RichText.query.get_or_404(id, description=u'该社团不存在简介')
    return jsonify({
        'message': rich_text,
        'errcode': 0
    })


@api.route('/apply', methods=['POST'])
def user_apply():
    """
    # 用户报名
    # status: OVER
    """
    data = request.json
    ApplyFrom(data=data).validate_or_error()
    if Apply.query.filter_by(student_id=data.get('student_id'), society_id=data.get('society_id')).first():
            Apply.update(data)
            return UpdateSuccess(u'报名信息更新成功')
    Apply.insert(data)
    return RegisterSuccess(u'报名成功')


@api.route('/user', methods=['POST'])
def user():
    """
    # 收集微信用户信息
    # status: TODO 未完工
    :return:
    """
    data = request.json
    app_id = current_app.config.get('APP_ID')
    app_secret = current_app.config.get('APP_SECRET')
    code = data.get('code')
    if not code:
        raise AuthFailed()
    response = request_wx_api(app_id, app_secret, code)
    user = User.query.filter_by(openid=response['openid']).first()
    if not user:
        User.insert(response['openid'], data)
        return RegisterSuccess(u'保存成功')
    else:
        user.update(data)
        return UpdateSuccess(u'更新成功')


def request_wx_api(app_id, app_secret, code):
    """
    # 请求微信接口
    :param app_id:
    :param app_secret:　
    :param code: 用户登录凭证
    """
    errcode = {
        '-1': u'系统繁忙，此时请开发者稍候再试',
        '40029': u'code无效',
        '45011': u'频率限制，每个用户每分钟100次',
    }
    response = requests.get(current_app.config.get('AUTH_LOGIN_URL').format(app_id, app_secret, code))
    response.encoding = response.apparent_encoding
    content = response.json()
    if 'errcode' in content.keys() and content.get('errcode') != 0:
        raise AuthFailed(errcode[content.get('errcode')])
    return content
