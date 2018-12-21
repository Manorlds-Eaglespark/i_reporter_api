# app/models/redflag.py
import uuid
from datetime import datetime

class Incident:
	init_dict ={
				"created_by":"",
				"type":"",
				"location":"",
				"status":"",
				"images":"",
				"videos":"",
				"comment":""
				}

	def __init__(self, init_dict):
		"""Initialize an incident object"""
		self.id = uuid.uuid4().clock_seq
		self.created_on = datetime.now()
		self.created_by = init_dict["created_by"]
		self.type = init_dict["type"]
		self.location = init_dict["location"]
		self.status = init_dict["status"]
		self.images = init_dict["images"]
		self.videos = init_dict["videos"]
		self.comment = init_dict["comment"]

	def to_json_object(self):
		return {
			"id":self.id,
			"created_on":self.created_on,
			"created_by":self.created_by,
			"type":self.type,
			"location":self.location,
			"status":self.status,
			"images":self.images,
			"videos":self.videos,
			"comment":self.comment
		}


