from app.models.user import User
# from app.models.admin import Admin
from app.models.incident import Incident

#users

# user1 = Admin(1, "Anorld", "Mukone", "Magister", "manorldsapiens@gmail.com", "123456", "0785555", "Manorld")
register_user = {"firstname":"Bob", "lastname":"Marley", "othernames":"", "email":"bobmareley@gmail.com", "password":"afsdfas2A1", "phonenumber":"0414225555", "username":"Bob Mar"}
login_user = {
                "email": "bob.marley@gmail.com",
                "password": "afsQdfas21"
            }


user2_data_dictionary = {"firstname":"Bob", "lastname":"Marley", "othernames":"",
                         "email":"bob.marley@gmail.com", "password":"afsQdfas21", "phonenumber":"0414225555", "username":"Bob Mar"}
user3_data_dictionary = {"firstname":"Christine", "lastname":"Turky", "othernames":"Sweeri","email":"christinet@gmail.com", "password":"asdfdsaf", "phonenumber":"013234565", "username":"Sweeri"}

user2_data = ["Bob", "Marley", "","bob.marley@gmail.com", "afsQdfas21", "0414225555", "Bob Mar"]
user3_data = ["Christine", "Turky", "Sweeri","christinet@gmail.com", "asdfdsaf", "013234565", "Sweeri"]
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

incident1_data_dictionary = {"created_by": 3, "type": "red-flag", "location": "0.215, 0.784", "status": "New", "images": "images-link", "videos": "videos-link", "comment": "Traffic office James Komac, requested for money"}
incident2_data_dictionary = {"created_by": 2, "type": "red-flag", "location": "0.114, 0.342", "status": "Rejected", "images": "images-link", "videos": "videos-link", "comment": "National id official Kabulenge Christine wants a bribe"}
incident3_data_dictionary = {"created_by": 2, "type": "intervation", "location": "0.435, 0.034", "status": "under-investigation", "images": "images-link", "videos": "videos-link", "comment": "Bunamwaya has no clean water supply."}
incident4_data_dictionary = {"created_by": 3, "type": "intervation", "location": "0.111, 0.344", "status": "Resolved", "images": "images-link", "videos": "videos-link", "comment":"Kisasi bypass road has alot of traffic jam."}
incident5_data_dictionary = {"created_by": 2, "type": "red-flag", "location": "0.113, 0.344", "status": "under-investigation", "images": "images-link",
                             "videos": "videos-link", "comment": "Filling up and construction in the Kisasi road wetland!!"}
incident6_data_dictionary = {"created_by": 5, "type": "intervation", "location": "0.113, 0.344", "status": "Resolved", "images": "images-link",
                             "videos": "videos-link", "comment": "Land grabbing in Gulu district!!"}

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
