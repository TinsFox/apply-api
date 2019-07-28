# -*-coding:utf8 -*-
from flask import jsonify, request, g
# -------------------------------------------
from api import SmallBlueprint
from models.community import Apply, Section, Society
from libs.token import auth
from libs.exceptions.errors import NotFound, Forbidden, EmptyError


api = SmallBlueprint('info', url_prefix='/admin')


@api.route('/user-info', methods=['GET'])
@auth.login_required
def user_info():
    """
    # 利用学号获取用户报名信息
    """
    data = []
    societies = []
    sections = []
    uid = request.args.get('uid')
    if len(uid) != 12:
        raise NotFound('用户ID不正确')
    if g.scope == 2:
        user = Apply.query.filter_by(student_id=uid)
    else:
        user = Apply.query.filter_by(student_id=uid, society_id=g.society_id)
    if not user.first():
        raise NotFound('该用户不存在')
    for info in user.all():
        societies.append(info.section.society.name)
        sections.append('%s-%s' % (info.section.society.name, info.section.name))
        t = dict(info, **{'section': info.section.name, 'society': info.section.society.name})
        data.append(t)
    return jsonify({
        "society": societies,
        'sections': sections,
        "message": data,
        "errcode": 0,
        "count": user.count(),
    })


@api.route('/section-info')
@auth.login_required
def section_info():
    """
    # 获取部门报名信息
    # TODO: 拒绝超级管理员访问 待定
    """
    section_id = request.args.get('section_id')
    section = Section.query.filter_by(id=section_id).first()
    if not section.applies:
        raise NotFound('该部门没有用户报名')
    return jsonify({
        'society': [section.society.name],
        'section': [section.name],
        'count': len(section.applies),
        'errcode': 0,
        'message': [_ for _ in section.applies],
    })


@api.route('/society-info', methods=['GET'])
@auth.login_required
def society_info():
    """
    # 获取社团报名信息
    # TODO: 拒绝超级管理员访问 待定
    """
    data = []
    society_id = request.args.get('society_id')
    if not society_id:
        raise EmptyError('请输入要查询的社团ID')
    # 权限控制--只能获取自己社团的报名信息
    # if society_id != g.society_id and g.scope != 2:
    #     raise Forbidden()
    users = Society.query.filter_by(id=society_id).first()
    if not users:
        raise NotFound('该社团不存在')
    for section in users.sections:
        data.append({section.name: [dict(user) for user in section.applies]})
    return jsonify({
        'society': [users.name],
        'section': [section.name for section in users.sections],
        'count': len(data),
        'errcode': 0,
        'message': data,


    })

