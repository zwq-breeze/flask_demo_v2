# -*- coding:utf-8 -*-
# -*- zanyunfei@datagrand.com -*-
# -*- 2020/5/7 -*-

from flask_marshmallow import Schema

from app.common.common import StatusEnum
from app.common.patch import fields


class UserSchema(Schema):  # type: ignore
    user_id = fields.Integer(attribute="id")
    user_name = fields.String(attribute="name")
    user_pw = fields.String(attribute="pw")
    create_time = fields.String(attribute="created_time")
    update_time = fields.DateTime(attribute="updated_time")
