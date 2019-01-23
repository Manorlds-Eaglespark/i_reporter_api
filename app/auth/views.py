# /app/auth/views.py
from app.utilities.register_validation import Register_Validation
from app.utilities.login_validation import Login_Validation
from app.utilities.helper_functions import Helper_Functions
from app.databases.database import Database
from app.data_store.data import users
from app.models.user import User
from app.mail import Mail
from flask import make_response, request, jsonify, abort, json
from flask.views import MethodView
from . import auth_blueprint
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")


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
        database = Database()
        

        if validated_input[0] == 200:
            if database.get_user_by_email(email):
                return Helper_Functions.the_return_method(
                    400, "That Email already is registered. Login or use a different Email to register.")
            else:
                new_user_info_list = [
                    firstname,
                    lastname,
                    othernames,
                    email,
                    password,
                    phonenumber,
                    username,
                    "False"]
                new_user = User(new_user_info_list)
                
                user_id = database.save_user(new_user)
                saved_user = database.get_user_by_email(email)
                return make_response(jsonify(
                    {"status": 201, "data": [{"id": user_id}]})), 201
        else:
            return Helper_Functions.the_return_method(
                validated_input[0], validated_input[1])


class LoginView(MethodView):
    """This class-based view handles user login and access token generation."""

    def post(self):

        input_data = json.loads(request.data)

        password = input_data['password']
        email = input_data['email']

        validate_input = Login_Validation(
            {"email": email, "password": password})

        validated_input = validate_input.check_inputs()

        database = Database()
        
        if validated_input[0] == 200:
            try:
                user_data = database.get_user_by_email(email)
                
                if user_data:
                    user_info = list(user_data)
                    user = User(user_info[1:])
                    user.password = user_info[5]
                    user_id = user_info[0]
                    if user.password_is_valid(password):

                        access_token = user.generate_token(
                            user_id, user.isadmin)
                        if access_token:
                            response = {
                                'status': 200,
                                'data': [{'access_token': access_token.decode()}]
                            }
                            return make_response(jsonify(response)), 200
                    else:
                        return Helper_Functions.the_return_method(
                            401, "Enter a correct Password")
                else:
                    return Helper_Functions.the_return_method(
                        401, "Email not registered on any account.")
            except Exception as e:
                response = {
                    'message': str(e)
                }
                return make_response(jsonify(response)), 500

        else:
            return Helper_Functions.the_return_method(
                validated_input[0], validated_input[1])


registration_view = RegistrationView.as_view('registration_view')
login_view = LoginView.as_view('login_view')

auth_blueprint.add_url_rule(
    '/api/v2/auth/signup',
    view_func=registration_view,
    methods=['POST'])

auth_blueprint.add_url_rule(
    '/api/v2/auth/login',
    view_func=login_view,
    methods=['POST']
)
