# -*-coding:utf8 -*-
from flask import request

from api import SmallBlueprint
from models.rich_text import RichText
from libs.token import auth
from libs.exceptions import RegisterSuccess, EmptyError

api = SmallBlueprint('rich_text', url_prefix='/admin')


@api.route('/append-society-brief', methods=['POST'])
@auth.login_required
def append_society_brief():
    """ 社团管理员填写社团简介 """
    data = request.json
    if not data:
        raise EmptyError('请求提交的数据不能为空值')
    society = RichText.query.filter_by(society_id=g.society_id).first()
    if not society:
        RichText.insert(g.society_id, data)
        return RegisterSuccess('保存成功')
    else:
        RichText.update(g.society_id, data)
        return RegisterSuccess('信息更新成功')


@api.route('/append-section-brief/<string:s_id>', methods=['POST'])
@auth.login_required
def append_section_brief(s_id):
    """ 社团管理员填写部门简介 """
    data = request.json
    if not data:
        raise EmptyError('请求提交的数据不能为空值')
    if not RichText.query.filter_by(id=s_id).first():
        RichText.insert(s_id, data)
        return RegisterSuccess('保存成功')
    else:
        RichText.update(s_id, data)
        return RegisterSuccess('信息更新成功')
