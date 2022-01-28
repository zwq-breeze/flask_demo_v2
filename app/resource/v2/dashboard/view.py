# coding=utf-8
# @Author: Jiasheng Gu
# @Date: 2020/3/18
from flask import g
from flask_restful import Resource
from app.model import UserModel
from app.common.filters import CurrentUserMixin
from app.service.user_service import UserService
from app.common.common import NlpTaskEnum
from flask import jsonify


class DemoResource(Resource):
    def get(self):
        # return jsonify("hello taylor")
        return UserService().get_by_id(1)

class DashboardResource(Resource, CurrentUserMixin):
    def get(self):
        """
        获取分类、抽取、分词和实体关系的项目数量、标注任务数、模型数、已标注任务数、已审核任务数
        :return:
        """
        result_skeleton = [
            {"type": "分类项目", "nlp_task_id": int(NlpTaskEnum.classify)},
            {"type": "抽取项目", "nlp_task_id": int(NlpTaskEnum.extract)},
            {"type": "实体关系", "nlp_task_id": int(NlpTaskEnum.relation)},
            {"type": "分词项目", "nlp_task_id": int(NlpTaskEnum.wordseg)},
        ]
        """
        管理员、超级管理员和游客角色可以看到模型、标注信息
        非管理员角色不能看到模型信息，只能看到标注相关信息
        """
        result_skeleton = UserService().get_dashboard_stats(result_skeleton, self.get_current_user())

        return result_skeleton
