import typing
from flask import g
from app.common.extension import db
from enum import Enum
from sqlalchemy.sql import func


def get_attr_from_g(name: str, default=None, raise_exception=True) -> typing.Any:
    def getter():
        if not hasattr(g, name):
            if raise_exception:
                raise AttributeError(f'flask g has not attribute {name}')
            return default
        return getattr(g, name)

    return getter


class BaseEntity(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer(),primary_key=True, default=get_attr_from_g('id'))
    created_time = db.Column(db.DateTime(), default=func.now())
    updated_time = db.Column(db.DateTime(), onupdate=func.now())
    is_deleted = db.Column(db.Boolean(), default=False)


