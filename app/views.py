# app/views.py
import re
from flask import Flask, request, jsonify, make_response, json
from datetime import datetime
from instance.config import app_config


def create_app(config_name):

    from app.models.incident import Incident
    from app.models.admin import Admin
    from app.models.user import User

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config['development'])
    app.config.from_pyfile('config.py')


    @app.route('/api/v1/redflags', methods=['POST', 'GET'])
    def get_and_post_redflags():
        pass

    from .auth import auth_blueprint
    app.register_blueprint(auth_blueprint)
    return app