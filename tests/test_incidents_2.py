import unittest
import json
from app.views import create_app
from app.data_store.data import incidents, login_user, incident5_data_dictionary, incident1_data_dictionary, incident2_data_dictionary, incident6_data_dictionary, incident3_data_dictionary, new_location, new_comment, incident3

class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        login_this_user =   {
                                "email": "bob.marley@gmail.com",
                                "password": "afsQdfas21"
                            }
        self.response = self.client.post('/api/v1/auth/login', data=json.dumps(login_this_user),
                                    content_type='application/json')
        data = json.loads(self.response.data)
        self.token = data["data"][0]["access_token"]
        self.headers=({"Authorization": "Bearer " + self.token + "_"})
        self.header_old = (
            {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NDc1OTUwMjksImlhdCI6MTU0NzU4NzgyOSwic3ViIjoxNjEwNSwiYWRuIjoiRmFsc2UifQ.AxU19wAI4_oPw0vyTgweu7MZ4Bf4VV6tsk4pJK68GrA" + "_"})

    def test_get_list_of_incidents_no_token_header(self):
        redflag_incident = {
                                "created_by": 5242,
                                "type": "red-flag",
                                "location": "0.112, 0.545",
                                "status": " sdfsd",
                                "images": ["sdfaf", "vfdgdf"],
                                "videos": ["video link", "fgfdgs"],
                                "comment": "This is the comment sgfd"
                            }
        self.client.post('/api/v1/red-flags', data=json.dumps(redflag_incident),
                         content_type='application/json', headers=self.headers)
        response = self.client.get('/api/v1/red-flags')
        data = json.loads(response.data)
        self.assertEqual(data["status"], 401)

    def test_get_an_incident_no_token_header(self):
        id = incidents[0].id
        response = self.client.get(
            '/api/v1/red-flags/'+str(id))
        data = json.loads(response.data)
        self.assertEqual(data["status"], 401)

    def test_create_new_red_flag_no_token_header(self):
        response = self.client.post('/api/v1/red-flags', data=json.dumps(incident6_data_dictionary),
                                    content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(data["status"], 401)

    def test_delete_red_flag_given_id_no_token_header(self):
        incidents.append(incident3)
        id = incidents[0].id
        response = self.client.delete(
            '/api/v1/red-flags/'+str(id))
        data = json.loads(response.data)
        self.assertEqual(data["status"], 401)


    def test_update_red_flag_comment_no_token_header(self):
        redflag_incident = {
                                "created_by": 5242,
                                "type": "red-flag",
                                "location": "0.112, 0.545",
                                "status": " sdfsd",
                                "images": ["sdfaf", "vfdgdf"],
                                "videos": ["video link", "fgfdgs"],
                                "comment": "This is the comment sgfd"
                            }
        self.client.post('/api/v1/red-flags', data=json.dumps(redflag_incident),
                         content_type='application/json', headers=self.headers)
        id = incidents[0].id
        response = self.client.patch('/api/v1/red-flags/'+str(id)+'/comment', data=json.dumps(new_comment),
                                     content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(data["status"], 401)


    def test_update_red_flag_location_no_header_token(self):
        redflag_incident = {
                                "created_by": 5242,
                                "type": "red-flag",
                                "location": "0.112, 0.545",
                                "status": " sdfsd",
                                "images": ["sdfaf", "vfdgdf"],
                                "videos": ["video link", "fgfdgs"],
                                "comment": "This is the comment sgfd"
                            }
        self.client.post('/api/v1/red-flags', data=json.dumps(redflag_incident),
                            content_type='application/json', headers=self.headers)
        id = incidents[0].id
        response = self.client.patch('/api/v1/red-flags/'+str(id)+'/location', data=json.dumps(new_location),
                                        content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(data["status"], 401)



    def test_get_list_of_incidents_expired_token_header(self):
        redflag_incident = {
                                "created_by": 5242,
                                "type": "red-flag",
                                "location": "0.112, 0.545",
                                "status": " sdfsd",
                                "images": ["sdfaf", "vfdgdf"],
                                "videos": ["video link", "fgfdgs"],
                                "comment": "This is the comment sgfd"
                            }
        self.client.post('/api/v1/red-flags', data=json.dumps(redflag_incident),
                         content_type='application/json', headers=self.headers)
        response = self.client.get('/api/v1/red-flags', headers=self.header_old)
        data = json.loads(response.data)
        self.assertEqual(data["status"], 401)

    def test_get_an_incident_expired_token_header(self):
        id = incidents[0].id
        response = self.client.get(
            '/api/v1/red-flags/'+str(id), headers=self.header_old)
        data = json.loads(response.data)
        self.assertEqual(data["status"], 401)

    def test_create_new_red_flag_expired_token_header(self):
        response = self.client.post('/api/v1/red-flags', data=json.dumps(incident6_data_dictionary),
                                    content_type='application/json', headers=self.header_old)
        data = json.loads(response.data)
        self.assertEqual(data["status"], 401)

    def test_delete_red_flag_given_id_expired_token_header(self):
        incidents.append(incident3)
        id = incidents[0].id
        response = self.client.delete(
            '/api/v1/red-flags/'+str(id), headers=self.header_old)
        data = json.loads(response.data)
        self.assertEqual(data["status"], 401)


    def test_update_red_flag_comment_expired_token_header(self):
        redflag_incident = {
                                "created_by": 5242,
                                "type": "red-flag",
                                "location": "0.112, 0.545",
                                "status": " sdfsd",
                                "images": ["sdfaf", "vfdgdf"],
                                "videos": ["video link", "fgfdgs"],
                                "comment": "This is the comment sgfd"
                            }
        self.client.post('/api/v1/red-flags', data=json.dumps(redflag_incident),
                         content_type='application/json', headers=self.headers)
        id = incidents[0].id
        response = self.client.patch('/api/v1/red-flags/'+str(id)+'/comment', data=json.dumps(new_comment),
                                     content_type='application/json', headers=self.header_old)
        data = json.loads(response.data)
        self.assertEqual(data["status"], 401)


    def test_update_red_flag_location_expired_token_header(self):
        redflag_incident = {
                                "created_by": 5242,
                                "type": "red-flag",
                                "location": "0.112, 0.545",
                                "status": " sdfsd",
                                "images": ["sdfaf", "vfdgdf"],
                                "videos": ["video link", "fgfdgs"],
                                "comment": "This is the comment sgfd"
                            }
        self.client.post('/api/v1/red-flags', data=json.dumps(redflag_incident),
                            content_type='application/json', headers=self.headers)
        id = incidents[0].id
        response = self.client.patch('/api/v1/red-flags/'+str(id)+'/location', data=json.dumps(new_location),
                                        content_type='application/json', headers=self.header_old)
        data = json.loads(response.data)
        self.assertEqual(data["status"], 401)