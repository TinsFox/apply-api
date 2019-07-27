SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/API?charset=utf8'

SQLALCHEMY_TRACK_MODIFICATIONS = False

AUTH_LOGIN_URL = 'https://api.weixin.qq.com/sns/jscode2session?appid={}&secret={}&js_code={}&grant_type=authorization_code'

# token过期时间
EXPIRATION = 60 * 60 * 60

# 输出csv格式
CSV_HEADER = ['学号', '名字', '性别', '学院', '专业班级', '电话', '邮箱', '曾任职务', '技能、特长', '是否加入其它组织', '个人简介', '新奇的想法', '加入社团原因',
              '是否服从调剂', '部门', '社团']


