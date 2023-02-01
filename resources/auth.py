from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, get_jti
from models.user import UserModel
from services.auth import set_user_token

_parser = reqparse.RequestParser()
_parser.add_argument('username', type=str, required=True)
_parser.add_argument('password', type=str, required=True)

class Login(Resource):
    def post(self):
        data = _parser.parse_args()
        username = data['username']
        password = data['password']
        user = UserModel.find_by_username(username)
        
        if not user:
            return {'msg': 'Invalid username'}, 404
        if user and user.password != password:
            return {'msg': 'Password incorrect'} , 400
        
        if user and user.password == password:
            access_token = create_access_token(identity=username, fresh=True, additional_claims=user.json())
            set_user_token(username=username, jti=get_jti(access_token))
            return {
                'access_toke': access_token
            }
