from sqlalchemy import Column, VARCHAR, INTEGER, TEXT, DATETIME
# -------------------------------------------------------
from models import db


class ApplyMessage(db.Model):
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

    __tablename__ = 'apply-users'
    id = Column('序号', INTEGER, primary_key=True, autoincrement=True)
    categories = Column('归属', VARCHAR(50), nullable=False)
    student_id = Column('学号', VARCHAR(12), unique=True, nullable=False)
    name = Column('名字', VARCHAR(30), nullable=False)
    sex = Column('性别', VARCHAR(6), nullable=False)
    college = Column('学院', VARCHAR(50), nullable=False)
    profession = Column('专业', VARCHAR(75), nullable=False)
    once_work = Column('曾任职务', VARCHAR(50))
    # ----------------------------------------------------------------
    phone = Column('联系电话', VARCHAR(11), nullable=False)
    email = Column('邮箱', VARCHAR(50))
    first_section = Column('意向部门', VARCHAR(30), nullable=False)
    second_section = Column('第二意向部门', VARCHAR(30))
    adjust = Column('是否服从调剂', VARCHAR(9))
    # ------------------------------------------------------------------
    skill = Column('特长技能', TEXT)
    other_organization = Column('是否加入其他组织', VARCHAR(50))
    introduction = Column('个人简介', TEXT, nullable=False)
    new_idea = Column('新奇的想法', TEXT, nullable=False)
    why = Column('为什么加入团队', TEXT, nullable=False)

    # create_time = Column()

    @staticmethod
    def insert_to_db(forms):
        """ 向数据库写入用户信息 """
        if isinstance(forms, dict):
            forms = dict(forms)
        with db.auto_commit():
            user = ApplyMessage()
            user = process_data(user, forms)
            db.session.add(user)

    @staticmethod
    def update_user_info(forms):
        """ 更新数据库用户信息 """
        if isinstance(forms, dict):
            forms = dict(forms)
        with db.auto_commit():
            user_info = ApplyMessage.query.filter_by(student_id=forms.pop('student_id')).first()
            process_data(user_info, forms)

    def keys(self):
        return ['categories', 'student_id', 'name', 'sex', 'college', 'profession', 'phone', 'first_section', 'second_section',
                'adjust', 'once_work', 'skill', 'other_organization', 'introduction', 'new_idea', 'why']

    def __getitem__(self, item):
        return getattr(self, item)


def process_data(user, forms):
    user.categories = forms.get('categories')
    user.name = forms.get('name')
    user.sex = forms.get('sex')
    user.college = forms.get('college')
    user.profession = forms.get('profession')
    user.once_work = forms.get('onece_work') if forms.get('onece_work') else '无'

    user.phone = forms.get('phone')
    user.email = forms.get('email') if forms.get('email') else '无'
    user.first_section = forms.get('first_section')
    user.second_section = forms.get('second_section') if forms.get('second_section') else '无'
    user.adjust = forms.get('adjust') if forms.get('adjust') else '不服从'

    user.skill = forms.get('skill')
    user.other_organization = forms.get('other_organization') if forms.get('other_organization') else '无'
    user.introduction = forms.get('introduction')
    user.new_idea = forms.get('new_idea')
    user.why = forms.get('why')

    if forms.get('student_id'):
        user.student_id = forms.get('student_id')
        return user




