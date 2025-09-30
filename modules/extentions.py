from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api


db: SQLAlchemy = SQLAlchemy()
api: Api = Api(
    title = 'Habbit Tracker API',
    version = '1.0',
    description = 'API для Habbit Tracker',
    doc = '/docs'
)