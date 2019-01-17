

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
        if not isinstance(self.created_by, int):
            return [400, "created_by field should be of type int"]
        elif not isinstance(self.type, str) or self.type.isspace() or len(self.type) < 8:
            return [
                400, "Type should be of type string: Either 'red-flag' or 'intervation'"]
        elif not isinstance(self.location, str) or self.location.isspace() or len(self.location) < 4:
            return [400, "Valid location required. Location should be of type string"]
        elif not isinstance(self.status, str) or self.status.isspace() or len(self.status) < 4:
            return [400, "Valid status required. Status should be of type string"]
        elif not isinstance(self.images, list) or not self.images or len(self.images) < 1:
            return [400, "Add images links in this format: [a, b, c]"]
        elif not isinstance(self.videos, list) or not self.videos or len(self.videos) < 1:
            return [400, "Add video links in this format: [a, b, c]"]
        elif not isinstance(self.comment, str) or self.comment.isspace() or len(self.comment) < 4:
            return [400, "Valid comment required. Comment should be of type string"]
        return [200, "All good"]
