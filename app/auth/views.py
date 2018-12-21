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

class RegistrationView(MethodView):
    """This class registers a new user."""
    def post(self):

        firstname = json.loads(request.data)['firstname']
        lastname = json.loads(request.data)['lastname']
        othernames = json.loads(request.data)['othernames']
        email = json.loads(request.data)['email']
        password = json.loads(request.data)['password']
        phonenumber = json.loads(request.data)['phonenumber']
        username = json.loads(request.data)['username']

        if Helper_Functions.email_exists_already(email) is True:
            return make_response(jsonify({"status": 400, "message": "That Email already is registered. Login or use a different Email to register."})), 400
        else:
            new_user_info_list = [ firstname, lastname, othernames, email, password, phonenumber, username]
            new_user = User(Helper_Functions.get_dict_data_from_list_user(new_user_info_list))
            
            users.append(new_user)
            return make_response(jsonify({"status":201, "data":new_user.to_json_object(), "message":"You registered successfully. Login to continue."})), 201
            

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
                if User.password_is_valid(user.password, password):
     
                    access_token = user.generate_token(user.id, user.isadmin)
                    if access_token:
                            response = {
                                'message': 'You logged in successfully.',
                                'access_token':  access_token.decode()
                            }
                            return make_response(jsonify(response)), 200
                else:
                    return Helper_Functions.the_return_method(400, None, "Enter a valid Password")


            except Exception as e:
                response = {
                    'message': str(e)
                }
                return make_response(jsonify(response)), 500

        else:
            return Helper_Functions.the_return_method(validated_input[0], None, validated_input[1])


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
