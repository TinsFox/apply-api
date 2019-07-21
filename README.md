# API

### 授权登录
##### 接口
```text
http 请求方式:　POST
/api/auth-login
```
##### 参数说明
|    参数  |　　　　　　　　说明　　　　　　　　|
|:--------:|:--------------------------------:|
|   code   |         用户授权登录凭证          |
##### 返回值
```json
{
  "message": "消息",
  "errcode": "错误码",
  "access_token": "令牌"
  
}
```

### 报名
##### 接口
```text
http 请求方式:　POST
/api/apply
```
##### 参数说明
|   　 参数  |　   　示例　   　|　　　　说明　　 　　　　　|
|:----------:|:---------------:|:------------------------:|
| student_id |       xxx       |         学号[必填]       |
| name       |       xxx       |        名字[必填]        |
| sex        |     　男/女     |         性别[必填]       |
| college    |      xx学院     |         学院[必填]       |
| profession |      xxx        |        专业[必填]        |
| phone      |      xxx        |        电话[必填]        |
| email      |    xxx@xxx.com  |        邮箱[可填]        |
| first_section |     xxx      |    第一意向部门[必填]    |
| second_section|     xxx      |    第二意向部门[可填]    |
| adjust     |    服从/不服从   |   调剂[默认不服从]       |
##### 返回值
```json
{
  "message": "消息",
  "errcode": "错误码"
}
```

### 统计人数
##### 接口
```text
http 请求方式:　GET
/api/apply/count
```
##### 返回值
```json
{
  "message": "消息",
  "errcode": "错误码",
  "count": "人数"
  
}
```
