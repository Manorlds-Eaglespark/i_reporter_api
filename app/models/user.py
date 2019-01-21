import os
import uuid
import jwt
from flask_bcrypt import Bcrypt
from datetime import datetime, timedelta


class User:
    def __init__(self, *args):
        user_info = args[0]
        self.id = uuid.uuid4().clock_seq
        self.firstname = user_info[0]
        self.lastname = user_info[1]
        self.othernames = user_info[2]
        self.email = user_info[3]
        self.password = Bcrypt().generate_password_hash(user_info[4]).decode()
        self.phonenumber = user_info[5]
        self.username = user_info[6]
        self.registered = datetime.now()
        self.isadmin = args[0][7]

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
