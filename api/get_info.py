from flask import jsonify, request, g
# -------------------------------------------
from api import SmallBlueprint
from models.apply import Apply
from libs.token import auth
from libs.exceptions.errors import NotFound, Forbidden


api = SmallBlueprint('info', url_prefix='/get')


@api.route('/user', methods=['GET'])
@auth.login_required
def apply_user():
    """ 利用学号获取用户报名信息 """
    uid = request.args.get('uid')
    if len(uid) != 12:
        raise NotFound('用户ID不正确')
    user_info = Apply.query.filter_by(student_id=uid)
    if not user_info.first():
        raise NotFound()
    if user_info.society != g.society and g.society != '超级管理员':
        raise Forbidden('无权限查看此用户')
    return jsonify(
        message=user_info.first(),
        errcode=0
    )


@api.route('/section-info')
@auth.login_required
def section_apply_user():
    """ 获取部门报名信息 """
    society = request.args.get('society')
    section = request.args.get('section')
    # 权限控制--只能获取自己社团的报名信息
    if society != g.society and g.society != '超级管理员':
        raise Forbidden()
    users_info = Apply.query.filter_by(categories=society, first_section=section)
    if not users_info.all():
        raise NotFound('%s还未有用户报名' % section)
    return jsonify({
        'section': '%s-%s' % (society, section),
        'message': users_info.all(),
        'errcode': 0,
        'count': users_info.count(),
    })


@api.route('/society-info', methods=['GET'])
@auth.login_required
def single_society_apply_user():
    """ 获取单个社团报名信息 over"""
    society = request.args.get('society')
    # 权限控制--只能获取自己社团的报名信息
    if society != g.society and g.society != '超级管理员':
        raise Forbidden()
    users = Apply.query.filter_by(categories=society)
    if not users.all():
        raise NotFound('%s社团还未有用户报名' % society)
    return jsonify({
        'society': society,
        'message': users.all(),
        'errcode': 0,
        'count': users.count(),
    })


@api.route('/societies', methods=['GET'])
@auth.login_required
def all_society_apply_user():
    """ 获取所有社团报名信息 over"""
    users = Apply.query.filter(Apply.id > 0)
    if not users.all():
        raise NotFound('暂时还未有用户报名')
    return jsonify({
        'message': users.all(),
        'errcode': 0,
        'count': users.count(),
        'society': '超级管理员',
    })


@api.route('/count', methods=['GET'])
@auth.login_required
def apply_count():
    """ 查询数据库记录 """
    user = Apply.query.filter(Apply.id > 0)
    return jsonify({
            'errcode': 0,
            'message': '所有社团报名人数',
            'count': user.count(),
        })