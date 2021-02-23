from db import db


class ItemModel(db.Model):
    __tablename__ = 'responses'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    sex = db.Column(db.String(6), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    last_company = db.Column(db.String(100), nullable=False)
    last_position = db.Column(db.String(50), nullable=False)
    relevant_experience = db.Column(db.Integer, nullable=False)
    school_diploma = db.Column(db.Boolean, nullable=False)
    bachelors_degree = db.Column(db.Boolean, nullable=False)
    bachelors_uni_faculty = db.Column(db.String, nullable=False)
    driving_license = db.Column(db.Boolean, nullable=False)
    skills_and_qualities = db.Column(db.String, nullable=False)
    english_level = db.Column(db.Integer, nullable=False)
    satisfied = db.Column(db.Boolean, nullable=True)
    rating = db.Column(db.Integer, nullable=True)

    def __init__(self, name, sex, age, last_company, last_position, relevant_experience, school_diploma, bachelors_degree, bachelors_uni_faculty, driving_license, skills_and_qualities, english_level, satisfied, rating):
        self.name = name
        self.sex = sex
        self.age = age
        self.last_company = last_company
        self.last_position = last_position
        self.relevant_experience = relevant_experience
        self.school_diploma = school_diploma
        self.bachelors_degree = bachelors_degree
        self.bachelors_uni_faculty = bachelors_uni_faculty
        self.driving_license = driving_license
        self.skills_and_qualities = skills_and_qualities
        self.english_level = english_level
        self.satisfied = satisfied
        self.rating = rating

    def json(self):
        return {"name": self.name, "sex": self.sex, "age": self.age, "last_company": self.last_company, "last_position": self.last_position, "relevant_experience": self.relevant_experience, "school_diploma": self.school_diploma, "bachelors_degree": self.bachelors_degree, "bachelors_uni_faculty": self.bachelors_uni_faculty, "driving_license": self.driving_license, "skills_and_qualities": self.skills_and_qualities, "english_level": self.english_level, "satisfied": self.satisfied, "rating": self.rating}

    @classmethod
    def cv_list(cls):
        return {"all received CVs:": list(map(lambda cv: cv.json(), cls.query.all()))}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def del_from_db(self):
        db.session.delete(self)
        db.session.commit()
