from wtforms import Form
from libs.exceptions.errors import FormError


class BaseForm(Form):
    def validate_or_error(self):
        if not super(BaseForm, self).validate():
            raise FormError(u'提交信息格式错误')
        return self



