# -*- coding:utf-8 -*-
# -*- zanyunfei@datagrand.com -*-
# -*- 2020/4/29 -*-
import typing
from abc import ABC
from sqlalchemy import not_
from app.model.base import BaseModel
from app.entity import UserEntity
from app.common.extension import session


class UserModel(BaseModel, ABC):
    def get_all(self):
        return session.query(UserEntity)
        # raise NotImplemented("no get_all")

    @staticmethod
    def is_empty_table():
        return session.query(UserEntity).filter(not_(UserEntity.is_deleted)).count() == 0

    def get_by_id(self, _id):
        return session.query(UserEntity).filter(UserEntity.id == _id, ~UserEntity.is_deleted).one()

    def get_by_filter(self, order_by="created_time", order_by_desc=True, limit=10, offset=0, **kwargs):
        q = session.query(UserEntity).filter(~UserEntity.is_deleted)
        for key, val in kwargs.items():
            if key == "ids":
                assert type(val) == typing.List
                q = q.filter(UserEntity.id.in_(val))
            elif key == "term_ids":
                # TODO: optimize logics in here
                pass
        count = q.count()
        items = q.offset(offset).limit(limit).all()
        return items, count

    def create(self, **kwargs) -> UserEntity:
        entity = UserEntity(**kwargs)
        session.add(entity)
        session.flush()
        return entity

    def bulk_create(self, entity_list) -> typing.List[UserEntity]:
        entity_list = [UserEntity(**entity) for entity in entity_list]
        session.bulk_save_objects(entity_list, return_defaults=True)
        session.flush()
        return entity_list

    def delete(self, _id):
        session.query(UserEntity).filter(UserEntity.doc_id == _id).update({UserEntity.is_deleted: True})
        session.flush()

    def bulk_delete(self, _id_list):
        session.query(UserEntity).filter(UserEntity.doc_id.in_(_id_list)).update({UserEntity.is_deleted: True})
        session.flush()

    def bulk_delete_by_filter(self, **kwargs):
        raise NotImplemented("no bulk_delete_by_filter")

    def update(self, _id, **kwargs):
        entity = session.query(UserEntity).filter(UserEntity.id == _id)
        entity.update(kwargs)
        session.flush()
        return entity.one()

    def bulk_update(self, entity_list):
        raise NotImplemented("no bulk_update")

