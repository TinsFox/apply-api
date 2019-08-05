# -*- coding: utf8 -*-
from flask import request, jsonify, g
from api import SmallBlueprint
from libs.exceptions import EmptyError, DeleteSuccess, UpdateSuccess, RegisterSuccess
from libs.token import auth
from models.community import Section, Society, Apply
from models.rich_text import RichText

api = SmallBlueprint('admin', url_prefix='/v1')


@api.route('/section', methods=['POST'])
@auth.login_required
def append_section():
    """
    # 社团管理员添加部门
    # status: OVER
    :return:
    """
    count = 0
    data = request.json
    if not data:
        raise EmptyError()
    society = Society.query.get_or_404(g.society_id)
    for value in data.values():
        if not Section.query.filter_by(society_id=g.society_id, name=value).first():
            Section.insert(society, value)
            count += 1
    return RegisterSuccess(msg=u'部门添加成功', data={'count': count})


@api.route('/section/<string:id>', methods=['DELETE'])
@auth.login_required
def delete_section(id):
    """
    # 社团管理员删除部门,连同用户信息一起删除
    # status: OVER
    :param id: 部门唯一身份标识
    :return:
    """
    section = Section.query.get_or_404(id, description=u'删除失败, 该部门不存在')
    Apply.delete(section.applies)
    section.delete()
    return DeleteSuccess(msg=u'部门删除成功')


@api.route('/brief', methods=['POST'])
@auth.login_required
def append_brief():
    """
    # 添加社团简介
    # status: OVER
    :return:
    """
    data = request.json
    if not data:
        raise EmptyError()
    rich_text = RichText.query.filter_by(id=g.society_id).first()
    if rich_text:
        RichText.update(g.society_id, rich_text)
        return UpdateSuccess(msg=u'社团简介更新成功')
    else:
        RichText.insert(g.society_id, data)
        return RegisterSuccess(msg=u'社团简介添加成功')


@api.route('/reset', methods=['DELETE'])
@auth.login_required
def reset_society():
    """
    # 重置社团信息
    # status: OVER
    """
    society = Society.query.get_or_404(g.society_id, description=u'重置失败,该社团不存在')
    for section in society.sections:
        Apply.delete(section.applies)
    return DeleteSuccess(u'社团报名信息重置成功')


@api.route('/section', methods=['GET'])
@auth.login_required
def admin_section_list():
    """
    # 管理员查看部门列表
    # status: OVER
    """
    society = Society.query.get_or_404(g.society_id, description=u'获取信息失败,该社团不存在')
    return jsonify({
        'data': [section for section in society.sections],
        'code': 0,
        'msg': '%s的部门列表' % society.name
    })
