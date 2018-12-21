# /app/auth/views.py
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from . import auth_blueprint
from flask.views import MethodView
from flask import make_response, request, jsonify, abort, json
from app.models.user import User
from app.data_store.data import users
import re


class RegistrationView(MethodView):
    """This class registers a new user."""

    def post(self):
        """Handle POST request for this view. Url ---> /v1/auth/register"""

        firstname = json.loads(request.data)['firstname']
        lastname = json.loads(request.data)['lastname']
        othernames = json.loads(request.data)['othernames']
        email = json.loads(request.data)['email']
        password = json.loads(request.data)['password']
        phonenumber = json.loads(request.data)['phonenumber']
        username = json.loads(request.data)['username']

        new_user = User(firstname, lastname, othernames, email, password, phonenumber, username)
        users.append(new_user)
        return make_response(jsonify({"status": 201, "message": "You registered successfully. Login to continue."})), 201

class LoginView(MethodView):
    """This class-based view handles user login and access token generation."""

    def post(self):
        """Handle POST request for this view. Url ---> /v1/auth/login"""
        password = json.loads(request.data)['password']
        email = json.loads(request.data)['email']
        try:
          pass
        except Exception as e:
            response = {
                'message': str(e)
            }
            return make_response(jsonify(response)), 500


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
