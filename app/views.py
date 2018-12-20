# app/views.py
import re
from flask import Flask, request, jsonify, make_response, json
from datetime import datetime
from instance.config import app_config
from app.data_store.data import incidents


def create_app(config_name):

    from app.models.incident import Incident
    from app.models.admin import Admin
    from app.models.user import User

    from app.utilities.helper_functions import Helper_Functions


    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config['development'])
    app.config.from_pyfile('config.py')


    @app.route('/api/v1/red-flags', methods=['GET'])
    def get_redflags():
        data = Helper_Functions.get_red_flags()
        return make_response(jsonify({"status":200, "data":data})), 200

    @app.route('/api/v1/red-flags/<red_flag_id>', methods=['GET'])
    def get_a_redflag(red_flag_id):
        data = Helper_Functions.get_a_red_flag(red_flag_id)
        return make_response(jsonify({"status": 200, "data": data})), 200

    @app.route('/api/v1/red-flags', methods=['POST'])
    def create_redflag():
        created_by = json.loads(request.data)['created_by']
        doc_type = json.loads(request.data)['doc_type']
        location = json.loads(request.data)['location']
        status = json.loads(request.data)['status']
        images = json.loads(request.data)['images']
        videos = json.loads(request.data)['videos']
        comment = json.loads(request.data)['comment']

        data = Helper_Functions.get_dict_data_from_list([created_by, doc_type, location,
                status, images, videos, comment])
        validation = Helper_Functions.validate_incident_input(data)
        # return str(validation)
        if validation[0] == 200:
            red_flag = Incident(data)
            incidents.append(red_flag)
            return Helper_Functions.the_return_method(201, red_flag.to_json_object(), "Created red-flag record")
        else:
            return Helper_Functions.the_return_method(validation[0], "None", validation[1])
    
    @app.route('/api/v1/red-flags/<red_flag_id>/location', methods=['PATCH'])
    def update_redflag_location(red_flag_id):
        location = json.loads(request.data)['location']
        data = Helper_Functions.update_location(red_flag_id, location)
        return Helper_Functions.the_return_method(200, data, "Updated red-flag record’s location")

    @app.route('/api/v1/red-flags/<red_flag_id>/comment', methods=['PATCH'])
    def update_redflag_comment(red_flag_id):
        comment = json.loads(request.data)['comment']
        data = Helper_Functions.update_comment(red_flag_id, comment)
        return Helper_Functions.the_return_method(200, data, "Updated red-flag record’s comment")

    @app.route('/api/v1/red-flags/<red_flag_id>', methods=['DELETE'])
    def delete_redflag(red_flag_id):
        if Helper_Functions.delete_redflag(red_flag_id):
            data = ""
            return Helper_Functions.the_return_method(200, data, "red-flag record has been deleted”")

    from .auth import auth_blueprint
    app.register_blueprint(auth_blueprint)
    return app
