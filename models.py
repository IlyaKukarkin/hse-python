from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Footballer(db.Model):
    __tablename__ = 'Footballers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    surname = db.Column(db.String(120))
    club_id = db.Column(db.Integer, ForeignKey('Club.id'))
    club = relationship('Club')

    def json(self):
        return {"id": self.id, "name": self.name, "surname": self.surname, "club": self.club.json()}


class Club(db.Model):
    __tablename__ = 'Club'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    def json(self):
        return {"id": self.id, "name": self.name}

    def jsonName(self):
        return self.name
