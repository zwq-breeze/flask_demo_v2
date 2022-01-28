# -*- coding:utf-8 -*-
# -*- zanyunfei@datagrand.com -*-
# -*- 2020/4/29 -*-
from app.common.extension import db
from app.entity.base import BaseEntity


class UserEntity(BaseEntity):
    __tablename__ = 'user'
    name = db.Column(db.String(255), nullable=False)
    pw = db.Column(db.String(255), nullable=False)
