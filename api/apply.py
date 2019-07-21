from flask import request
# ---------------------------------------------
from models.user import ApplyMessage
from api import SmallBlueprint
from libs.token import auth
from libs.user_msg_form import CollectionUserMessage
from libs.exceptions.errors import UpdateApplySuccess, ApplySuccess, ApplyFailed


apply_api = SmallBlueprint('apply', url_prefix='/apply')


@apply_api.route('/', methods=['POST'])
# @auth.login_required
def apply():
    """ 向 MySQL 插入用户报名信息"""
    form = CollectionUserMessage(request.form)
    if form.validate():
        if ApplyMessage.user_is_exist(request.form.get('student_id')):
            ApplyMessage.update_user_info(request.form)
            return UpdateApplySuccess()
        ApplyMessage.insert_to_db(request.form)
        return ApplySuccess()
    else:
        raise ApplyFailed()


@apply_api.route('/count', methods=['GET'])
# @auth.login_required
def apply_count():
    """ 查询数据库记录 """
    return ApplyMessage.get_count(), 200
