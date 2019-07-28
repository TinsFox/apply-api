# -*-coding:utf8 -*-
from flask import request
# ---------------------------------------------
from models.community import Apply, Section
from api import SmallBlueprint
from libs.forms.apply import ApplyFrom
from libs.exceptions import UpdateSuccess, RegisterSuccess, FormError


api = SmallBlueprint('apply', url_prefix='open')


@api.route('/apply', methods=['POST'])
def apply():
    """
    # 向 MySQL 插入用户报名信息
    # TODO 数据重复利用"""
    data = request.json
    form = ApplyFrom(data=data)
    if form.validate():
        section = Section.query.filter_by(id=data['first_section_id']).first()
        if Apply.query.filter_by(student_id=data.get('student_id'), society_id=data.get('society_id')).first():
            Apply.update_user_info(data, section)
            return UpdateSuccess('报名信息更新成功')
        Apply.insert_to_db(data, section)
        return RegisterSuccess('报名成功')
    else:
        raise FormError('提交表单格式错误')



