from flask import Blueprint, jsonify, request
from models import Footballer, db, Club

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
                    <a href="./api/clubs">Clubs</a>
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
    club_id = request.args.get('club_id')
    club = Club.query.get(club_id)
    if club is None:
        return 'Error: club with that ID doesn`t exist'
    else:
        player = Footballer(name=name, surname=surname, club_id=club_id)
        db.session.add(player)
        db.session.commit()
        return jsonify(player.json())


@api.route('/player/<int:id>/edit')
def edit_player(id):
    player = Footballer.query.get(id)
    if player:
        name = request.args.get('name')
        surname = request.args.get('surname')
        club_id = request.args.get('club_id')
        if club_id is not None:
            club = Club.query.get(club_id)
            if club is None:
                return 'Error: club with that ID doesn`t exist'
            else:
                player.club_id = club.id
        if name is not None:
            player.name = name
        if surname is not None:
            player.surname = surname
        db.session.commit()
        return jsonify(player.json())
    else:
        return 'Player not found'


@api.route('/clubs')
def get_clubs():
    return jsonify([(lambda club: club.json())(club) for club in Club.query.all()])


@api.route('/club/<int:id>')
def get_club(id):
    club = Club.query.get(id)
    return club.json() if club else 'Club not found'


@api.route('/club/add')
def put_club():
    name = request.args.get('name')
    club = Club(name=name)
    db.session.add(club)
    db.session.commit()
    return jsonify(club.json())


@api.route('/club/<int:id>/edit')
def edit_club(id):
    club = Club.query.get(id)
    if club:
        name = request.args.get('name')
        if name:
            club.name = name
        db.session.commit()
        return jsonify(club.json())
    else:
        return 'Club not found'
