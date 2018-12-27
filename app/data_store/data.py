from app.models.user import User
# from app.models.admin import Admin
from app.models.incident import Incident

#users

# user1 = Admin(1, "Anorld", "Mukone", "Magister", "manorldsapiens@gmail.com", "123456", "0785555", "Manorld")
register_user = {
                    "firstname": "Bob",
                    "lastname": "Marley",
                    "othernames": "",
                    "email": "bobmareley@gmail.com",
                    "password": "afsdfas2A1",
                    "phonenumber": "0414225555",
                    "username": "Bob Mar"
                    }
login_user = {
    "email": "bob.marley@gmail.com",
    "password": "afsQdfas21"
}
user2_data = {"firstname": "Bob", "lastname": "Marley", "othernames": "",
              "email": "bob.marley@gmail.com", "password": "afsQdfas21", "phonenumber": "0414225555", "username": "Bob Mar"}
user3_data = {"firstname": "Christine", "lastname": "Turky", "othernames": "Sweeri",
              "email": "christinet@gmail.com", "password": "asdfdsaf", "phonenumber": "013234565", "username": "Sweeri"}
user2 = User(user2_data)
user3 = User(user3_data)

users = [user2, user3]

# incident1_data = {"created_by":3, "type":"red-flag", "location":"0.215, 0.784", "status":"New", "images":"images-link","videos":"videos-link", "comment":"Traffic office James Komac, requested for money"}

incident1_data = [3, "red-flag", "0.215, 0.784", "New", "images-link","videos-link", "Traffic office James Komac, requested for money"]
incident2_data = [2, "red-flag", "0.114, 0.342", "Rejected", "images-link","videos-link", "National id official Kabulenge Christine wants a bribe"]
incident3_data =[2, "intervation", "0.435, 0.034", "under-investigation", "images-link", "videos-link", "Bunamwaya has no clean water supply."]
incident4_data = [3, "intervation", "0.111, 0.344", "Resolved", "images-link", "videos-link", "Kisasi bypass road has alot of traffic jam."]
incident5_data = [2, "red-flag", "0.113, 0.344", "under-investigation", "images-link",
                     "videos-link", "Filling up and construction in the Kisasi road wetland!!"]

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
