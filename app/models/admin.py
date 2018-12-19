# app/models/Admin.py
from app.models.user import User

class Admin(User):

    def __init__(self, *args):
        super().__init__(*args)
        self.isadmin = "True"
