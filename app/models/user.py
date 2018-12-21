#user object
import re
import uuid
from flask_bcrypt import Bcrypt
from datetime import datetime, timedelta


firstname = ""
lastname = ""
othernames = ""
email = ""
password = "_"
phonenumber = ""
username = ""


class User:
    def __init__(self, *args):
        self.id = uuid.uuid1(),
        self.firstname = firstname,
        self.lastname = lastname,
        self.othernames = othernames,
        self.email = email,
        self.password = Bcrypt().generate_password_hash(password).decode()
        self.phonenumber = phonenumber,
        self.username = username,
        self.registered = datetime.now()
        self.isadmin = "False"

    def check_if_user_email_exist(self):
        pass

    @staticmethod
    def login_validate(email, password):
        if not username or username.isspace():
            return 'Username field can not be left empty.'
        elif not password or password.isspace():
            return 'Password field can not be left empty.'
        else:
            return None

    def password_is_valid(self, password):
        return Bcrypt().check_password_hash(self.password, password)

    def generate_token(self, user_id, email, is_admin):
        try:
            """ set up a payload with an expiration time"""
            payload = {
                'exp': datetime.utcnow() + timedelta(minutes=120),
                'iat': datetime.utcnow(),
                'sub': user_id,
                'eml': email,
                'adn': is_admin
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
        payload = jwt.decode(token, str(os.getenv('SECRET')), algorithms='HS256')
        return payload['adn']

    @staticmethod
    def decode_email(token):
        """Decodes the email from the Authorization header."""
        payload = jwt.decode(token, str(os.getenv('SECRET')), algorithms='HS256')
        return payload['eml']

    @staticmethod
    def decode_token(token):
        """Decodes the access token from the Authorization header."""
        try:
            # try to decode the token using our SECRET variable
            payload = jwt.decode(token, str(os.getenv('SECRET')), algorithms='HS256')
            return payload['sub']
        except jwt.ExpiredSignatureError:
            # the token is expired, return an error string
            return "Expired token. Please login to get a new token"
        except jwt.InvalidTokenError:
            # the token is invalid, return an error string
            return "Invalid token. Please register or login"
