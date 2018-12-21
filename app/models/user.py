# app/models/redflag.py
import os
import uuid
import jwt
from flask_bcrypt import Bcrypt
from datetime import datetime, timedelta


class User:
    user_info = {
        "firstname": "",
        "lastname": "",
        "othernames": "",
        "email": "",
        "password": "",
        "phonenumber": "",
        "username": ""
    }

    def __init__(self, user_info):
            """Initialize an user object"""
            self.id = uuid.uuid4().clock_seq
            self.firstname = user_info["firstname"]
            self.lastname = user_info["lastname"]
            self.othernames = user_info["othernames"]
            self.email = user_info["email"]
            self.password = Bcrypt().generate_password_hash(
                user_info["password"]).decode()
            self.phonenumber = user_info["phonenumber"]
            self.username = user_info["username"]
            self.registered = datetime.now()
            self.isadmin = "False"


    def to_json_object(self):
        return {
            "id":self.id,
            "firstname":self.firstname,
            "lastname":self.lastname,
            "othernames":self.othernames,
            "email":self.email,
            "phonenumber":self.phonenumber,
            "username":self.username,
            "registered":self.registered,
            "isadmin":self.isadmin
        }

    def password_is_valid(self, password):
        return Bcrypt().check_password_hash(self.password, password)

    def generate_token(self, user_id, isadmin):
        try:
            """ set up a payload with an expiration time"""
            payload = {
                'exp': datetime.utcnow() + timedelta(minutes=120),
                'iat': datetime.utcnow(),
                'sub': user_id,
                'adn': isadmin
            }
            """create the byte string token using the payload and the SECRET key"""
            jwt_string = jwt.encode(
					payload,
					str(os.getenv('SECRET')),
					algorithm='HS256'
				)
            return jwt_string

        except Exception as e:
            """return an error in string format if an exception occurs"""
            return str(e)

    @staticmethod
    def password_is_valid(password1, password2):
        """
        Checks the password against it's hash to validates the user's password
        """
        return Bcrypt().check_password_hash(password1, password2)

    @staticmethod
    def decode_admin_status(token):
        """Decodes the email from the Authorization header."""
        payload = jwt.decode(token, str(
            os.getenv('SECRET')), algorithms='HS256')
        return payload['adn']

    @staticmethod
    def decode_token(token):
        """Decodes the access token from the Authorization header."""
        try:
            # try to decode the token using our SECRET variable
            payload = jwt.decode(token, str(
                os.getenv('SECRET')), algorithms='HS256')
            return payload['sub']
        except jwt.ExpiredSignatureError:
            # the token is expired, return an error string
            return "Expired token. Please login to get a new token"
        except jwt.InvalidTokenError:
            # the token is invalid, return an error string
            return "Invalid token. Please register or login"
