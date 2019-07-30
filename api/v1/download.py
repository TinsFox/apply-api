# -*- coding: utf8 -*-
from flask import current_app, stream_with_context, Response, g
from api import SmallBlueprint
from libs.token import auth
from models.community import Society, Apply


api = SmallBlueprint('download', url_prefix='/admin')


@api.route('/download/apply.csv', methods=['GET'])
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
            print(1)
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
