from wtforms import StringField, Form
from wtforms.validators import DataRequired, Length


class CollectionUserMessage(Form):
    """ 用户报名表单 """
    student_id = StringField(validators=[DataRequired(message='学号不能为空'), Length(12, 12)])
    name = StringField(validators=[DataRequired(), Length(2, 10)])
    sex = StringField(validators=[DataRequired()])
    college = StringField(validators=[DataRequired()])
    profession = StringField(validators=[DataRequired()])
    phone = StringField(validators=[DataRequired(), Length(11, 11)])
    email = StringField(validators=[DataRequired(), Length(6, 25)])
    first_section = StringField(validators=[DataRequired()])
    second_section = StringField()
    adjust = StringField()
