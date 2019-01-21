import uuid
from datetime import datetime


class Incident:
    def __init__(self, *args):
        """Initialize an incident object"""
        incident_info = args[0]
        self.id = uuid.uuid4().clock_seq
        self.created_on = datetime.now()
        self.created_by = incident_info[0]
        self.type = incident_info[1]
        self.location = incident_info[2]
        self.status = incident_info[3]
        self.images = incident_info[4]
        self.videos = incident_info[5]
        self.comment = incident_info[6]

    def to_json_object(self):
        return self.__dict__
