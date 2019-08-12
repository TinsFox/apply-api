# <center>API文档</center>

<hr/>

### 管理员账号注册
- [x] 测试
- 请求方式: ***POST***
- API: *http://127.0.0.1:5000/api/v1/register/社团编号*
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
{
    "code": 0,
    "data": {
        "list": [
            {
                "count": 0
            }
        ]
    },
    "msg": "社团添加成功"
}
```
- 失败返回值(示例):
```json
{
    "code": "xx",
    "data": {
        "errlist": []
    },
    "msg": ""
}
```
<hr/>

### 管理员登录
- [x] 测试
- 请求方式: ***POST***
- API: *http://127.0.0.1:5000/api/v1/login*
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
{
    "code": 0,
    "data": {
      "list": []
    },
    "msg": ""
}
```
- 失败返回值(示例):
```json
{
    "code": "xx",
    "data": {
        "errlist": []
    },
    "msg": ""
}
```
<hr/>

### 管理员修改密码
- [x] 测试
- 请求方式: ***PUT***
- API: *http://127.0.0.1:5000/api/v1/change*
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
{
    "code": 0,
    "data": {
      "list": []
    },
    "msg": ""
}
```
- 失败返回值:
```json
{
    "code": "xx",
    "data": {
        "errlist": []
    },
    "msg": ""
}
```
<hr/>

### 添加社团
- [x] 测试
- 请求方式: ***POST***
- API: *http://127.0.0.1:5000/api/v1/society*
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
    "code": 0,
    "data": {
        "list": [
            {
                "count": 0
            }
        ]
    },
    "msg": "社团添加成功"
}
```
- 失败返回值:
```json
{
    "code": 4008,
    "data": {
        "errlist": []
    },
    "msg": "提交的信息不能为空值"
}
```
<hr/>

### 获取社团列表
- [x] 测试
- 请求方式: ***GET***
- API: *http://127.0.0.1:5000/api/v1/society/页数*
- 权限: 无
- 成功返回值:
```json
{
    "code": 0,
    "data": {
        "list": [
            {
                "id": "c4ca4238a0b923820dcc509a6f75849b",
                "name": "1",
                "update_time": "2019-08-06"
            }
        ],
        "max_page": 1
    },
    "msg": "获取社团列表成功"
}
```
- 失败返回值:
```json
{
    "code": 4001,
    "data": {
        "errlist": []
    },
    "msg": "该页不存在"
}
```
<hr/>

### 删除社团
- [x] 测试
- 请求方式: ***DELETE***
- API: *http://127.0.0.1:5000/api/v1/society/社团编号*
- 权限: 超级管理员
- 说明: 社团,简介,部门,用户报名信息都会被删除,注意使用
- 成功返回值:
```json
{
    "code": 0,
    "data": {
        "list": []
    },
    "msg": "删除成功"
}
```
- 失败返回值:
```json
{
    "code": 4001,
    "data": {
        "errlist": []
    },
    "msg": "删除失败,该社团不存在"
}
```
<hr/>

### 添加部门
- [x] 测试
- 请求方式: ***POST***
- API: *http://127.0.0.1:5000/api/v1/section*
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
    "code": 0,
    "data": [
        {
            "count": 0
        }
    ],
    "msg": "部门添加成功"
}
```
- 失败返回值:
```json
{
    "code": "xx",
    "data": {
        "errlist": []
    },
    "msg": ""
}
```
<hr/>

### 获取部门列表
- [x] 测试
- 请求方式: ***GET***
- API: *http://127.0.0.1:5000/api/v1/section/社团编号*
- 权限: 无
- 成功返回值:
```json
{
    "code": 0,
    "data": {
      "list": []
    },
    "msg": ""
}
```
- 失败返回值:
```json
{
    "code": "xx",
    "data": {
        "errlist": []
    },
    "msg": ""
}
```
<hr/>

### 查看部门列表[管理员]
- [x] 测试
- 请求方式: ***GET***
- API: *http://127.0.0.1:5000/api/v1/section*
- 权限: 社团管理员
- 成功返回值:
```json
{
    "code": 0,
    "data": {
      "list": []
    },
    "msg": ""
}
```
- 失败返回值:
```json
{
    "code": "xx",
    "data": {
        "errlist": []
    },
    "msg": ""
}
```
<hr/>
### 删除部门
- [x] 测试
- 请求方式: ***DELETE***
- API: *http://127.0.0.1:5000/api/v1/section/部门编号*
- 权限: 社团管理员
- 说明: 部门连同该部门的报名信息都会删除掉
- 成功返回值:
```json
{
    "code": 0,
    "data": {
      "list": []
    },
    "msg": ""
}
```
- 失败返回值:
```json
{
    "code": "xx",
    "data": {
        "errlist": []
    },
    "msg": ""
}
```
<hr/>

### 添加社团简介
- [x] 测试
- 请求方式: ***POST***
- API: *http://127.0.0.1:5000/api/v1/brief*
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
    "code": 0,
    "data": {
      "list": []
    },
    "msg": ""
}
```
- 失败返回值:
```json
{
    "code": "xx",
    "data": {
        "errlist": []
    },
    "msg": ""
}
```
<hr/>

