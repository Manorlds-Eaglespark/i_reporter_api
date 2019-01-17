import os
import uuid
import jwt
from flask_bcrypt import Bcrypt
from datetime import datetime, timedelta


class User:
    def __init__(self, *args):
        self.id = uuid.uuid4().clock_seq
        self.firstname = args[0][0]
        self.lastname = args[0][1]
        self.othernames = args[0][2]
        self.email = args[0][3]
        self.password = Bcrypt().generate_password_hash(args[0][4]).decode()
        self.phonenumber = args[0][5]
        self.username = args[0][6]
        self.registered = datetime.now()
        self.isadmin = "False"

    def to_json_object(self):
        return self.__dict__

    def password_is_valid(self, password):
        return Bcrypt().check_password_hash(self.password, password)

    def generate_token(self, user_id, isadmin):
        try:
            payload = {
                'exp': datetime.utcnow() + timedelta(minutes=120),
                'iat': datetime.utcnow(),
                'sub': user_id,
                'adn': isadmin
            }
            jwt_string = jwt.encode(
                payload,
                str(os.getenv('SECRET')),
                algorithm='HS256'
            )
            return jwt_string

        except Exception as e:
            return str(e)

    @staticmethod
    def password_is_valid(password1, password2):
        return Bcrypt().check_password_hash(password1, password2)

    @staticmethod
    def decode_admin_status(token):
        payload = jwt.decode(token, str(
            os.getenv('SECRET')), algorithms='HS256')
        return payload['adn']

    @staticmethod
    def decode_token(token):
        try:
            payload = jwt.decode(
                token, str(
                    os.getenv('SECRET')), algorithms='HS256')
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return "Expired token. Please login to get a new token"
        except jwt.InvalidTokenError:
            return "Invalid token. Please register or login"
        return None
