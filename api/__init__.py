from flask import Blueprint

api_bp = Blueprint('api', __name__, url_prefix='/api')


class SmallBlueprint(object):
    def __init__(self, name, url_prefix=None):
        self.url_list = []
        self.rule = None
        self.name = name
        self.url_prefix = url_prefix

    def route(self, rule, **options):
        def decorator(view_func):
            endpoint = options.pop("endpoint", view_func.__name__)
            self.url_list.append((rule, endpoint, view_func, options))
            return view_func
        return decorator

    def register(self, app):
        for rule, enpoint, view_func, options in self.url_list:
            if self.url_prefix is None:
                self.rule = rule
            else:
                self.rule = self.url_prefix + rule
            app.add_url_rule(self.rule, enpoint, view_func, **options)


def api_blueprint(api_bp):

    from api import apply, info, super_admin, open, admin

    admin.api.register(api_bp)
    apply.api.register(api_bp)
    info.api.register(api_bp)
    super_admin.api.register(api_bp)
    open.api.register(api_bp)


    return api_bp
