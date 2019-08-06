# -*-coding:utf8 -*-
from wtforms import StringField, TextField
from wtforms.validators import DataRequired, Length
from libs.forms import BaseForm


class ApplyFrom(BaseForm):
    """ 用户报名表单 """
    society_id = StringField(validators=[DataRequired(message=u'社团编号字段丢失')])

    student_id = StringField(validators=[DataRequired(message=u'学号字段丢失'), Length(12, 12, message=u'学号长度不正确')])
    name = StringField(validators=[DataRequired(message=u'名字字段丢失'), Length(2, 10, message=u'名字长度为2~10位之间')])
    sex = StringField(validators=[DataRequired(message=u'性别字段丢失')])
    college = StringField(validators=[DataRequired(message=u'学院字段丢失')])
    profession = StringField(validators=[DataRequired(message=u'专业字段丢失')])
    once_work = StringField()

    phone = StringField(validators=[DataRequired(message=u'电话字段丢失'), Length(11, 11, message=u'手机号码长度不为11为数字')])
    email = StringField(validators=[Length(6, 25, message=u'邮箱长度不为6~25位之间')])
    section_id = StringField(validators=[DataRequired(u'部门编号字段丢失')])
    second_section_id = StringField()
    adjust = StringField()

    skill = TextField()
    other_organization = StringField()
    introduction = TextField()
    new_idea = TextField()
    reason = TextField()
