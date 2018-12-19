#user object
import re

class User:
    def __init__(self, *args):
        self.id = id,
        self.firstname = firstname,
        self.lastname = lastname,
        self.othernames = othernames,
        self.email = email,
        self.password = password,
        self.phonenumber = phoneNumber,
        self.username = username,
        self.registered = datetime.now()
        self.isadmin = "False"
        
    
    def check_if_user_email_exist(self):
        email = db.check_email(self.email)
        if email != None:
            return 'Email already has an account.'

    @staticmethod
    def login_validate(email, password):
        if not username or username.isspace():
            return 'Username field can not be left empty.'
        elif not password or password.isspace():
            return 'Password field can not be left empty.'
        else:
            return None