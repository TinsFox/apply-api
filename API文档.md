# <center>API文档</center>

<hr/>

### 管理员账号注册
- [x] 测试
- 请求方式: ***POST***
- API: *http://127.0.0.1:5000/api/open/register/社团编号*
- 权限: 无
- 参数:
```json
{
    "account": "账号(4-12位)",
    "password":"密码(6-18位)"
}
```
- 成功返回值:
```json
 "message": "注册成功",
 "errcode": 0
```
- 失败返回值
```json
 "message": "失败信息",
 "errcode": "错误码"
```
<hr/>

### 管理员登录
- [x] 测试
- 请求方式: ***POST***
- API: *http://127.0.0.1:5000/api/open/login*
- 权限: 无
- 参数:
```json
{
    "account": "账号(4-12位)",
    "password":"密码(6-18位)"
}
```
- 成功返回值:
```json
 "acess_token": "token值",
 "message": "登录成功",
 "errcode": 0
```
- 失败返回值:
```json
 "message": "失败信息",
 "errcode": "错误码"
```
<hr/>

### 管理员修改密码
- [x] 测试
- 请求方式: ***PUT***
- API: *http://127.0.0.1:5000/api/open/change*
- 权限: 无
- 参数:
```json
{
    "account": "账号(4-12位)",
    "old_pwd":"旧密码(6-18位)",
    "new_pwd": "新密码(6-18位)",
    "confirm_pwd": "确认密码(6-18位)"
}
```
- 成功返回值:
```json
 "message": "密码修改成功",
 "errcode": 0
```
- 失败返回值:
```json
 "message": "失败信息",
 "errcode": "错误码"
```
<hr/>

### 获取社团列表
- [x] 测试
- 请求方式: ***GET***
- API: *http://127.0.0.1:5000/api/open/society-list*
- 权限: 无
- 成功返回值:
```json
 {
    "count": "总社团数量",
    "errcode": 0,
    "message": [
        {
            "id": "社团编号",
            "name": "名字",
            "update_time": "2019-07-29"
        },
        ]
}
```
- 失败返回值:
```json
 "message": "失败信息",
 "errcode": "错误码"
```
<hr/>

### 获取部门列表
- [x] 测试
- 请求方式: ***GET***
- API: *http://127.0.0.1:5000/api/open/section-list/社团编号*
- 权限: 无
- 成功返回值:
```json
{
  "count": "当前社团的部门的数量",
  "errcode": 0,
  "message": [
    {
      "id": "部门编号",
      "name": "名称",
      "update_time": "2019-07-29"
    }
  ]
}
```
- 失败返回值:
```json
 "message": "失败信息",
 "errcode": "错误码"
```
<hr/>

### 获取社团简介
- [x] 测试
- 请求方式: ***GET***
- API: *http://127.0.0.1:5000/api/open/get-brief/社团编号*
- 权限: 无
- 成功返回值:
```json
{
  "errcode": 0,
  "message": {
    "body": {"内容"}
    },
  "update_time":""
```
<hr/>

### 用户报名
- [x] 测试
- 请求方式: ***POST***
- API: *http://127.0.0.1:5000/api/open/apply*
- 权限: 无
- 参数
```json
{
	"student_id": "学号(12位)[必填]",
	"name": "名字[必填]",
	"sex": "男或女[必填]",
	"college":"学院[必填]",
	"profession":"专业班级[必填]",
	"once_work":"曾任职务[选填]-默认[无]",
	"phone": "联系电话(11位)[必填]",
	"email":"邮箱[必填]",
	"section_id": "意向部门编号[必填]",
	"society_id": "社团编号[必填]",
	"second_section_id": "第二意向部门编号[选填]-默认[无]",
	"adjust":"服从/不服从调剂[选填]-默认[不服从]",
	"skill":"技能[必填]",
	"other_organization":"是否加入其他组织[选填]-默认[无]",
	"introduction":"简介[必填]",
	"new_idea":"新奇想法[必填]",
	"reason":"加入该社团原因[必填]"
}
```
- 成功返回值:
```json
 "message": "报名成功",
 "errcode": 0
```
<hr/>

### 收集用户信息
- [x] 测试
- 请求方式: ***POST***
- API: *http://127.0.0.1:5000/api/open/user*
- 权限: 无
- 参数:
```json
{
   "code":""
}
```
- 成功返回值:
```json
{
  "errcode": 0,
  "message": "保存成功"
```
<hr/>

### 添加部门
- [x] 测试
- 请求方式: ***POST***
- API: *http://127.0.0.1:5000/api/admin/append-section*
- 权限: 社团管理员
- 参数:
```json
{
    "1": "部门1",
    "2": "部门2",
    "..": "部门..",
}
```
- 成功返回值:
```json
{
   "message": "添加部门成功",
   "errcode": 0,
   "count": "添加成功数量, 0即不成功"
}
```
- 失败返回值:
```json
 "message": "失败信息",
 "errcode": "错误码"
```
<hr/>

