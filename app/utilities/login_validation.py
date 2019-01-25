

init_dict = {
    "email": "",
    "password": ""
}


class Login_Validation():
    def __init__(self, init_dict):
        self.email = init_dict["email"]
        self.password = init_dict["password"]

    def check_inputs(self):
        if not isinstance(self.email, str):
            return [406, "Type str required for email."]
        elif self.email.isspace() or not self.email:
            return [406, "Provide an Email"]
        elif self.password.isspace() or not self.password or not isinstance(self.password, str):
            return [406, "Provide a Password"]
        return [200, "All good"]
