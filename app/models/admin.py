# app/models/Admin.py
from app.models.user import User

class Admin(User):

    def __init__(self, *args):
        User.__init__(self, *args)
        self.isadmin = "True"
