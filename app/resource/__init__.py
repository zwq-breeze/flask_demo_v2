from flask import Flask
from app.common.routes import add_routes


def register_blueprint(flask_app: Flask) -> None:
    # from . import v2
    # flask_app.register_blueprint(v2.blueprint)
    add_routes(flask_app)
