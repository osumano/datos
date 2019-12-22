import os

postgres_db_env = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = postgres_db_env
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfigDocker(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = postgres_db_env
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = postgres_db_env
