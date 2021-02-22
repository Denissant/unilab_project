from db import db


class ItemModel(db.Model):
    __tablename__ = 'information'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nickname = db.Column(db.String(20), unique=True, nullable=False)
    hourly_wage = db.Column(db.Float(precision=2))
    type = db.Column(db.String(50))
    experience = db.Column(db.String(25))

    def __init__(self, _id, nickname, hourly_wage, type, experience):
        self.id = _id
        self.nickname = nickname
        self.hourly_wage = hourly_wage
        self.type = type
        self.experience = experience

    @classmethod
    def find_by_name(cls, nickname):
        return cls.query.filter_by(nickname=nickname).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def del_from_db(self):
        db.session.delete(self)
        db.session.commit()
