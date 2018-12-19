from app.models.user import User
from app.models.admin import Admin
from app.models.incident import Incident


#users
user1 = Admin(1, "Anorld", "Mukone", "Magister", "manorldsapiens@gmail.com", "123456", "0785555", "Manorld")
user2 = User(2 "Bob", "Marley", "", "bob.marley@gmail.com", "afsdfas21", "0414225555", "Bob Mar")
user3 = User(3, "Christine", "Turky", "Sweeri", "christinet@gmail.com", "asdfdsaf", "013234565", "Sweeri")

users = [user1, user2, user3]

#incidents
incident1 = Incident(1, "2018-12-15 19:55:04.874256", 3, "redflag", "0.215, 0.784", "New", "images-link", "videos-link", "Traffic office James Komac, requested for money")
incident2 = Incident(2, "2018-12-16 19:55:04.127256", 2, "redflag", "0.114, 0.342", "Rejected", "images-link", "videos-link", "National id official Kabulenge Christine wants a bribe")
incident3 = Incident(3, "2018-12-17 19:55:04.757256", 2, "intervation", "0.435, 0.034", "under-investigation", "images-link", "videos-link", "Bunamwaya has no clean water supply.")
incident4 = Incident(4, "2018-12-18 19:55:04.967556", 3, "intervation", "0.111, 0.344", "Resolved", "images-link", "videos-link", "Kisasi bypass road has alot of traffic jam.")
incident5 = Incident(5, "2018-12-19 19:55:04.927258", 2, "redflag", "0.113, 0.344", "under-investigation", "images-link", "videos-link", "Filling up and construction in the Kisasi road wetland!!")

incidents = [incident1, incident2, incident3, incident4, incident5]