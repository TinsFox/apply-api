def register_v1_blueprint(bp):
    from api.v1 import admin, client, open, super_admin

    admin.api.register(bp)
    client.api.register(bp)
    open.api.register(bp)


