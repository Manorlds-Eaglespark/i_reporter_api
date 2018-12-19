# app/models/redflag.py
import uuid
from datetime import datetime, timedelta
from app.data_store.data import incidents

created_on = ""
created_by = ""
doc_type = ""
location = ""
status = ""
images = ""
videos = ""
comment = ""

class Incident:
	def __init__(self, *args):
		self.id = uuid.uuid1()
		self.created_on = datetime.now()
		self.created_by = created_by
		self.doc_type = doc_type
		self.location = location
		self.status = status
		self.images = images
		self.videos = videos
		self.comment = comment

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

	@staticmethod
	def get_red_flags():
		red_flags_list = []
		for incident in incidents:
			if incident.doc_type == "red-flag":
				red_flags_list.append(incident.to_json_object())
		return red_flags_list
