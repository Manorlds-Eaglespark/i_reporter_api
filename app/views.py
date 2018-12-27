# app/views.py
import re
from flask import Flask, request, jsonify, make_response, json
from datetime import datetime
from instance.config import app_config
from app.data_store.data import incidents
from app.utilities.helper_functions import Helper_Functions
from app.utilities.incident_validation import Incident_Validation


def create_app(config_name):

    from app.models.incident import Incident
    # from app.models.admin import Admin
    from app.models.user import User

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config['development'])
    app.config.from_pyfile('config.py')

    @app.route('/api/v1/red-flags', methods=['GET'])
    def get_redflags():
        data = Helper_Functions.get_red_flags()
        if data:
            return make_response(jsonify({"status": 200, "data": data})), 200
        else:
            return make_response(jsonify({"status":404, "error":"No resource added yet."}))

    @app.route('/api/v1/red-flags/<red_flag_id>', methods=['GET'])
    def get_a_redflag(red_flag_id):
        data = Helper_Functions.get_a_red_flag(red_flag_id)
        if data:
            return make_response(jsonify({"status": 200, "data": [data]})), 200
        else:
            return make_response(jsonify({"status": 404, "error": "Resource not found."})), 404

    @app.route('/api/v1/red-flags', methods=['POST'])
    def create_redflag():

        input_data = json.loads(request.data)
        created_by = input_data['created_by']
        doc_type   = input_data['type']
        location   = input_data['location']
        status     = input_data['status']
        images     = input_data['images']
        videos     = input_data['videos']
        comment    = input_data['comment']

        input_list = [created_by, doc_type, location, status, images, videos, comment]

        validate_inputs = Incident_Validation(
            Helper_Functions.get_dict_data_from_list_incident(input_list))
        validated_inputs = validate_inputs.check_types()
        if validated_inputs[0] == 200:
            red_flag = Incident(input_list)
            incidents.append(red_flag)
            return make_response(jsonify({"status": 201, "data": [{"id":red_flag.id, "message":"Created red-flag record"}]}))
        else:
            return Helper_Functions.the_return_method(validated_inputs[0], None, validated_inputs[1])

    @app.route('/api/v1/red-flags/<red_flag_id>/location', methods=['PATCH'])
    def update_redflag_location(red_flag_id):
        location = json.loads(request.data)['location']
        data = Helper_Functions.update_location(red_flag_id, location)
        if data:
            return make_response(jsonify({"status": 200, "data": [{"id":data["id"], "message":"Updated red-flag record’s location"}]}))
        else:
            return Helper_Functions.the_return_method(404, None, "Red-flag not found")

    @app.route('/api/v1/red-flags/<red_flag_id>/comment', methods=['PATCH'])
    def update_redflag_comment(red_flag_id):
        comment = json.loads(request.data)['comment']
        data = Helper_Functions.update_comment(red_flag_id, comment)
        if data:
            return make_response(jsonify({"status": 200, "data": [{"id": data["id"], "message":"Updated red-flag record’s comment"}]}))
        else:
            return Helper_Functions.the_return_method(404, None, "Resource with that id not found")

    @app.route('/api/v1/red-flags/<red_flag_id>', methods=['DELETE'])
    def delete_redflag(red_flag_id):
        if Helper_Functions.delete_redflag(red_flag_id):
            return make_response(jsonify({"status": 200, "data": [{"id": red_flag_id, "message": "red-flag record has been deleted"}]}))
        else:
            return make_response(jsonify({"status":404, "error":"Resource not found."}))

    from .auth import auth_blueprint
    app.register_blueprint(auth_blueprint)
    return app
