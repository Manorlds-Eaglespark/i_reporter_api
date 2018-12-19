# app/models/redflag.py
from datetime import datetime, timedelta

class Incident:

	def __init__(self, *args):
		self.id = id
		self.createdOn = datetime.now()
		self.createdBy = CreatedBy
		self.doc_type = doc_type
		self.location = location
		self.status = status
		self.images = images
		self.videos = videos
		self.comment = comment
