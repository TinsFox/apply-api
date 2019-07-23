from flask import request
# ---------------------------------------------
from models.user import ApplyMessage
from api import SmallBlueprint
from libs.user_msg_form import CollectionUserMessage
from libs.exceptions.errors import UpdateApplySuccess, ApplySuccess, ApplyFailed


apply_api = SmallBlueprint('apply')


@apply_api.route('/apply', methods=['POST'])
def apply():
    """ 向 MySQL 插入用户报名信息"""
    form = CollectionUserMessage(request.form)
    if form.validate():
        if ApplyMessage.query.filter_by(student_id=request.form.get('student_id')).first():
            ApplyMessage.update_user_info(request.form)
            return UpdateApplySuccess()
        ApplyMessage.insert_to_db(request.form)
        return ApplySuccess()
    else:
        raise ApplyFailed()



