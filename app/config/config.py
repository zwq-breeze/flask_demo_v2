import os
from pathlib import Path
from flask import Config, current_app

BASE_PATH: str = os.getcwd()
ROOT_PATH: Path = Path(__file__).parents[1]  # is same as 'BASE_PATH', but more conveniently to be used


def get_config_from_app(*args, **kwargs):
    return current_app.config.get(*args, **kwargs)


class BasicConfig(Config):
    SECRET_KEY = 'datagrand-voc-admin-api'


class SqlalchemyConfigMixin:
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:53306/szse"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(
        os.getenv('MYSQL_USER', 'root'),
        os.getenv('MYSQL_PASSWORD', 'zyf123456'),
        os.getenv('MYSQL_HOST', '127.0.0.1'),
        os.getenv('MYSQL_PORT', 3306),
        os.getenv('MYSQL_DATABASE', 'dbtest'),
        os.getenv('MYSQL_CHARSET', 'utf8mb4')
    )
    # 调试SQL语句时使用，慎开
    # SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_POOL_RECYCLE = 280


# Redis实例的生成不应该依赖于Flask实例，所以生成redis的实例直接引用的此配置
class RedisConfigMixin:
    REDIS_HOST = os.getenv('REDIS_HOST', '127.0.0.1')
    REDIS_PORT = os.getenv('REDIS_PORT', 6379)
    REDIS_DATABASE = os.getenv('REDIS_DATABASE', 0)


class AsyncQueueConfigMixin:
    EXTRACT_TRAIN_QUEUE_KEY = 'queue:a'
    EXTRACT_TASK_QUEUE_KEY = 'task:contract:queue'
    EXTRACT_EVALUATE_QUEUE_KEY = 'model:evaluate:queue'
    RELATION_TRAIN_QUEUE_KEY = 'queue:a'
    RELATION_TASK_QUEUE_KEY = 'task:contract:queue'
    RELATION_EVALUATE_QUEUE_KEY = 'model:evaluate:queue'
    WORDSEG_TRAIN_QUEUE_KEY = 'queue:a'
    WORDSEG_TASK_QUEUE_KEY = 'task:contract:queue'
    WORDSEG_EVALUATE_QUEUE_KEY = 'model:evaluate:queue'
    CLASSIFY_MODEL_QUEUE_KEY = 'queue:classify:a'
    # 新词发现队列
    NEW_WORD_TASK_QUEUE_KEY = 'task:newword_queue'
    TEXT_CLUSTERING_TASK_QUEUE_KEY = 'task:clustering:queue'
    # 字词向量队列
    WORD_EMBEDDING_TASK_QUEUE = 'task:embedding:queue'
    # 训练数据导出队列
    DATA_EXPORT_QUEUE_KEY = 'queue:data_export:a'




class DevelopmentConfig(
    BasicConfig,
    SqlalchemyConfigMixin,
    RedisConfigMixin,
    AsyncQueueConfigMixin,
):
    ENV = "development"
    DEBUG = True
    TESTING = True
    PROPAGATE_EXCEPTIONS = True
    AUTHMGR_FORWARD_INIT_URL = 'http://{}:{}/forward/forward_init/'.format(
        os.getenv('AUTHMGR_HOST', 'authmgr'),
        os.getenv('AUTHMGR_PORT', 10001)
    )


class TestingConfig(BasicConfig):
    ENV = "testing"
    DEBUG = False
    TESTING = True
    PROPAGATE_EXCEPTIONS = True


class ProductionConfig(BasicConfig):
    # TODO 正确配置生产环境配置
    ENV = "production"
    DEBUG = False
    TESTING = False
    PROPAGATE_EXCEPTIONS = True


Configs = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
