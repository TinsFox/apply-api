# -*- coding: utf8 -*-
from flask import request, jsonify, g
from api import SmallBlueprint
from libs.exceptions import EmptyError, DeleteSuccess, UpdateSuccess, RegisterSuccess
from libs.token import auth
from models.community import Section, Society, Apply
from models.rich_text import RichText


api = SmallBlueprint('admin', url_prefix='/admin')


@api.route('/append-section', methods=['POST'])
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
    return jsonify({
            'data': '添加部门成功',
            'code': 0,
            'count': count
        })


@api.route('/delete-section/<string:id>', methods=['DELETE'])
@auth.login_required
def delete_section(id):
    """
    # 社团管理员删除部门,连同用户信息一起删除
    # status: TODO
    :param id: 部门唯一身份标识
    :return:
    """
    section = Section.query.get_or_404(id, description=u'删除失败, 该部门不存在')
    Apply.delete(section.applies)
    section.delete()
    return DeleteSuccess()


@api.route('/append-brief', methods=['POST'])
@auth.login_required
def append_brief():
    """
    # 添加社团简介
    # status: OVER
    :return:
    """
    data = request.json
    rich_text = RichText.query.filter_by(id=g.society_id).first()
    if rich_text:
        RichText.update(g.society_id, rich_text)
        return UpdateSuccess(u'信息更新成功')
    else:
        RichText.insert(g.society_id, data)
        return RegisterSuccess(u'信息保存成功')


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
    return DeleteSuccess(u'重置成功')


@api.route('/admin-section-list', methods=['GET'])
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
        'count': len(society.sections)
    })

