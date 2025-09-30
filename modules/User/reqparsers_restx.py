from flask_restx import reqparse

user_add_parser: reqparse.RequestParser = reqparse.RequestParser()
user_add_parser.add_argument('name', type=str, required=True, help='Имя пользователя', location='form')