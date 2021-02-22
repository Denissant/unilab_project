from flask_restful import Resource, reqparse
from modules.user import User


class RegisterUser(Resource):
    signup_parser = reqparse.RequestParser()
    signup_parser.add_argument('username',
                               type=str,
                               required=True,
                               help='Username is required and should be string type')
    signup_parser.add_argument('password',
                               type=str,
                               required=True,
                               help='Password is required and should be string type')

    def post(self):
        received_data = RegisterUser.signup_parser.parse_args()
        found = User.find_by_username(received_data['username'])
        if found:
            return f"""Username "{received_data['username']}" is already taken""", 400
        else:
            new_user = User(**received_data)     # id should be fixed, (data['username'], data['password']) LATER
            new_user.add()
            return f'Successfully registered: {received_data}', 201
