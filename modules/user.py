from db import db

class User(db.Model):
    __tablename__ = 'usersdatabase'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(16), unique=True, nullable=False)

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    def __repr__(self):
        return f"User ID: {self.id}. Username: {self.username}. Password: {self.password}"

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_userid(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def add(self):
        db.session.add(self)
        db.session.commit()
