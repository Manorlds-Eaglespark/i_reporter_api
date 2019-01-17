import uuid
from datetime import datetime


class Incident:
    def __init__(self, *args):
        """Initialize an incident object"""
        self.id = uuid.uuid4().clock_seq
        self.created_on = datetime.now()
        self.created_by = args[0][0]
        self.type = args[0][1]
        self.location = args[0][2]
        self.status = args[0][3]
        self.images = args[0][4]
        self.videos = args[0][5]
        self.comment = args[0][6]

    def to_json_object(self):
        return self.__dict__
