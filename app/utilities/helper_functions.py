from app.models.incident import Incident
from app.data_store.data import incidents
from flask import make_response, jsonify


class Helper_Functions:

    @staticmethod
    def the_return_method(status, data, message):
        return make_response(jsonify({"status": status, "data": data, "message": message})), status


    @staticmethod
    def get_red_flags():
        red_flags_list = []
        for incident in incidents:
            if incident.doc_type == "red-flag":
                red_flags_list.append(incident.to_json_object())
        return red_flags_list
    @staticmethod
    def get_a_red_flag(id):
        for incident in incidents:
            if incident.id == int(id):
                return incident.to_json_object()
    
    @staticmethod
    def get_dict_data_from_list(list_data):
        return {
         			"created_by": list_data[0],
         			"doc_type": list_data[1],
         			"location": list_data[2],
         			"status": list_data[3],
         			"images": list_data[4],
         			"videos": list_data[5],
         			"comment": list_data[6]
        }

    @staticmethod
    def validate_incident_input(data):
        if not data["created_by"]:
            return [400, "created_by required for user creating this redflag", data["created_by"]]
        if type(data["created_by"]) is not int:
            return[400, "created_by should be of type int."]
        if not data["doc_type"] == "red-flag" or not data["doc_type"] == "intervation":
            return[400, "doc_type is either red-flag or intervation"]
        if not data["location"] or data["location"].isspace():
            return [400, "Location field required."]
        if not data["status"] or not data["images"] or not data["videos"] or not data["comment"]:
            return [400, "Make sure you filled these required fields: Status, images, videos and comment"]

        return [200, "All Good"]

    @staticmethod
    def update_location(id, location):
        for incident in incidents:
            if incident.id == int(id):
                incident.location = location
                return incident.to_json_object()

    @staticmethod
    def update_comment(id, comment):
        for incident in incidents:
            if incident.id == int(id):
                incident.comment = comment
                return incident.to_json_object()

    @staticmethod
    def delete_redflag(id):
        for incident in incidents:
            if incident.id == int(id):
                incidents.remove(incident)
                return True
        return False
