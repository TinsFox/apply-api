SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/API?charset=utf8'

SQLALCHEMY_TRACK_MODIFICATIONS = False

AUTH_LOGIN_URL = 'https://api.weixin.qq.com/sns/jscode2session?appid={}&secret={}&js_code={}&grant_type=authorization_code'

# token过期时间
EXPIRATION = 60 * 60 * 4

# 归属

CATEGORIES = {
    'rjcx': 1
}