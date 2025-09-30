from flask_restx import Namespace, Resource
from flask_restx.reqparse import ParseResult
from modules.extentions import db
from .models import User
from .reqparsers_restx import user_add_parser


name_space: Namespace = Namespace('Users', description='User operations')

@name_space.route('/')
class UserController(Resource):
    @name_space.expect(user_add_parser)
    @name_space.doc(
        description = 'Создание нового пользователя',
        responses = {
            201: "Пользователь создан",
            400: "Неверные данные"
        }
    )
    def post(self):
        """Создание нового пользователя"""
        args: ParseResult = user_add_parser.parse_args()
        
        new_user: User = User(**args)

        db.session.add(new_user)
        db.session.commit()

        return {"id": new_user.id, "name": new_user.name}, 201
