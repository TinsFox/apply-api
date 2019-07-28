# -*-coding:utf8 -*-
from flask import jsonify
# ---------------------------------
from api import SmallBlueprint
from models.community import Society
from models.rich_text import RichText


api = SmallBlueprint('open', url_prefix='/open')


@api.route('/society-list', methods=['GET'])
def society_list():
    """ 社团列表 TODO"""
    society = Society.query
    return jsonify({
        'message': society.all(),
        'count': society.count(),
        'errcode': 0
    })


@api.route('/section-list/<string:s_id>', methods=['GET'])
def section_list(s_id):
    """ 部门列表 TODO"""
    society = Society.query.filter_by(id=s_id).first()
    return jsonify({
            'message': [section for section in society.sections],
            'errcode': 0,
            'count': len(society.sections)
        })


@api.route('/get-brief/<string:s_id>', methods=['GET'])
def get_brief(s_id):
    """
    # 获取简介
    :param s_id: 社团编号或部门编号,即要获取简介的信息
    """
    info = RichText.query.filter_by(id=s_id).first()
    if info:
        return {
            'message': info.body,
            'errcode': 0,
        }
    else:
        return {}


