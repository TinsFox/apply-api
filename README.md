# API

### 管理员登录
- 接口
```text
http 请求方式:　POST
/api/admin-login
```
- 参数说明

|    参数  |　　　　　　　　说明　　　　　　　　|
|:--------:|:--------------------------------:|
|  account |              账户                |
| password |              密码                |

- 返回值
```json
{
  "message": "消息",
  "errcode": "错误码",
  "access_token": "令牌"
  
}
```
- `headers`中携带`token`
```json
{
  "Authorization": "Bearer token"
}

```

<hr/>
### 报名
- 接口
```text
http 请求方式:　POST
/api/apply
```
- 参数说明

|   　 参数  |　   　示例　   　|　　　　说明　　 　　　　　|
|:----------:|:---------------:|:------------------------:|
| categories |      xxxx       |      归属那个社团[必填]   |
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
- 返回值
```json
{
  "message": "消息",
  "errcode": "错误码"
}
```
<hr/>

### 统计人数
- 接口
```text
http 请求方式:　GET
/api/user/count
```
- 返回值
```json
{
  "message": "消息",
  "errcode": "错误码",
  "count": "人数"
  
}
```
<hr/>

### 获取单个用户信息
- 接口
```text
http 请求方式:　GET
/api/user/single?uid='用户学号'
```
- 返回值
```json
{
  "message": "用户报名信息",
  "errcode": "错误码"
}
```

<hr/>

### 获取所有社团用户报名信息
- 接口
```text
http 请求方式:　GET
/api/user/all
```
- 返回值
```json
{
  "message": "用户报名信息",
  "errcode": "错误码",
  "count": "人数"
  
}
```
<hr/>

### 获取单个社团用户报名信息
- 接口
```text
http 请求方式:　GET
/api/user/part?category='社团名称'
```
- 返回值
```json
{
  "message": "用户报名信息",
  "errcode": "错误码",
  "count": "人数"
  
}
```