### 获取社团简介
- [x] 测试
- 请求方式: ***GET***
- API: *http://127.0.0.1:5000/api/v1/brief/社团编号*
- 权限: 无
- 成功返回值:
```json
{
    "code": 0,
    "data": {
      "list": []
    },
    "msg": ""
}
```
- 失败返回值
```json
{
    "code": "xx",
    "data": {
        "errlist": []
    },
    "msg": ""
}
```
<hr/>

### 用户报名
- [x] 测试
- 请求方式: ***POST***
- API: *http://127.0.0.1:5000/api/v1/user*
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
{
    "code": 0,
    "data": {
      "list": []
    },
    "msg": ""
}
```
<hr/>

### 查询用户报名信息
- [x] 测试
- 请求方式: ***GET***
- API: *http://127.0.0.1:5000/api/v1/user/学号*
- 权限: 社团管理员
- 成功返回值:
```json
{
    "code": 0,
    "data": {
        "list":[
        {
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
            "student_id": ""
        }
    ]
    },
    "msg": "用户信息获取成功"
}
```
- 失败返回值:
```json
{
    "code": "xx",
    "data": {
        "errlist": []
    },
    "msg": ""
}
```
<hr/>

### 收集用户信息
- [x] 测试
- 请求方式: ***POST***
- API: *http://127.0.0.1:5000/api/v1/collection*
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
    "code": 0,
    "data": {
      "list": []
    },
    "msg": ""
}
```
- 失败返回值:
```json
{
    "code": "xx",
    "data": {
        "errlist": []
    },
    "msg": ""
}
```
<hr/>

### 获取部门报名信息
- [x] 测试
- 请求方式: ***GET***
- API: *http://127.0.0.1:5000/api/v1/section-info/部门编号/页数*
- 权限: 社团管理员
- 成功返回值:
```json
{
    "code": 0,
    "data": {
      "list": [],
      "max_page": 1
    },
    "msg": ""
}
```
- 失败返回值:
```json
{
    "code": "xx",
    "data": {
        "errlist": []
    },
    "msg": ""
}
```
<hr/>

### 获取社团报名信息
- [x] 测试
- 请求方式: ***GET***
- API: *http://127.0.0.1:5000/api/v1/society-info/页数*
- 权限: 社团管理员
- 成功返回值:
```json
{
    "code": 0,
    "data": {
      "list": [
      {
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
            "student_id": "",
            "section": ""
        }
        ],
      "max_page": 1
    },
    "msg": ""
}
```
- 失败返回值:
```json
{
    "code": "xx",
    "data": {
        "errlist": []
    },
    "msg": ""
}
```
<hr/>

### 重置社团报名信息
- [x] 测试
- 请求方式: ***DELETE***
- API: *http://127.0.0.1:5000/api/v1/reset*
- 权限: 社团管理员
- 说明: 只删除该社团的用户报名信息
- 成功返回值:
```json
{
    "code": 0,
    "data": {
      "list": []
    },
    "msg": ""
}
```
- 失败返回值:
```json
{
    "code": "xx",
    "data": {
        "errlist": []
    },
    "msg": ""
}
```
<hr/>

### 文件下载
- [x] 测试
- 请求方式: ***GET***
- API: *http://127.0.0.1:5000/api/v1/download*
- 权限: 社团管理员/超级管理员

<hr/>


### 文件上传
- [x] 测试
- 请求方式: ***POST***
- API: *http://127.0.0.1:5000/api/v1/upload*
- 权限: 超级管理员
- 支持文件后缀类型: `.csv`或`.xls`
- 表的格式
![表的格式](http://tva1.sinaimg.cn/large/0060lm7Tly1g5mybi3mxpj30cn02s0sw.jpg
)
- 成功返回值:
```json
{
    "code": 0,
    "data": {
      "list": []
    },
    "msg": ""
}
```
- 失败返回值:
```json
{
    "code": "xx",
    "data": {
        "errlist": []
    },
    "msg": ""
}
```
<hr/>


### 删除所有信息
- [x] 测试
- 请求方式: ***DELETE***
- API: *http://127.0.0.1:5000/api/v1/delete-all*
- 权限: 超级管理员
- 成功返回值:
```json
{
    "code": 0,
    "data": {
      "list": []
    },
    "msg": ""
}
```
