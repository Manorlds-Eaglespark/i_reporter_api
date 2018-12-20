from app.models.incident import Incident
from app.data_store.data import incidents


class Helper_Functions:

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
