# app/models/Admin.py
from app.models.user import User

class Admin(User):

	def __init__(self, *args):
		super().__init__(*args)
        self.id = id,
        self.firstname = firstname,
        self.lastname = lastname,
        self.othernames = othernames,
        self.email = email,
        self.password = password,
        self.phonenumber = phoneNumber,
        self.username = username,
        self.registered = registered
        self.isadmin = "True"
