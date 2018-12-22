import re


init_dict = {
        "firstname": "",
        "lastname": "",
        "othernames": "",
        "email": "",
        "password": "",
        "phonenumber": "",
        "username": ""
    }
    

class Register_Validation():

    def __init__(self, init_dict):
        self.firstname = init_dict["firstname"]
        self.lastname = init_dict["lastname"]
        self.othernames = init_dict["othernames"]
        self.email = init_dict["email"]
        self.password = init_dict["password"]
        self.phonenumber = init_dict["phonenumber"]
        self.username = init_dict["username"]

    def check_input(self):
        if not (self.firstname and self.lastname and self.email and self.password and self.phonenumber and self.username):
            return [400, "Make sure you fill all the required fields"]
        elif (type(self.firstname) is not str or type(self.lastname) is not str or type(self.othernames) is not str or type(self.email) is not str or type(self.password) is not str or type(self.phonenumber) is not str or type(self.username) is not str):
            return [400, "Make sure to strings use only "]
        elif self.firstname.isspace() or self.lastname.isspace() or self.othernames.isspace() or self.email.isspace() or self.password.isspace() or self.phonenumber.isspace() or self.username.isspace():
            return [400, "Make sure to have no empty spaces in fields"]

        elif not re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", self.email) is not None:
            return [401, "Please enter a valid Email."]
        elif len(self.password) < 4:
            return [401, "Make sure your password is at lest 4 letters"]
        elif re.search('[0-9]', self.password) is None:
            return [401, "Make sure your password has a number in it"]
        elif re.search('[A-Z]', self.password) is None:
            return [401, "Make sure your password has a capital letter in it"]
        return [200, "All Good"]
