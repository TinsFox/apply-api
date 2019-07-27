# API文档

<hr/>

## 开放接口
### 用户报名
- 请求方式: POST
- URL: 'http://127.0.0.1:5000/api/open/apply'
- 参数:
```json
{
	"student_id": "学号",
	"name": "名字",
	"sex": "性别",
	"college":"学院",
	"profession":"专业班级",
	"phone": "电话",
	"email":"邮箱",
	"first_section_id": "意向部门编号",
	"second_section_id": "第二意向部门编号[可选]",
	"society_id": "社团编号",
	"once_work":"曾任职务",
	"skill":"技能",
	"other_organization":"是否加入其他组织",
	"introduction":"简介",
	"new_idea":"新奇想法",
	"reason":"加入该社团原因"
}
```
### 管理员注册
- 请求方式: POST
- URL: 'http://127.0.0.1:5000/api/admin/register/社团ID'
```json
{
	"account": "账号",
	"password": "密码"
}
```
### 管理员登录
- 请求方式: POST
- URL: 'http://127.0.0.1:5000/api/admin/login'
- 参数:
```json
{
	"account":"账户",
	"password":"密码"
}
```

### 管理员修改密码
- 请求方式: POST
- URL: 'http://127.0.0.1:5000/api/admin/change'
- 权限: 开放
- 参数:
```json
{
	"account":"账户",
	"old_pwd":"旧密码",
	"new_pwd":"新密码",
	"confirm_pwd":"确认密码"
}
```
### 获取社团列表
- 请求方式: GET
- URL: 'http://127.0.0.1:5000/api/open/society-list'

### 获取部门列表
- 请求方式: GET
- URL: 'http://127.0.0.1:5000/api/open/section-list/<社团ID>'


### 获取简介
- 请求方式: GET
- URL: 'http://127.0.0.1:5000/api/open/get-brief/<社团\部门ID>' 



<hr/>

## 社团管理员
### 删除社团
- 请求方式: DELETE
- URL: 'http://127.0.0.1:5000/api/admin/delete-society/<社团ID>'

### 删除部门
- 请求方式: DELETE
- URL: 'http://127.0.0.1:5000/api/admin/delete-section/<部门ID>'

### 填写部门信息
- 请求方式: POST
- URL: 'http://127.0.0.1:5000/api/admin/append-section'
- 参数:
```json
{
  "1": "部门"
}
```
### 部门列表
- 请求方式: GET
- URL: 'http://127.0.0.1:5000/api/admin/admin-section-list'

### 填写社团简介
- 请求方式: POST
- URL: 'http://127.0.0.1:5000/api/admin/append-society-brief'

### 填写部门简介
- 请求方式: POST
- URL: 'http://127.0.0.1:5000/api/admin/append-section-brief/<部门ID编号>'

## 超级管理员\社团管理员
### 文件下载
- 请求方式: GET
- URL: 'http://127.0.0.1:5000/api/admin/download/apply.csv'
- 权限: 社团管理员


## 超级管理员
### 添加社团
- 请求方式: POST
- URL: 'http://127.0.0.1:5000/api/admin/append_society'
- 权限: 超级管理员
```json
{
	"1": "社团名称"
}
```