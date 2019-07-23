from flask import jsonify, request
# -------------------------------------------
from api import SmallBlueprint
from models.user import ApplyMessage
from libs.token import auth
from libs.exceptions.errors import NotFound


admin_api = SmallBlueprint('admin', url_prefix='user')


@admin_api.route('/count', methods=['GET'])
@auth.login_required
def apply_count():
    """ 查询数据库记录 """
    user = ApplyMessage.query.filter(ApplyMessage.id > 0)
    return {
            'errcode': 0,
            'message': '全部报名人数',
            'count': user.count(),
        }


@admin_api.route('/all-society', methods=['GET'])
@auth.login_required
def get_all_society_user():
    """ 获取所有社团报名信息 """
    users_info = ApplyMessage.query.filter(ApplyMessage.id > 0)
    if not users_info.all():
        raise NotFound('还未有用户报名')
    return jsonify({
        'message': users_info.all(),
        'errcode': 0,
        'count': users_info.count(),
    })


@admin_api.route('/single-society', methods=['GET'])
@auth.login_required
def get_single_society_user():
    """ 获取单个社团报名信息 """
    society = request.args.get('society')
    users_info = ApplyMessage.query.filter_by(categories=society)
    if not users_info.all():
        raise NotFound('%s社团还未有用户报名' % society)
    return jsonify({
        'society': society,
        'message': users_info.all(),
        'errcode': 0,
        'count': users_info.count(),
    })


@admin_api.route('/society-section')
def get_section_user():
    society = request.args.get('society')
    section = request.args.get('section')
    users_info = ApplyMessage.query.filter_by(categories=society, first_section=section)
    if not users_info.all():
        raise NotFound('%s还未有用户报名' % section)
    return jsonify({
        'section': section,
        'message': users_info.all(),
        'errcode': 0,
        'count': users_info.count(),
    })


@admin_api.route('/user/single', methods=['GET'])
@auth.login_required
def get_user():
    """ 利用学号获取用户报名信息 """
    uid = request.args.get('uid')
    if len(uid) != 12:
        raise NotFound('用户ID不正确')
    user_info = ApplyMessage.query.filter_by(student_id=uid)
    if not user_info.first():
        raise NotFound()
    return jsonify(
        message=user_info.first(),
        errcode=0
    )