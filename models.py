from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()




class Footballer(db.Model):
    __tablename__ = 'Footballers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    surname = db.Column(db.String(120))
    club = db.Column(db.String(120))
    health_id = db.Column(db.Integer, ForeignKey('Health.id'))
    health = relationship('Health')

    def json(self):
        return {"id": self.id, "name": self.name, "surname": self.surname, "club": self.club, "health": self.health.json()}


class Health(db.Model):
    __tablename__ = 'Health'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    def json(self):
        return {"id": self.id, "name": self.name}
