from wtforms import StringField, Form, TextField
from wtforms.validators import DataRequired, Length


class CollectionUserMessage(Form):
    """ 用户报名表单 """
    categories = StringField(validators=[DataRequired()])
    student_id = StringField(validators=[DataRequired(message='学号不能为空'), Length(12, 12)])
    name = StringField(validators=[DataRequired(), Length(2, 10)])
    sex = StringField(validators=[DataRequired()])
    college = StringField(validators=[DataRequired()])
    profession = StringField(validators=[DataRequired()])
    once_work = StringField()

    phone = StringField(validators=[DataRequired(), Length(11, 11)])
    email = StringField(validators=[Length(6, 25)])
    first_section = StringField(validators=[DataRequired()])
    second_section = StringField()
    adjust = StringField()

    skill = TextField(validators=[DataRequired()])
    other_organization = StringField()
    introduction = TextField(validators=[DataRequired()])
    new_idea = TextField(validators=[DataRequired()])
    why = TextField(validators=[DataRequired()])
