from flask import Blueprint, jsonify, request
from models import Footballer, db

index = Blueprint('index', __name__, url_prefix='/')
api = Blueprint('api', __name__, url_prefix='/api')

@index.route('/')
@index.route('/index')
def get_index():
    return '''
            <html>
                <title>
                    Players Database
                </title>
                <body>
                    <h1>Api</h1>
                    <a href="./api/players">Players</a>
                </body>
            </html>
    
    '''

@api.route('/players')
def get_players():
    return jsonify([(lambda player: player.json())(player) for player in Footballer.query.all()])


@api.route('/player/<int:id>')
def get_player(id):
    player = Footballer.query.get(id)
    return player.json() if player else 'Not found'


@api.route('/player/add')
def put_player():
    name = request.args.get('name')
    surname = request.args.get('surname')
    club = request.args.get('club')
    player = Footballer(name=name, surname=surname, club=club)
    db.session.add(player)
    db.session.commit()
    return jsonify(player.json())
