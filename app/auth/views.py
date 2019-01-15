# /app/auth/views.py
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from . import auth_blueprint
from flask.views import MethodView
from flask import make_response, request, jsonify, abort, json
from app.models.user import User
from app.data_store.data import users
from app.utilities.helper_functions import Helper_Functions
from app.utilities.login_validation import Login_Validation
from app.utilities.register_validation import Register_Validation

class RegistrationView(MethodView):
    """This class registers a new user."""
    def post(self):

        input_data = json.loads(request.data)

        firstname = input_data['firstname']
        lastname = input_data['lastname']
        othernames = input_data['othernames']
        email = input_data['email']
        password = input_data['password']
        phonenumber = input_data['phonenumber']
        username = input_data['username']

        validate_input = Register_Validation(
            {"firstname": firstname, "lastname": lastname, "othernames": othernames, "email": email, "password": password, "phonenumber": phonenumber, "username": username})
        validated_input = validate_input.check_input()
        if validated_input[0] == 200:
            if Helper_Functions.email_exists_already(email) is True:
                return Helper_Functions.the_return_method(400, "That Email already is registered. Login or use a different Email to register.")
            else:
                new_user_info_list = [ firstname, lastname, othernames, email, password, phonenumber, username]
                new_user = User(new_user_info_list)
                
                users.append(new_user)
                return make_response(jsonify({"status":201, "data":[{"id":(new_user.to_json_object())["id"]}]})), 201
        else:
            return Helper_Functions.the_return_method(validated_input[0], validated_input[1])


class LoginView(MethodView):
    """This class-based view handles user login and access token generation."""

    def post(self):
        """Handle POST request for this view. Url ---> /v1/auth/login"""
        password = json.loads(request.data)['password']
        email = json.loads(request.data)['email']

        validate_input = Login_Validation({"email":email, "password":password})
        validated_input = validate_input.check_inputs()
        if validated_input[0] == 200:
            try:
                user = Helper_Functions.get_user(email)
                if user:
                        if User.password_is_valid(user.password, password):
            
                            access_token = user.generate_token(user.id, user.isadmin)
                            if access_token:
                                    response = {
                                        'status':200,
                                        'data': [{'access_token':  access_token.decode()}]
                                    }
                                    return make_response(jsonify(response)), 200
                        else:
                            return Helper_Functions.the_return_method(401, "Enter a correct Password")
                else:
                    return Helper_Functions.the_return_method(401, "Email not registered on any account.")
            except Exception as e:
                response = {
                    'message': str(e)
                }
                return make_response(jsonify(response)), 500

        else:
            return Helper_Functions.the_return_method(validated_input[0], validated_input[1])


registration_view = RegistrationView.as_view('registration_view')
login_view = LoginView.as_view('login_view')

auth_blueprint.add_url_rule(
    '/api/v1/auth/register',
    view_func=registration_view,
    methods=['POST'])

auth_blueprint.add_url_rule(
    '/api/v1/auth/login',
    view_func=login_view,
    methods=['POST']
)
