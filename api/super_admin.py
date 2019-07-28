# -*-coding:utf8 -*-
from flask import request, jsonify
# ----------------------------------------------
from api import SmallBlueprint
from models.community import Society, Section, Apply
from libs.exceptions import EmptyError, DeleteSuccess, NotFound
from libs.token import auth


api = SmallBlueprint('super-admin', url_prefix='/admin')


@api.route('/append-society', methods=['POST'])
@auth.login_required
def append_society():
    """ 添加社团 """
    count = 0
    data = request.json
    if not data:
        raise EmptyError()
    for value in data.values():
        if not Society.query.filter_by(name=value).first():
            Society.insert(value)
            count += 1
    return jsonify({
        'message': '社团名称写入成功',
        'errcode': 0,
        'count': count
    })





