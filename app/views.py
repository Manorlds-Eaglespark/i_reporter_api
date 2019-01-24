import os
import re
from flask import Flask, request, jsonify, make_response, json
from datetime import datetime
from instance.config import app_config
from app.data_store.data import incidents
from app.utilities.helper_functions import Helper_Functions
from app.utilities.incident_validation import Incident_Validation
from app.models.user import User
from app.mail import Mail
from os.path import join, dirname
from dotenv import load_dotenv

def create_app(config_name):

    from app.models.incident import Incident
    from app.models.user import User
    from app.databases.database import Database

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    database = Database()

    @app.route('/', methods=['GET'])
    def welcome_to_api():
        response = {"status": 200, "data": [{
            "message": "Welcome To iReporter API. Consume Using Endpoints Given Here.",
                                            "endpoint 1": "GET     /api/v1/red-flags",
                                            "endpoint 2": "GET     /api/v1/red-flags/<red-flag-id>",
                                            "endpoint 3": "POST    /api/v1/red-flags",
                                            "endpoint 4": "PATCH   /api/v1/red-flags/<red-flag-id>/location",
                                            "endpoint 5": "PATCH   /api/v1/red-flags/<red-flag-id>/comment",
                                            "endpoint 6": "DELETE  /red-flags/<red-flag-id>"}]}
        return make_response(jsonify(response)), 200

    @app.route('/api/v2/red-flags', methods=['GET'])
    def get_redflags():
        
      

        access_token = Helper_Functions.get_access_token()
        if access_token:
            user_id = User.decode_token(access_token)
            if not isinstance(user_id, str):
                data = database.get_all_red_flags()
                if len(data) > 0:
                    return make_response(
                        jsonify({"status": 200, "data": data})), 200
                else:
                    return Helper_Functions.the_return_method(
                        404, "No resource added yet.")
            else:
                return Helper_Functions.the_return_method(401, user_id)
        else:
            return Helper_Functions.the_return_method(
                401, "A Resource Token is required. Sign-in or log-in")

    @app.route('/api/v2/red-flags/<red_flag_id>', methods=['GET'])
    def get_a_redflag(red_flag_id):
        access_token = Helper_Functions.get_access_token()
        if access_token:
            user_id = User.decode_token(access_token)
            if not isinstance(user_id, str):
                data = database.get_incident_by_id(red_flag_id)
                if data:
                    return make_response(
                        jsonify({"status": 200, "data": [data]})), 200
                else:
                    return Helper_Functions.the_return_method(
                        404, "Resource not found.")
            else:
                return Helper_Functions.the_return_method(401, user_id)
        else:
            return Helper_Functions.the_return_method(
                401, "A Resource Token is required. Sign-in or log-in")

    @app.route('/api/v2/red-flags', methods=['POST'])
    def create_redflag():
        access_token = Helper_Functions.get_access_token()
        if access_token:
            user_id = User.decode_token(access_token)
            if not isinstance(user_id, str):
                input_data = json.loads(request.data)
                created_by = int(user_id)
                doc_type = 'red-flag'
                location = input_data['location']
                status = input_data['status']
                images = input_data['images']
                videos = input_data['videos']
                comment = input_data['comment']
                input_list = [
                    created_by,
                    doc_type,
                    location,
                    status,
                    images,
                    videos,
                    comment
                ]

                validate_inputs = Incident_Validation(
                    Helper_Functions.get_dict_data_from_list_incident(input_list))

                validated_inputs = validate_inputs.check_types()
                duplicate_exists = database.get_like_this_in_database(comment, created_by)

                if validated_inputs[0] == 200:

                    if not duplicate_exists:

                        red_flag = Incident(input_list)
                        incident_id = database.save_incident(red_flag)
                        return make_response(jsonify({"status": 201, "data": [
                                             {"id": incident_id, "message": "Created red-flag record"}]}))
                    else:
                        return make_response(
                            jsonify({"status": 400, "error": "a similar resource already exists."}))
                else:
                    return make_response(
                        jsonify({"status": validated_inputs[0], "error": validated_inputs[1]}))
            else:
                return Helper_Functions.the_return_method(401, user_id)
        else:
            return Helper_Functions.the_return_method(
                401, "A Resource Token is required. Sign-in or log-in")

    @app.route('/api/v2/red-flags/<red_flag_id>/location', methods=['PATCH'])
    def update_redflag_location(red_flag_id):
        access_token = Helper_Functions.get_access_token()
        if access_token:
            user_id = User.decode_token(access_token)
            if not isinstance(user_id, str):
                location = json.loads(request.data)['location']
                data = database.update_location_of_incident(
                    red_flag_id, location)
                if data:
                    return make_response(jsonify({"status": 200, "data": [
                                         {"id": data[0], "message":"Updated red-flag record’s location"}]}))
                else:
                    return make_response(
                        jsonify({"status": 404, "error": "Resource not found."}))
            else:
                return Helper_Functions.the_return_method(401, user_id)
        else:
            return Helper_Functions.the_return_method(
                401, "A Resource Token is required. Sign-in or log-in")

    @app.route('/api/v2/red-flags/<red_flag_id>/comment', methods=['PATCH'])
    def update_redflag_comment(red_flag_id):

        access_token = Helper_Functions.get_access_token()
        if access_token:
            user_id = User.decode_token(access_token)
            if not isinstance(user_id, str):

                comment = json.loads(request.data)['comment']
                data = database.update_comment_of_incident(
                    red_flag_id, comment)

                if data:
                    return make_response(jsonify({"status": 200, "data": [
                                         {"id": data, "message":"Updated red-flag record’s comment"}]}))
                else:
                    return make_response(
                        jsonify({"status": 404, "error": "Resource not found."}))
            else:
                return Helper_Functions.the_return_method(401, user_id)
        else:
            return Helper_Functions.the_return_method(
                401, "A Resource Token is required. Sign-in or log-in")

    @app.route('/api/v2/red-flags/<red_flag_id>', methods=['DELETE'])
    def delete_redflag(red_flag_id):

        access_token = Helper_Functions.get_access_token()

        if access_token:
            user_id = User.decode_token(access_token)
            if not isinstance(user_id, str):
                if database.get_incident_by_id(red_flag_id):
                    database.delete_incident(red_flag_id)
                    return make_response(jsonify({"status": 200, "data": [
                                         {"id": red_flag_id, "message": "red-flag record has been deleted"}]}))
                else:
                    return make_response(
                        jsonify({"status": 404, "error": "Resource not found."}))
            else:
                return Helper_Functions.the_return_method(401, user_id)
        else:
            return Helper_Functions.the_return_method(
                401, "A Resource Token is required. Sign-in or log-in")

    @app.route('/api/v2/red-flags/<red_flag_id>/status', methods=['PATCH'])
    def update_redflag_status(red_flag_id):

        access_token = Helper_Functions.get_access_token()

        if access_token:
            is_admin = Helper_Functions.get_admin_status(access_token)
            if is_admin:
                user_id = User.decode_token(access_token)
                if not isinstance(user_id, str):

                    status = json.loads(request.data)['status']
                    

                    if database.get_incident_by_id(red_flag_id):
                        data = database.update_status_of_incident(
                            red_flag_id, status)
                        return make_response(jsonify({"status": 200, "data": [
                            {"id": data, "message":"Updated red-flag record’s status"}]}))
                    else:
                        return make_response(
                            jsonify({"status": 404, "error": "Resource not found."}))
                else:
                    return Helper_Functions.the_return_method(401, user_id)
            else:
                return Helper_Functions.the_return_method(
                    401, "Access denied.")
        else:
            return Helper_Functions.the_return_method(
                401, "A Resource Token is required. Sign-in or log-in")


    @app.route('/api/v2/interventions', methods=['POST'])
    def create_intervention_record():
        access_token = Helper_Functions.get_access_token()
        if access_token:
            user_id = User.decode_token(access_token)
            if not isinstance(user_id, str):
                input_data = json.loads(request.data)
                created_by = int(user_id)
                doc_type = 'intervention'
                location = input_data['location']
                status = input_data['status']
                images = input_data['images']
                videos = input_data['videos']
                comment = input_data['comment']
                input_list = [
                    created_by,
                    doc_type,
                    location,
                    status,
                    images,
                    videos,
                    comment
                ]

                validate_inputs = Incident_Validation(
                    Helper_Functions.get_dict_data_from_list_incident(input_list))

                validated_inputs = validate_inputs.check_types()
                duplicate_exists = database.get_like_this_in_database(comment, created_by)

                if validated_inputs[0] == 200:

                    if not duplicate_exists:

                        red_flag = Incident(input_list)
                        incident_id = database.save_incident(red_flag)
                        return make_response(jsonify({"status": 201, "data": [
                                             {"id": incident_id, "message": "Created red-flag record"}]}))
                    else:
                        return make_response(
                            jsonify({"status": 400, "error": "a similar resource already exists."}))
                else:
                    return make_response(
                        jsonify({"status": validated_inputs[0], "error": validated_inputs[1]}))
            else:
                return Helper_Functions.the_return_method(401, user_id)
        else:
            return Helper_Functions.the_return_method(
                401, "A Resource Token is required. Sign-in or log-in")


    @app.route('/api/v2/interventions', methods=['GET'])
    def get_intervention_records():
        access_token = Helper_Functions.get_access_token()
        if access_token:
            user_id = User.decode_token(access_token)
            if not isinstance(user_id, str):
                data = database.get_all_interventions()
                if len(data) > 0:
                    return make_response(
                        jsonify({"status": 200, "data": Helper_Functions.convert_to_dictionary_list(data)})), 200
                else:
                    return Helper_Functions.the_return_method(
                        404, "No resource added yet.")
            else:
                return Helper_Functions.the_return_method(401, user_id)
        else:
            return Helper_Functions.the_return_method(
                401, "A Resource Token is required. Sign-in or log-in")


    @app.route('/api/v2/interventions/<intervention_id>', methods=['GET'])
    def get_an_intervention_record(intervention_id):
        access_token = Helper_Functions.get_access_token()
        if access_token:
            user_id = User.decode_token(access_token)
            if not isinstance(user_id, str):
                data = database.get_incident_by_id(intervention_id)
                
                if data:
                    return make_response(
                        jsonify({"status": 200, "data": [Incident.convert_to_dictionary(data)]})), 200
                else:
                    return Helper_Functions.the_return_method(
                        404, "Resource not found.")
            else:
                return Helper_Functions.the_return_method(401, user_id)
        else:
            return Helper_Functions.the_return_method(
                401, "A Resource Token is required. Sign-in or log-in")


    @app.route('/api/v2/interventions/<intervention_id>/comment', methods=['PATCH'])
    def intervention_comment(intervention_id):

            access_token = Helper_Functions.get_access_token()
            if access_token:
                user_id = User.decode_token(access_token)
                if not isinstance(user_id, str):

                    comment = json.loads(request.data)['comment']
                    data = database.update_comment_of_incident(
                        intervention_id, comment)

                    if data:
                        return make_response(jsonify({"status": 200, "data": [
                                            {"id": data, "message": "Updated intervention record’s comment"}]}))
                    else:
                        return make_response(
                            jsonify({"status": 404, "error": "Resource not found."}))
                else:
                    return Helper_Functions.the_return_method(401, user_id)
            else:
                return Helper_Functions.the_return_method(
                    401, "A Resource Token is required. Sign-in or log-in")

    @app.route('/api/v2/interventions/<intervention_id>', methods=['DELETE'])
    def delete_interventions(intervention_id):

        access_token = Helper_Functions.get_access_token()

        if access_token:
            user_id = User.decode_token(access_token)
            if not isinstance(user_id, str):
                if database.get_incident_by_id(intervention_id):
                    database.delete_incident(intervention_id)
                    return make_response(jsonify({"status": 200, "data": [
                                         {"id": intervention_id, "message": "Intervention record has been deleted"}]}))
                else:
                    return make_response(
                        jsonify({"status": 404, "error": "Resource not found."}))
            else:
                return Helper_Functions.the_return_method(401, user_id)
        else:
            return Helper_Functions.the_return_method(
                401, "A Resource Token is required. Sign-in or log-in")

  
    from .auth import auth_blueprint
    app.register_blueprint(auth_blueprint)
    return app
