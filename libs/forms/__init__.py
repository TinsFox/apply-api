from wtforms import Form
from libs.exceptions.errors import FormError


class BaseForm(Form):
    def validate_or_error(self):
        if not super(BaseForm, self).validate():
            msg = ''.join([_ for _ in self.errors.values()][0])
            raise FormError(msg)
        return self



