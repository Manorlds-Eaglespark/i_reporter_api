from app.models.incident import Incident
from app.data_store.data import incidents
from app.data_store.data import users
from flask import make_response, jsonify, request
from app.models.user import User
from app.databases.database import Database

class Helper_Functions:

    @staticmethod
    def the_return_method(status, message):
        return make_response(
            jsonify({"status": status, "error": message})), status

    @staticmethod
    def get_dict_incidents(list_data):
        dictionary_list = []
        for item in list_data:
            dictionary_list.append(Incident.convert_to_dictionary(item))
        return dictionary_list

    @staticmethod
    def get_dict_user(list_data):
        return {
            "id":list_data[0],
            "firstname": list_data[1],
            "lastname": list_data[2],
            "othernames": list_data[3],
            "email": list_data[4],
            "phonenumber": list_data[6],
            "username": list_data[7]
        }

    @staticmethod
    def get_dict_data_from_list_incident(list_data):
        return {
            "created_by": list_data[0],
            "type": list_data[1],
            "location": list_data[2],
            "status": list_data[3],
            "images": list_data[4],
            "videos": list_data[5],
            "comment": list_data[6]
        }
        
    @staticmethod
    def owner_required(current_user, intervention_id):
        database = Database()
        incident_data = database.get_incident_by_id(intervention_id)
        
        created_by = incident_data[2]
        return created_by
        if current_user != int(created_by):
            return Helper_Functions.the_return_method(403, "This record does not belong to you.")

