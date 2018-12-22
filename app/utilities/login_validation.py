

init_dict = {
    "email": "",
    "password": ""
}


class Login_Validation():
    def __init__(self, init_dict):
        self.email = init_dict["email"]
        self.password = init_dict["password"]

    def check_inputs(self):
        if type(self.email) is not str:
            return [400, "Type str required for email."]
        elif self.email.isspace() or not self.email:
            return [400, "Provide an Email"]
        elif self.password.isspace() or not self.password or type(self.password) is not str:
            return [400, "Provide a Password"]
        return [200, "All good"]

