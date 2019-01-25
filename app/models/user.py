import os
import jwt
from flask_bcrypt import Bcrypt
from datetime import datetime, timedelta


class User:
    def __init__(self, *args):
        user_info = args[0]
        self.firstname = user_info[0]
        self.lastname = user_info[1]
        self.othernames = user_info[2]
        self.email = user_info[3]
        self.password = Bcrypt().generate_password_hash(user_info[4]).decode()
        self.phonenumber = user_info[5]
        self.username = user_info[6]
        self.registered = datetime.now()
        self.isadmin = user_info[7]

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

    