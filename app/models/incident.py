# app/models/redflag.py
import uuid
from datetime import datetime, timedelta

class Incident:
	init_dict ={
				"created_by":"",
				"doc_type":"",
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
		self.doc_type = init_dict["doc_type"]
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
			"doc_type":self.doc_type,
			"location":self.location,
			"status":self.status,
			"images":self.images,
			"videos":self.videos,
			"comment":self.comment
		}


