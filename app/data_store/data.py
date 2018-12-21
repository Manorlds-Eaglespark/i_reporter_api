from app.models.user import User
# from app.models.admin import Admin
from app.models.incident import Incident

#users

# user1 = Admin(1, "Anorld", "Mukone", "Magister", "manorldsapiens@gmail.com", "123456", "0785555", "Manorld")
user2 = User({"id":1,"firstname": "Bob", "lastname": "Marley", "othernames": "", "email": "bob.marley@gmail.com", "password": "afsdfas21", "phonenumber": "0414225555", "username":"Bob Mar"})
user3 = User({"id": 3, "firstname": "Christine", "lastname": "Turky", "othernames": "Sweeri", "email":"christinet@gmail.com", "password":"asdfdsaf", "phonenumber":"013234565", "username":"Sweeri"})

users = [user2, user3]

incident1_data = {"created_by":3, "type":"red-flag", "location":"0.215, 0.784", "status":"New", "images":"images-link","videos":"videos-link", "comment":"Traffic office James Komac, requested for money"}
incident2_data = {"created_by":2, "type":"red-flag", "location":"0.114, 0.342", "status":"Rejected", "images":"images-link",
                     "videos":"videos-link", "comment":"National id official Kabulenge Christine wants a bribe"}
incident3_data = {"created_by":2, "type":"intervation", "location":"0.435, 0.034", "status":"under-investigation",
                     "images":"images-link", "videos":"videos-link", "comment":"Bunamwaya has no clean water supply."}
incident4_data = {"created_by":3, "type":"intervation", "location":"0.111, 0.344", "status":"Resolved",
                     "images":"images-link", "videos":"videos-link", "comment":"Kisasi bypass road has alot of traffic jam."}
incident5_data = {"created_by":2, "type":"red-flag", "location":"0.113, 0.344", "status":"under-investigation", "images":"images-link",
                     "videos":"videos-link", "comment":"Filling up and construction in the Kisasi road wetland!!"}

#incidents
incident1 = Incident(incident1_data)
incident2 = Incident(incident2_data)
incident3 = Incident(incident3_data)
incident4 = Incident(incident4_data)
incident5 = Incident(incident5_data)

incidents = [incident1, incident2, incident3, incident4, incident5]

new_location = {
	"location": "new location"
}

new_comment = {
	"comment": "This is the new comment"
}
