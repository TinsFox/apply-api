# -*-coding:utf8 -*-
from wtforms import StringField, TextField
from wtforms.validators import DataRequired, Length
from libs.forms import BaseForm


class ApplyFrom(BaseForm):
    """ 用户报名表单 """
    society_id = StringField(validators=[DataRequired()])

    student_id = StringField(validators=[DataRequired(), Length(12, 12)])
    name = StringField(validators=[DataRequired(), Length(2, 10)])
    sex = StringField(validators=[DataRequired()])
    college = StringField(validators=[DataRequired()])
    profession = StringField(validators=[DataRequired()])
    once_work = StringField()

    phone = StringField(validators=[DataRequired(), Length(11, 11)])
    email = StringField(validators=[DataRequired(), Length(6, 25)])
    section_id = StringField(validators=[DataRequired()])
    second_section_id = StringField()
    adjust = StringField()

    skill = TextField(validators=[DataRequired()])
    other_organization = StringField()
    introduction = TextField(validators=[DataRequired()])
    new_idea = TextField(validators=[DataRequired()])
    reason = TextField(validators=[DataRequired()])
