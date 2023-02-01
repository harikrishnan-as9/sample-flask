from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
from models.user import UserModel

parser = reqparse.RequestParser()
parser.add_argument('password', type=str, required=True)
parser.add_argument('role', type=str)

_parser = parser.copy()
_parser.add_argument('username', type=str, required=True)

def get_user_response(user):
    access_token = create_access_token(identity=user.username, fresh=True, additional_claims=user.json())
    response = user.json()
    status_code = 200
    headers = {'x-access-token':access_token}
    return (response, status_code, headers)


class Users(Resource):
    def get(self):
        return [user.json() for user in UserModel.find_all()]
    
    def post(self):
        data = _parser.parse_args()
        username = data['username']
        password = data['password']
        role = data['role'].lower() if data['role'] else 'default'

        if UserModel.find_by_username(username):
            return {'msg': f'username "{username}" already taken'}, 400
        
        user = UserModel(username=username, password=password, role=role)
        user.save()
        return get_user_response(user)
    
class User(Resource):
    def put(self, _id):
        user = UserModel.find_by_id(_id)
        if not user:
            return {'msg': f'User with id "{_id}" doesn\'t exist'}, 404
        
        data = _parser.parse_args()
        username = data['username']
        password = data['password']
        role = data['role'].lower() if data['role'] else user.role

        if UserModel.find_by_username(username) and UserModel.find_by_username(username)._id != user._id:
            return {'msg': f'Another user with username "{username}" already exist'}, 400

        user.username = username    
        user.password = password
        user.role = role
        user.save()

        return get_user_response(user)
    
    def delete(self, _id):
        user = UserModel.find_by_id(_id)
        if not user:
            return {'msg': f'User with id "{_id}" doesn\'t exist'}, 404
        
        data = user.json()
        user.delete()
        return {
            'msg': f'user with id "{_id}" has been deleted',
            'data': data
        }

