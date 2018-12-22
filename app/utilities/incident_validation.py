

init_dict = {
        "created_by": "",
        "type": "",
        "location": "",
        "status": "",
        "images": "",
        "videos": "",
        "comment": ""
    }

class Incident_Validation():
    def __init__(self, init_dict):
        self.created_by = init_dict["created_by"]
        self.type = init_dict["type"]
        self.location = init_dict["location"]
        self.status = init_dict["status"]
        self.images = init_dict["images"]
        self.videos = init_dict["videos"]
        self.comment = init_dict["comment"]

    def check_types(self):
        if type(self.created_by) is not int:
            return [400, "created_by field should be of type int"]
        elif type(self.type) is not str or self.type.isspace() or len(self.type) < 8:
            return [400, "Type should be of type string: Either 'red-flag' or 'intervation'"]
        elif type(self.location) is not str or self.location.isspace() or len(self.location) < 4:
            return [400, "Valid location required. Location should be of type string"]
        elif type(self.status) is not str or self.status.isspace() or len(self.status) < 4:
            return [400, "Valid status required. Status should be of type string"]
        elif type(self.images) is not str or self.images.isspace() or len(self.images) < 4:
            return [400, "Valid images link required. Images should be of type string"]
        elif type(self.videos) is not str or self.videos.isspace() or len(self.videos) < 4:
            return [400, "Valid video link required. Vidoes should be of type string"]
        elif type(self.comment) is not str or self.comment.isspace() or len(self.comment) < 4:
            return [400, "Valid comment required. Comment should be of type string"]
        return [200, "All good"]