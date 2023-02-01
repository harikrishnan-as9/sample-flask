from flask_restful import Resource, reqparse
from models.genre import GenreModel

parser = reqparse.RequestParser()
parser.add_argument('name', required=True,help='Name is mandatory')

class Genres(Resource):

    def get(self):
        return [genre.json() for genre in GenreModel.find_all()]        

    def post(self):
        data = parser.parse_args()
        name = data['name'].capitalize()
        if GenreModel.find_by_name(name=name):
            return {
                'msg': f'{name} already taken'
            }, 400
        genre = GenreModel(name=name)
        genre.save()
        return genre.json()
    
class Genre(Resource):

    def put(self, _id):
        genre = GenreModel.find_by_id(_id)
        if genre is None:
            return {
                'msg': f'Item with id {_id} is not available'
            }, 404
        
        data = parser.parse_args()
        name = data['name'].capitalize()
        genre.name = name
        genre.save()
        return genre.json()
    
    def delete(self, _id):
        genre = GenreModel.find_by_id(_id)
        if genre is None:
            return {
                'msg': f'Item with id {_id} is not available'
            }, 404
        
        genre.delete()
        return {
            'msg': f'Item with id {_id} is deleted',
            'item': genre.json()
        }

