from sqlalchemy import Column, VARCHAR, ForeignKey, INTEGER, TEXT

from models import generate_id, db
from models.base_model import BaseModel


class Society(BaseModel):
    """ 社团 """
    __tablename__ = 'society'
    id = Column(VARCHAR(64), primary_key=True, comment='社团编号')
    name = Column('Society Name', VARCHAR(80), nullable=False, comment='社团名称')

    @staticmethod
    def insert(name):
        with db.auto_commit():
            society = Society()
            society.id = generate_id(name)
            society.name = name
            db.session.add(society)

    def keys(self):
        return ['id', 'name', 'update_time']


class Section(BaseModel):
    """ 部门 """
    __tablename__ = 'section'
    id = Column(VARCHAR(64), primary_key=True, comment='部门编号')
    name = Column('Section Name', VARCHAR(60), nullable=False, comment='部门名称')
    society_id = Column(VARCHAR(64), ForeignKey("society.id"), nullable=False, comment='社团名称')
    society = db.relationship('Society', backref='sections')

    @staticmethod
    def insert(o, name):
        """ 填写部门信息 """
        with db.auto_commit():
            section = Section()
            # print(generate_id("{0}-{1}".format(o.name, name)))
            section.id = generate_id("{0}-{1}".format(o.name, name))
            section.name = name
            section.society_id = o.id
            db.session.add(section)

    def keys(self):
        return ['id', 'name', 'update_time']


class Apply(BaseModel):
    """
    # 用户报名信息模型
    # 字符集: utf8
    # student_id: 学号[必填]
    # name: 名字[必填]
    # sex: 性别[必填]
    # college: 学院[必填]
    # profession: 专业[必填]
    # phone: 电话[必填]
    # email: 邮箱[可填]
    # first_section: 第一意向部门[必填]
    # second_section: 第二意向部门[可填]
    # adjust: 调剂[默认不服从]
    """

    __tablename__ = 'apply'
    id = Column('ID', INTEGER, primary_key=True, autoincrement=True, comment='序号')

    student_id = Column('Student ID', VARCHAR(12), nullable=False, comment='学号')
    name = Column('Name', VARCHAR(40), nullable=False, comment='名字')
    sex = Column('Sex', VARCHAR(8), nullable=False, comment='性别')
    college = Column('College', VARCHAR(80), nullable=False, comment='学院')
    profession = Column('Professional', VARCHAR(100), nullable=False, comment='专业')
    once_work = Column('Once Work', VARCHAR(50), comment='曾任职务')
    # ----------------------------------------------------------------
    phone = Column('Phone', VARCHAR(11), nullable=False, comment='联系电话')
    email = Column('Email', VARCHAR(50), nullable=False, comment='邮箱')
    society_id = Column('Society ID', VARCHAR(64), nullable=False, comment='社团编号')
    section_id = Column(VARCHAR(64), ForeignKey('section.id'), nullable=False, comment='意向部门编号')
    second_section_id = Column('Second Section', VARCHAR(64), comment='第二意向部门编号')
    adjust = Column('Adjust', VARCHAR(12), comment='是否服从调剂')
    # ------------------------------------------------------------------
    skill = Column('Skill', TEXT, nullable=False, comment='特长技能')
    other_organization = Column('Other Organization', VARCHAR(60), comment='兼其他社团')
    introduction = Column('Introduction', TEXT, nullable=False, comment='个人简介')
    new_idea = Column('Idea', TEXT, nullable=False, comment='新奇的想法')
    reason = Column('Reason', TEXT, nullable=False, comment='为什么加入团队')
    # ------------------------------------------------------------------------
    section = db.relationship('Section', backref='applies')

    @staticmethod
    def insert(data):
        """ 向数据库写入用户信息 """
        with db.auto_commit():
            user = Apply()
            user = process_data(user, data)
            db.session.add(user)

    @staticmethod
    def update(data):
        """ 更新数据库用户信息 """
        with db.auto_commit():
            user = Apply.query.filter_by(student_id=data.pop('student_id')).first()
            user.update_time = user.generate_datetime
            process_data(user, data)

    def keys(self):
        return ['student_id', 'name', 'sex', 'college', 'profession', 'phone', 'email', 'once_work', 'skill',
                'other_organization', 'introduction', 'new_idea', 'reason', 'adjust']

    @staticmethod
    def delete(data):
        """ 删除数据 """
        with db.auto_commit():
            if isinstance(data, list):
                for t in data:
                    db.session.delete(t)
            else:
                db.session.delete(data)


def process_data(user, forms):
    user.society_id = forms.get('society_id')

    user.name = forms.get('name')
    user.sex = forms.get('sex')
    user.college = forms.get('college')
    user.profession = forms.get('profession')
    user.once_work = forms.get('onece_work') if forms.get('onece_work') else '无'

    user.phone = forms.get('phone')
    user.email = forms.get('email')
    user.section_id = forms.get('section_id')
    user.second_section_id = forms.get('second_section_id') if forms.get('second_section_id') else '无'
    user.adjust = forms.get('adjust') if forms.get('adjust') else '不服从'

    user.skill = forms.get('skill')
    user.other_organization = forms.get('other_organization') if forms.get('other_organization') else '无'
    user.introduction = forms.get('introduction')
    user.new_idea = forms.get('new_idea')
    user.reason = forms.get('reason')

    # user.section = o

    if forms.get('student_id'):
        user.student_id = forms.get('student_id')
        return user
