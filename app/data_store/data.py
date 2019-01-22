from app.models.user import User
from app.models.incident import Incident

register_user = {
    "firstname": "Bob",
    "lastname": "Marley",
    "othernames": "dfgdfs",
    "email": "bob.marley@gmail.com",
    "password": "afsdfas2A1",
    "phonenumber": "0414225555",
    "username": "Bob Mar"}
login_user = {
    "email": "bob.marley@gmail.com",
    "password": "afsdfas2A1"
}


user2_data_dictionary = {"firstname": "Bob", "lastname": "Marley", "othernames": "",
                         "email": "bob.marley@gmail.com", "password": "afsQdfas21", "phonenumber": "0414225555", "username": "Bob Mar"}
user3_data_dictionary = {
    "firstname": "Christine",
    "lastname": "Turky",
    "othernames": "Sweeri",
    "email": "christinet@gmail.com",
    "password": "asdfdsaf",
    "phonenumber": "013234565",
    "username": "Sweeri"}

user2_data = [
    "Bob",
    "Marley",
    "",
    "bob.marley@gmail.com",
    "afsQdfas21",
    "0414225555",
    "Bob Mar",
    "False"]

user3_data = [
    "Christine",
    "Turky",
    "Sweeri",
    "christinet@gmail.com",
    "asdfdsaf",
    "013234565",
    "Sweeri",
    "True"]

user2 = User(user2_data)
user3 = User(user3_data)

users = [user2, user3]

incident1_data = [3,
                  "red-flag",
                  "0.215, 0.784",
                  "New",
                  ["images-link-1",
                   "images-link-1"],
                  ["videos-link-1",
                      "videos-link-2"],
                  "Traffic office James Komac, requested for money"]
incident2_data = [2,
                  "red-flag",
                  "0.114, 0.342",
                  "Rejected",
                  ["images-link-1",
                   "images-link-1"],
                  ["videos-link-1",
                      "videos-link-2"],
                  "National id official Kabulenge Christine wants a bribe"]
incident3_data = [2,
                  "intervation",
                  "0.435, 0.034",
                  "under-investigation",
                  ["images-link-1",
                   "images-link-1"],
                  ["videos-link-1",
                      "videos-link-2"],
                  "Bunamwaya has no clean water supply."]
incident4_data = [3,
                  "intervation",
                  "0.111, 0.344",
                  "Resolved",
                  ["images-link-1",
                   "images-link-1"],
                  ["videos-link-1",
                      "videos-link-2"],
                  "Kisasi bypass road has alot of traffic jam."]
incident5_data = [2, "red-flag", "0.113, 0.344", "under-investigation", ["images-link-1", "images-link-1"],
                     ["videos-link-1", "videos-link-2"], "Filling up and construction in the Kisasi road wetland!!"]

incident1_data_dictionary = {"created_by": 3, "type": "red-flag", "location": "0.215, 0.784", "status": "New", "images": [
    "images-link-1", "images-link-1"], "videos": ["videos-link-1", "videos-link-2"], "comment": "Traffic office James Komac, requested for money"}
incident2_data_dictionary = {
    "created_by": 2,
    "type": "red-flag",
    "location": "0.114, 0.342",
    "status": "Rejected",
    "images": [
        "images-link-1",
        "images-link-1"],
    "videos": [
        "videos-link-1",
        "videos-link-2"],
    "comment": "National id official Kabulenge Christine wants a bribe"}
incident3_data_dictionary = {
    "created_by": 2,
    "type": "intervation",
    "location": "0.435, 0.034",
    "status": "under-investigation",
    "images": [
        "images-link-1",
        "images-link-1"],
    "videos": [
        "videos-link-1",
        "videos-link-2"],
    "comment": "Bunamwaya has no clean water supply."}
incident4_data_dictionary = {"created_by": 3, "type": "intervation", "location": "0.111, 0.344", "status": "Resolved", "images": [
    "images-link-1", "images-link-1"], "videos": ["videos-link-1", "videos-link-2"], "comment": "Kisasi bypass road has alot of traffic jam."}
incident5_data_dictionary = {"created_by": 2, "type": "red-flag", "location": "0.113, 0.344", "status": "under-investigation", "images": ["images-link-1", "images-link-1"],
                             "videos": ["videos-link-1", "videos-link-2"], "comment": "Filling up and construction in the Kisasi road wetland!!"}
incident6_data_dictionary = {"created_by": 5, "type": "intervation", "location": "0.113, 0.344", "status": "Resolved", "images": ["images-link-1", "images-link-1"],
                             "videos": ["videos-link-1", "videos-link-2"], "comment": "Land grabbing in Gulu district!!"}

incident1 = Incident(incident1_data)
incident2 = Incident(incident2_data)
incident3 = Incident(incident3_data)
incident4 = Incident(incident4_data)
incident5 = Incident(incident5_data)

trial_incidents_list = [incident1, incident2, incident3, incident4, incident5]

incidents = []
new_location = {
    "location": "new location"
}

new_comment = {
    "comment": "This is the new comment to test on"
}

new_status = {
    "status": "Resolved"
}
