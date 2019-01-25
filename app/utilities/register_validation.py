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
        elif (not isinstance(self.firstname, str) or not isinstance(self.lastname, str) or not isinstance(self.othernames, str) or not isinstance(self.email, str) or not isinstance(self.password, str) or not isinstance(self.phonenumber, str) or not isinstance(self.username, str)):
            return [406, "Make sure to strings use only "]
        elif not self.phonenumber.isdigit():
            return [406, "Make use phone number is digits only."]
        elif self.password.isspace() or len(self.password) < 4:
            return [406, "Make sure your password has atlest 4 letters"]
        elif re.search('[0-9]', self.password) is None:
            return [406, "Make sure your password has a number in it"]
        elif re.search('[A-Z]', self.password) is None:
            return [406, "Make sure your password has a capital letter in it"]
        elif not re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", self.email) is not None:
            return [406, "Please enter a valid Email."]
        elif  (not self.firstname.isalnum() or not self.lastname.isalnum() or not self.othernames.isalnum() and self.username.isalnum() or self.email.isspace() or self.phonenumber.isspace()):
            return [406, "Make sure to use the English alphabert in the fields"]
        return [200, "All Good"]
