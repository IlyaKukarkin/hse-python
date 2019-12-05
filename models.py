from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Footballer(db.Model):
    __tablename__ = 'Footballers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    surname = db.Column(db.String(120))
    club = db.Column(db.String(120))

    def json(self):
        return {"id": self.id, "name": self.name, "surname": self.surname, "club": self.club}
