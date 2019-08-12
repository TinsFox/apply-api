# -*- coding: utf8 -*-
from flask import current_app, stream_with_context, Response, g, request, jsonify
import xlrd
# -------------------------------------------------------------
from api import SmallBlueprint
from libs.token import auth
from models.community import Society, Apply, Section
from models import generate_id
from libs.exceptions import FormError, RegisterSuccess


api = SmallBlueprint('download', url_prefix='/v1')


@api.route('/download', methods=['GET'])
@auth.login_required
def file_download():
    """
    # 社团下载报名信息
    # status: OVER
    """
    def download():
        societies = []
        if g.scope == 1:
            society = Society.query.get_or_404(g.society_id)
            societies.append(society)
        elif g.scope == 2:
            society = Society.query.all()
            societies.extend(society)
        yield ','.join(current_app.config['CSV_HEADER']) + '\n'
        for society in societies:
            for section in society.sections:
                users = Apply.query.filter_by(society_id=society.id, section_id=section.id).all()
                for user in users:
                    data = dict(user, **{'section': section.name, 'society': society.name,
                                'time': str(user.update_time)})
                    yield ','.join(data.values()) + '\n'
    return Response(stream_with_context(download()), mimetype='text/csv', headers={"Content-Disposition": "attachment; filename={}.csv;".format(g.society_id)})


@api.route('/upload', methods=['POST'])
@auth.login_required
def file_upload():
    """
    # 文件上传
    # status: OVER
    :return:
    """
    success_count = 0
    file = request.files['file']
    if file and allowed_file(file.filename):
        data = xlrd.open_workbook(file_contents=file.read())
        if data.sheet_loaded(data.sheet_names()[-1]):
            table = data.sheets()[0]
            if not isinstance(table.cell_value(0, 1), str):
                raise FormError(u'文件上传失败,请检查表中格式是否正确')
            if '社团' not in table.cell_value(0, 1):
                raise FormError(u'文件上传失败,请检查表中格式是否正确')
            for num in range(1, table.nrows):
                count = 1   # 第一列
                for row in table.row_values(num):
                    # id = None
                    if count == 1: pass     # 序号列
                    elif count == 2:        # 社团列
                        id = generate_id(row)
                        if not Society.query.filter_by(name=row).first():
                            Society.insert(row)
                    else:
                        if not row:
                            continue
                        society = Society.query.get(id)
                        if not Section.query.filter_by(name=row, society_id=id).first():
                            Section.insert(society, row)
                            success_count += 1
                    count += 1
    else:
        raise FormError(msg=u'文件上传失败,文件后缀错误')
    return RegisterSuccess(msg=u'数据导入成功', data={'count': success_count})


def allowed_file(filename):
    """
    :param filename: 文件名
    :return: True or False
    """
    return '.' in filename and filename.split('.')[-1] in ['xls', 'csv']
