# -*- coding:utf-8 -*-
# -*- zanyunfei@datagrand.com -*-
# -*- 2020/4/28 -*-
from flask_restful import Api
from app.resource.v2.dashboard import view as dashboardview



routes = {
        '/demo':dashboardview.DemoResource,  # demo user
}

def add_routes(flask_app):
    api = Api(flask_app)
    for url, handler in routes.items():
            api.add_resource(handler, url)