# -*- coding:utf-8 -*-
# -*- zanyunfei@datagrand.com -*-
# -*- 2020/4/29 -*-

from app.common.extension import session
from app.model import UserModel
from app.schema.user_schema import UserSchema

class UserService:
    @staticmethod
    def get_by_id(id):
        user = UserModel().get_by_id(id)
        result = UserSchema().dump(user)
        return result

    @staticmethod
    def get_docs(args):
        filters = {}
        if args.get('ids'):
            filters["ids"] = args.get('ids')
        return UserModel().get_by_filter(**filters)

    @staticmethod
    def update_doc_by_id(id, args):
        user = UserModel().update(id, **args)
        session.commit()
        return user