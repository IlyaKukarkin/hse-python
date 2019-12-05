from flask import Flask

from models import db, Footballer, Health
from routes import api, index

app = Flask(__name__)
app.register_blueprint(api)
app.register_blueprint(index)
db.init_app(app)

with app.app_context():
    db.create_all()
    health = Health(name='well')
    injury = Health(name='injured')
    db.session.add(health)
    db.session.add(injury)
    db.session.commit()
    db.session.add(Footballer(name='Lionel', surname='Messi', club='Barcelona', health_id=injury.id))
    db.session.add(Footballer(name='Cristiano', surname='Ronaldo', club='Juventus', health_id=health.id))
    db.session.commit()

if __name__ == '__main__':
    app.run()
