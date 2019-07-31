# 使用说明

### 环境配置 
```shell
 pip install -r requirements.txt
 ```
 
 ### 修改配置文件
 进入`config`目录,在该目录下打开`config.y`文件,修改项目所要的配置文件
 ```python
 # 配置数据库
 SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://用户名:密码@localhost/数据库?charset=utf8'
 
 # 设置token过期时间
EXPIRATION = 60 * 60 * 2
```
 ### 项目运行
 - python run.py

 ### 服务器部署
 ```shell
 # 安装 gunicorn
 pip install gunicoern

 # 运行下面命令
 nohup gunicorn -w 4 -b 0.0.0.0:5000 run:app &
```
 
 ### 请求携带token
 该`token`需要放置在`headers`中,其它方式不可以,下面图片为使用`postman`测试时`token`的携带, 格式为
 ```json
{
  "Authorization": "Bearer token(将获取到的token进行替换, Bearer为固定字段,注意二者之间需要空格)" 
}
```
 ![headers中携带token](http://tva1.sinaimg.cn/large/0060lm7Tly1g5hzoxx9l0j30ne05v3yq.jpg)
 
 
 
 
 
  
 
 
