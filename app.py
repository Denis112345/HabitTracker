from flask import Flask
from modules.extentions import db, api
from modules.User.routes import name_space as user_namespace

def create_app() -> Flask:
    app: Flask = Flask(__name__)
    # app.config.from_object('config.DevelopConfig')

    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://admin:admin@localhost:5432/habit"

    db.init_app(app)
    api.init_app(app)

    api.add_namespace(user_namespace, path='/users')

    return app

if __name__ == '__main__':
    app: Flask = create_app()

    with app.app_context():
        db.create_all()

    app.run(host='0.0.0.0', port=5201, debug=True)
