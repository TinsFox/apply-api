from flask import request
# ---------------------------------------------
from models.apply import Apply
from api import SmallBlueprint
from libs.forms.user import CollectionUserMessage
from libs.exceptions.errors import UpdateApplySuccess, ApplySuccess, ApplyFailed


api = SmallBlueprint('apply')


@api.route('/apply', methods=['POST'])
def apply():
    """ 向 MySQL 插入用户报名信息"""
    form = CollectionUserMessage(request.form)
    if form.validate():
        if Apply.query.filter_by(student_id=request.form.get('student_id')).first():
            Apply.update_user_info(request.form)
            return UpdateApplySuccess()
        Apply.insert_to_db(request.form)
        return ApplySuccess()
    else:
        raise ApplyFailed()



