# -*- coding: utf8 -*-
from flask import g
from collections import defaultdict
# -------------------------------------------
from api import SmallBlueprint
from models.community import Apply, Section, Society
from libs.token import auth
from libs.exceptions import NotFound, ViewSuccess


api = SmallBlueprint('info', url_prefix='/v1')


@api.route('/user/<string:id>', methods=['GET'])
@auth.login_required
def user_info(id):
    """
    # 查询用户报名信息
    # status: OVER
    :param id: 学号
    :return:
    """
    if len(id) != 12:
        raise NotFound('用户ID不正确')
    user = Apply.query.filter_by(student_id=id, society_id=g.society_id).first_or_404()
    data = dict(user, **{'section': user.section.name, 'society': user.section.society.name})
    return ViewSuccess(msg=u"用户信息获取成功", data=data)


@api.route('/section-info/<string:id>/<int:page>', methods=['GET'])
@auth.login_required
def section_info(id, page):
    """
    # 获取部门报名信息
    # status: OVER
    :param id: 部门编号
    :param page: 页数
    :return:
    """
    if page <= 0:
        raise NotFound('该页不存在')
    end = page * 15
    start = end - 15
    section = Section.query.filter_by(id=id, society_id=g.society_id).first_or_404(description=u'该部门不存在')
    data = [dict(user, **{'section': section.name, 'society': section.society.name}) for user in section.applies[start: end]]
    return ViewSuccess(msg=u'%s部门报名信息获取成功' % section.name, data=data)


@api.route('/society-info', methods=['GET'])
@auth.login_required
def society_info():
    """
    # 获取社团报名信息
    :return:
    """
    data = defaultdict(list)
    society = Society.query.get_or_404(g.society_id)
    for section in society.sections:
        data[section.name].extend([dict(user, **{'section': user.section.name, 'society': user.section.society.name})
                                   for user in section.applies])
    return ViewSuccess(msg=u'社团报名信息获取成功', data=data)
