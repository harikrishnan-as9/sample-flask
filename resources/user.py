from flask_restful import Resource, reqparse
from models.user import UserModel

parser = reqparse.RequestParser()
parser.add_argument('password', type=str, required=True)
parser.add_argument('role', type=str)

_parser = parser.copy()
_parser.add_argument('username', type=str, required=True)

class Users(Resource):
    def get(self):
        return [user.json() for user in UserModel.find_all()]
    
    def post(self):
        data = _parser.parse_args()
        username = data['username']
        password = data['password']
        role = data['role'].lower() if data['role'] else 'default'

        if UserModel.find_by_username(username):
            return {'message': f'username "{username}" already taken'}, 404
        
        user = UserModel(username=username, password=password, role=role)
        user.save()
        return user.json()
    
class User(Resource):
    def put(self, _id):
        user = UserModel.find_by_id(_id)
        if not user:
            return {'message': f'User with id "{_id}" doesn\'t exist'}, 404
        
        data = _parser.parse_args()
        username = data['username']
        password = data['password']
        role = data['role'].lower() if data['role'] else user.role

        if UserModel.find_by_username(username) and UserModel.find_by_username(username)._id != user._id:
            return {'message': f'Another user with username "{username}" already exist'}, 400

        user.username = username    
        user.password = password
        user.role = role
        user.save()

        return user.json()
    
    def delete(self, _id):
        user = UserModel.find_by_id(_id)
        if not user:
            return {'message': f'User with id "{_id}" doesn\'t exist'}, 404
        
        data = user.json()
        user.delete()
        return {
            'message': f'user with id "{_id}" has been deleted',
            'data': data
        }

