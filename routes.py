from flask import Blueprint, jsonify, request
from models import Footballer, db, Health

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
    return player.json() if player else 'Player not found'


@api.route('/player/add')
def put_player():
    name = request.args.get('name')
    surname = request.args.get('surname')
    club = request.args.get('club')
    health_id = request.args.get('health_id')
    player = Footballer(name=name, surname=surname, club=club, health_id=health_id)
    db.session.add(player)
    db.session.commit()
    return jsonify(player.json())

@api.route('/healths')
def get_healths():
    return jsonify([(lambda health: health.json())(health) for health in Health.query.all()])

@api.route('/health/<int:id>')
def get_health(id):
    health = Health.query.get(id)
    return health.json() if health else 'Health not found'

@api.route('/health/add')
def put_health():
    name = request.args.get('name')
    health = Health(name=name)
    db.session.add(health)
    db.session.commit()
    return jsonify(health.json())
