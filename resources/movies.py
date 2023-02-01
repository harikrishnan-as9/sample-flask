from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt
from models.movies import MoviesModel
from models.genre import GenreModel
from config import config

jwt_optional = not config['jwt_required']

parser = reqparse.RequestParser()
parser.add_argument('title',type=str, required=True)
parser.add_argument('numberInStock',type=int, required=True)
parser.add_argument('dailyRentalRate',type=float, required=True)
parser.add_argument('genreId',type=int, required=True)
parser.add_argument('liked',type=bool)


class Movies(Resource):
    def get(self):
        return [movie.json() for movie in MoviesModel.find_all()]
    
    @jwt_required(optional=jwt_optional)
    def post(self):
        data = parser.parse_args()
        title = data['title']
        genre_id = data['genreId']
        numberInStock = data['numberInStock']
        dailyRentalRate = data['dailyRentalRate']
        liked = data['liked'] if data['liked'] != None else False

        if MoviesModel.find_by_title(title=title):
            return {'msg': f'another movie with name "{title}" already present in database'}, 400
        if not GenreModel.find_by_id(genre_id):
            return {'msg': f'genre with id: {genre_id} is not present in database'}, 404

        movie = MoviesModel(title=title, numberInStock=numberInStock, dailyRentalRate=dailyRentalRate,genre_id=genre_id, liked=liked)
        try:
            movie.save()
        except:
            return {'msg': 'something went wrong while saving the data to database'}, 500
        return movie.json()


class Movie(Resource):
    def get(self, _id):
        movie = MoviesModel.find_by_id(_id)
        if not movie:
            return {'msg': f'movie with id: {_id} is not present in database'}, 404

        return movie.json()

    @jwt_required(optional=jwt_optional)
    def put(self, _id):
        movie = MoviesModel.find_by_id(_id)
        if not movie:
            return {'msg': f'movie with id: {_id} is not present in database'}, 404
        
        data = parser.parse_args()
        title = data['title']
        genre_id = data['genreId']
        numberInStock = data['numberInStock']
        dailyRentalRate = data['dailyRentalRate']
        liked = data['liked']

        if MoviesModel.find_by_title(title=title) and MoviesModel.find_by_title(title=title)._id != movie._id    :
            return {'msg': f'another movie with name "{title}" already present in database'}, 400
        if not GenreModel.find_by_id(genre_id):
            return {'msg': f'genre with id: {genre_id} is not present in database'}, 404

        movie.title = title
        movie.genre_id = genre_id
        movie.numberInStock = numberInStock
        movie.dailyRentalRate = dailyRentalRate
        movie.liked = liked if liked != None else movie.liked
        movie.save()
        return movie.json()
    
    @jwt_required(optional=jwt_optional)
    def delete(self, _id):
        is_admin = get_jwt()['isAdmin']
        if(not is_admin):
            return {'msg': 'Not authorized, only admin can delte movie'}, 401

        movie = MoviesModel.find_by_id(_id)
        if not movie:
            return {'msg': f'movie with id: {_id} is not present in database'}, 404
        
        data = movie.json()
        movie.delete()
        return {'msg': f'movie with {movie.title} has been deleted', 'data':data}
