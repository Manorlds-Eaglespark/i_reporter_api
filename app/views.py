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


    @app.route('/api/v1/red-flags', methods=[GET'])
    def get_redflags():
        pass

    @app.route('/api/v1/red-flags/<red_flag_id>', methods=[GET'])
    def get_redflags(red_flag_id):
        pass

    @app.route('/api/v1/red-flags', methods=[POST'])
    def create_redflag():
        pass
    
    @app.route('/api/v1/red-flags/<red_flag_id>/location', methods=[PATCH'])
    def update_redflag_location(red_flag_id):
        pass

    @app.route('/api/v1/red-flags/<red_flag_id>/comment', methods=[PATCH'])
    def update_redflag_comment(red_flag_id):
        pass

    @app.route('/api/v1/red-flags/<red_flag_id>', methods=[DELETE'])
    def delete_redflag(red_flag_id):
        pass

    from .auth import auth_blueprint
    app.register_blueprint(auth_blueprint)
    return app