### 删除部门
- [x] 测试
- 请求方式: ***DELETE***
- API: *http://127.0.0.1:5000/api/admin/delete-section/部门编号*
- 权限: 社团管理员
- 说明: 部门连同该部门的报名信息都会删除掉
- 成功返回值:
```json
 "message": "删除成功",
 "errcode": 0
```
- 失败返回值:
```json
 "message": "失败信息",
 "errcode": "错误码"
```
<hr/>

### 查询用户报名信息
- [x] 测试
- 请求方式: ***GET***
- API: *http://127.0.0.1:5000/api/admin/user-info/学号*
- 权限: 社团管理员
- 成功返回值:
```json
{
    "errcode": 0,
    "message": {
        "adjust": "",
        "college": "",
        "email": "",
        "introduction": "",
        "name": "",
        "new_idea": "",
        "once_work": "",
        "other_organization": "",
        "phone": "",
        "profession": "",
        "reason": "",
        "section": "",
        "sex": "",
        "skill": "",
        "society": "",
        "student_id": "",
        "update_time": ""
    }
}
```
- 失败返回值:
```json
 "message": "失败信息",
 "errcode": "错误码"
```
<hr/>

### 获取部门报名信息
- [x] 测试
- 请求方式: ***GET***
- API: *http://127.0.0.1:5000/api/admin/section-info/部门编号*
- 权限: 社团管理员
- 成功返回值:
```json
{
    "errcode": 0,
    "message": ["信息"]
}
```
- 失败返回值:
```json
 "message": "失败信息",
 "errcode": "错误码"
```
<hr/>

### 获取社团报名信息
- [x] 测试
- 请求方式: ***GET***
- API: *http://127.0.0.1:5000/api/admin/society-info*
- 权限: 社团管理员
- 成功返回值:
```json
{
    "errcode": 0,
    "message": {
                "部门1":["信息1"],
                "部门2":["信息2"],
                }
}
```
- 失败返回值:
```json
 "message": "失败信息",
 "errcode": "错误码"
```
<hr/>

### 查看部门列表[管理员]
- [x] 测试
- 请求方式: ***GET***
- API: *http://127.0.0.1:5000/api/admin/admin-section-list*
- 权限: 社团管理员
- 成功返回值:
```json
 "message": ["部门列表"],
 "count": "部门数量",
 "errcode": 0
```
- 失败返回值:
```json
 "message": "失败信息",
 "errcode": "错误码"
```
<hr/>

### 重置社团报名信息
- [x] 测试
- 请求方式: ***DELETE***
- API: *http://127.0.0.1:5000/api/admin/reset*
- 权限: 社团管理员
- 说明: 只删除该社团的用户报名信息
- 成功返回值:
```json
{
    "errcode": 0,
    "message": "重置成功"
}
```
- 失败返回值:
```json
 "message": "失败信息",
 "errcode": "错误码"
```
<hr/>


### 添加社团简介
- [x] 测试
- 请求方式: ***POST***
- API: *http://127.0.0.1:5000/api/admin/append-brief*
- 权限: 社团管理员
- 参数:
```
{
    "信息随意"
}
```
- 成功返回值:
```json
{
    "errcode": 0,
    "message": "信息保存成功"
}
```
- 失败返回值:
```json
 "message": "失败信息",
 "errcode": "错误码"
```
<hr/>

### 文件下载
- [x] 测试
- 请求方式: ***GET***
- API: *http://127.0.0.1:5000/api/admin/download/apply.csv*
- 权限: 社团管理员/超级管理员
<hr/>

### 添加社团
- [x] 测试
- 请求方式: ***POST***
- API: *http://127.0.0.1:5000/api/admin/append-society*
- 权限: 超级管理员
- 参数:
```json
{
	"1": "社团名字1",
	"2": "社团名字2",
	"3": "社团名字3",
	"4": "社团名字4",
	"5": "社团名字5",
	"...": "..."
}
```
- 成功返回值:
```json
{
    "count": "添加成功的数目",
    "errcode": 0,
    "message": "添加社团成功"
}
```
- 失败返回值:
```json
 "message": "失败信息",
 "errcode": "错误码"
```
<hr/>

### 删除社团
- [x] 测试
- 请求方式: ***DELETE***
- API: *http://127.0.0.1:5000/api/admin/delete-society/社团编号*
- 权限: 超级管理员
- 说明: 社团,简介,部门,用户报名信息都会被删除,注意使用
- 成功返回值:
```json
{
    "errcode": 0,
    "message": "添加社团成功"
}
```
- 失败返回值:
```json
 "message": "失败信息",
 "errcode": "错误码"
```
<hr/>
