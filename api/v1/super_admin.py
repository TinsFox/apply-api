# -*- coding: utf8 -*-
from flask import request
from api import SmallBlueprint
from libs.token import auth
from libs.exceptions import EmptyError, DeleteSuccess, RegisterSuccess
from models.community import Society, Apply
from models.rich_text import RichText


api = SmallBlueprint('super', url_prefix='/v1')


@api.route('/society', methods=['POST'])
@auth.login_required
def append_society():
    """
    # 添加社团
    :return:
    """
    count = 0
    data = request.json
    if not data:
        raise EmptyError()
    for value in data.values():
        if not Society.query.filter_by(name=value).first():
            Society.insert(value)
            count += 1
    return RegisterSuccess(msg='社团添加成功', data={'count': count})


@api.route('/society/<string:id>', methods=['DELETE'])
@auth.login_required
def delete_society(id):
    """
    # 删除社团
    # status:
    :param id: 社团唯一身份标识
    :return:
    """
    society = Society.query.get_or_404(id, description=u'删除失败,该社团不存在')
    for section in society.sections:
        Apply.delete(section.applies)
        section.delete()
    society.delete()
    try:
        rich_text = RichText.query.get_or_404(id)
    except Exception:
        raise DeleteSuccess()
    else:
        rich_text.delete()
    return DeleteSuccess()
