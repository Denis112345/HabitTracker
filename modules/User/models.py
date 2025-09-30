from modules.extentions import db


class User(db.Model):
    __tablename__: str = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self) -> str:
        return f"<User {self.name}>"
