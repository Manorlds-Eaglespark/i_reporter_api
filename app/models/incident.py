import uuid
from datetime import datetime


class Incident:
    def __init__(self, *args):
        """Initialize an incident object"""
        incident_info = args[0]
        self.created_on = datetime.now()
        self.created_by = incident_info[0]
        self.t_ype = incident_info[1]
        self.location = incident_info[2]
        self.status = incident_info[3]
        self.images = incident_info[4]
        self.videos = incident_info[5]
        self.comment = incident_info[6]

    def to_json_object(self):
        return self.__dict__

    @staticmethod
    def convert_to_dictionary(data_list):
        return{
            "id": data_list[0],
            "created_on": data_list[1],
            "created_by": data_list[2],
            "type": data_list[3],
            "location": data_list[4],
            "status": data_list[5],
            "images": data_list[6],
            "videos": data_list[7],
            "comment": data_list[8]
        }
