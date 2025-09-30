import os


class BaseConfg:
    pass


class DevelopConfig(BaseConfg):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URL")


class ProductionConfig(BaseConfg):
    DEBUG = False
