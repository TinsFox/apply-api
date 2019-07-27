from flask import request, jsonify, g, Response, stream_with_context, current_app
# ----------------------------------------------
from api import SmallBlueprint
from libs.token import generate_token, auth
from libs.exceptions import FormError, NotFound, RegisterFailed, RegisterSuccess, \
                            UpdateSuccess, DeleteSuccess
from libs.forms import AdminRegisterForm, AdminLoginForm, AdminChangePwdForm
from models.admin import Admin
from models.community import Section, Society, create_id, Apply
from models.rich_text import RichText

api = SmallBlueprint('admin', url_prefix='/admin')


@api.route('/register/<string:s_id>', methods=['POST'])
def admin_register(s_id):
    """
    # 管理员注册
    :param s_id: 社团编号
    """
    data = request.json
    status = AdminRegisterForm(data=data).validate()
    if not status:
        raise FormError('提交表单格式错误')
    if not Admin.query.filter_by(society_id=s_id).first():
        Admin.register(s_id, data)
    else:
        raise RegisterFailed('该社团管理员已存在')
    return RegisterSuccess()


@api.route('/login', methods=['POST'])
def admin_login():
    """ 管理员登录 """
    data = request.json
    status = AdminLoginForm(data=data).validate()
    if not status:
        raise FormError('提交表单格式错误')
    g.info = Admin.login_verify(data['account'], data['password'])
    token = {
        'acess_token': generate_token(),
        'message': '登录成功',
        'errcode': 0
    }
    return jsonify(token)


@api.route('/change', methods=['PUT'])
def admin_change_password():
    """ 管理员修改密码 """
    data = request.json
    status = AdminChangePwdForm(data=data).validate()
    if not status:
        raise FormError('提交表单格式错误')
    Admin.change_password(data['account'], data['old_pwd'], data['new_pwd'])
    return UpdateSuccess()


@api.route('/append-section', methods=['POST'])
@auth.login_required
def append_section():
    """
    # 社团管理员填写部门信息
    # TODO: 部门改动
    # 拒绝超级管理员访问
    """
    data = request.json
    society = Society.query.filter_by(id=g.society_id).first()
    for value in data.values():
        if not Section.query.filter_by(id=create_id(society.name+value)).first():
            Section.insert(society, value)
    return RegisterSuccess('保存成功')


@api.route('/delete-section/<string:s_id>', methods=['DELETE'])
@auth.login_required
def delete_section(s_id):
    """
    # 删除部门 OVER
    # 拒绝超级管理员访问
    :param s_id: 部门编号
    """
    section = Section.query.filter_by(id=s_id, society_id=g.society_id).first()
    if section:
        Apply.delete(section.applies)
        # RichText.delete(section)
        Section.delete(section)
        return DeleteSuccess()
    else:
        return NotFound('删除失败')


@api.route('/delete-society', methods=['DELETE'])
@auth.login_required
def delete_society():
    """ 删除社团 TODO"""
    society = Society.query.filter_by(id=g.society_id).first()
    if society:
        for section in society.sections:
            Apply.delete(section.applies)
        # RichText.delete(society.sections)
        Section.delete(society.sections)
        Society.delete(society)
        return DeleteSuccess()
    else:
        NotFound('该社团不存在')


@api.route('/admin-section-list', methods=['GET'])
@auth.login_required
def admin_section_list():
    """ 管理员查看部门列表 """
    society = Society.query.filter_by(id=g.society_id).first()
    return jsonify({
            'message': [section for section in society.sections],
            'errcode': 0,
            'count': len(society.sections)
        })


@api.route('/download/apply.csv', methods=['GET'])
@auth.login_required
def file_download():
    """ 社团下载报名信息"""
    def download():
        societies = []
        if g.scope == 1:
            society = Society.query.filter_by(id=g.society_id).first()
            societies.append(society)
        elif g.scope == 2:
            society = Society.query.all()
            societies.extend(society)
        yield ','.join(current_app.config['CSV_HEADER']) + '\n'
        for society in societies:
            for section in society.sections:
                users = Apply.query.filter_by(society_id=g.society_id, first_section_id=section.id).all()
                for user in users:
                    data = dict(user)
                    data['section'] = section.name
                    data['society'] = section.society.name
                    yield ','.join(data.values()) + '\n'
    return Response(stream_with_context(download()), mimetype='text/csv', headers={"Content-Disposition": "attachment; filename={}.csv;".format(g.society_id)})


