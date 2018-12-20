#user object
import re
import uuid
from datetime import datetime, timedelta


firstname = ""
lastname = ""
othernames = ""
email = ""
password = ""
phonenumber = ""
username = ""

class User:
    def __init__(self, *args):
        self.id = uuid.uuid1(),
        self.firstname = firstname,
        self.lastname = lastname,
        self.othernames = othernames,
        self.email = email,
        self.password = password,
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
