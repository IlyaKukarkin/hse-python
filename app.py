from flask import Flask

from models import db, Men
from routes import api

app = Flask(__name__)
app.register_blueprint(api)
db.init_app(app)

with app.app_context():
    db.create_all()
    db.session.add(Men(name='Ivan'))
    db.session.add(Men(name='Ivan The Second'))
    db.session.commit()

if __name__ == '__main__':
    app.run()
