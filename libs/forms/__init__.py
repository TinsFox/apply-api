from wtforms import Form
from libs.exceptions.errors import FormError


class BaseForm(Form):
    def validate_or_error(self):
        data = []
        if not super(BaseForm, self).validate():
            for value in self.errors.values():
                data.extend(value)
            raise FormError(msg='表单格式错误', data=data)
        return self



