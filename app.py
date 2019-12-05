from flask import Flask

from models import db, Footballer, Club
from routes import api, index

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.register_blueprint(api)
app.register_blueprint(index)
db.init_app(app)

with app.app_context():
    db.create_all()
    barcelona = Club(name='Barcelona')
    juventus = Club(name='Juventus')
    db.session.add(barcelona)
    db.session.add(juventus)
    db.session.commit()
    db.session.add(Footballer(name='Lionel', surname='Messi', club_id=barcelona.id))
    db.session.add(Footballer(name='Cristiano', surname='Ronaldo', club_id=juventus.id))
    db.session.commit()

if __name__ == '__main__':
    app.run()
