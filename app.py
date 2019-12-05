from flask import Flask

from models import db, Footballer
from routes import api

app = Flask(__name__)
app.register_blueprint(api)
db.init_app(app)

with app.app_context():
    db.create_all()
    db.session.add(Footballer(name='Lionel', surname='Messi', club='Barcelona'))
    db.session.add(Footballer(name='Cristiano', surname='Ronaldo', club='Juventus'))
    db.session.commit()

if __name__ == '__main__':
    app.run()
