from flask import Blueprint


Auth = True


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


def api_blueprint():
    api_bp = Blueprint('api', __name__, url_prefix='/api')

    from api.auth_login import auth_api
    from api.apply import apply_api
    from api.get_info import admin_api

    auth_api.register(api_bp)
    apply_api.register(api_bp)
    admin_api.register(api_bp)

    return api_bp
