import os
from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate

from db import db
from resources.genre import Genres, Genre
from resources.movies import Movies, Movie
from resources.user import Users, User

app = Flask(__name__)

database_name = 'data.db'

app.secret_key='mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(os.path.abspath(__file__)), database_name)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

api = Api(app)

migrate = Migrate(app, db)

@app.before_first_request
def before_first_request():
    db.create_all()

@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Methods'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response


api.add_resource(Genres, '/genres')
api.add_resource(Genre, '/genre/<int:_id>')

api.add_resource(Movies, '/movies')
api.add_resource(Movie, '/movie/<int:_id>')

api.add_resource(Users, '/users')
api.add_resource(User, '/user/<int:_id>')

debug = True
port = 5000
if __name__ == '__main__':
    app.run(debug=debug, port=port)
