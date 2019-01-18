import unittest
import json
from app.views import create_app
from app.data_store.data import incidents, login_user, incident5_data_dictionary,new_status, incident1_data_dictionary, incident2_data_dictionary, incident6_data_dictionary, incident3_data_dictionary, new_location, new_comment, incident3


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        login_this_user = {
            "email": "bob.marley@gmail.com",
            "password": "afsQdfas21"
        }
        login_this_admin = {
                            "email":"christinet@gmail.com",
                            "password":"asdfdsaf"
        }
        self.response = self.client.post('/api/v1/auth/login', data=json.dumps(login_this_user),
                                         content_type='application/json')
        self.response_2 = self.client.post('/api/v1/auth/login', data=json.dumps(login_this_admin),
                                         content_type='application/json')
        data = json.loads(self.response.data)
        data_2 = json.loads(self.response_2.data)
        self.token = data["data"][0]["access_token"]
        self.headers = ({"Authorization": "Bearer " + self.token})
        
        self.token_2 = data_2["data"][0]["access_token"]
        self.headers_admin = ({"Authorization": "Bearer " + self.token_2})
        self.header_old = (
            {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NDc1OTUwMjksImlhdCI6MTU0NzU4NzgyOSwic3ViIjoxNjEwNSwiYWRuIjoiRmFsc2UifQ.AxU19wAI4_oPw0vyTgweu7MZ4Bf4VV6tsk4pJK68GrA"})

    def test_server_is_running(self):
        response = self.client.get('/')
        data = json.loads(response.data)
        self.assertEqual(data["status"], 200)

    def test_get_list_of_incidents_when_none_exists(self):
        incidents.clear()
        response = self.client.get('/api/v1/red-flags', headers=self.headers)
        data = json.loads(response.data)
        self.assertEqual(data["status"], 404)
        self.assertEqual(data["error"], "No resource added yet.")

    def test_get_list_of_incidents(self):
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
        response = self.client.get('/api/v1/red-flags', headers=self.headers)
        data = json.loads(response.data)
        self.assertEqual(data["status"], 200)

    def test_create_new_red_flag(self):
        response = self.client.post('/api/v1/red-flags', data=json.dumps(incident6_data_dictionary),
                                    content_type='application/json', headers=self.headers)
        data = json.loads(response.data)
        self.assertEqual(data["status"], 201)
        self.assertEqual(data["data"][0]["message"], "Created red-flag record")

    def test_get_an_incident(self):
        id = incidents[0].id
        response = self.client.get(
            '/api/v1/red-flags/' + str(id), headers=self.headers)
        data = json.loads(response.data)
        self.assertEqual(data["status"], 200)

    def test_get_an_incident_with_unknown_id(self):
        response = self.client.get(
            '/api/v1/red-flags/' + str(1000010), headers=self.headers)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["error"], "Resource not found.")

    def test_create_new_red_flag_already_saved(self):
        response = self.client.post('/api/v1/red-flags', data=json.dumps(incident6_data_dictionary),
                                    content_type='application/json', headers=self.headers)
        data = json.loads(response.data)
        self.assertEqual(data["status"], 400)
        self.assertEqual(data["error"], "a similar resource already exists.")

    def test_create_new_red_flag_no_doc_type(self):
        input_data = incident1_data_dictionary
        input_data["type"] = ""
        response = self.client.post('/api/v1/red-flags', data=json.dumps(input_data),
                                    content_type='application/json', headers=self.headers)
        data = json.loads(response.data)
        self.assertEqual(data["status"], 400)
        self.assertEqual(
            data["error"], "Type should be of type string: Either 'red-flag' or 'intervation'")

    def test_create_new_red_flag_other_doc_type(self):
        input_data = incident1_data_dictionary
        input_data["type"] = "redd_flag"
        response = self.client.post('/api/v1/red-flags', data=json.dumps(input_data),
                                    content_type='application/json', headers=self.headers)
        data = json.loads(response.data)
        self.assertEqual(data["status"], 400)
        self.assertEqual(
            data["error"], "Valid status required. Status should be of type string")

    def test_create_new_red_flag_no_location(self):
        input_data = incident2_data_dictionary
        input_data["location"] = ""
        response = self.client.post('/api/v1/red-flags', data=json.dumps(input_data),
                                    content_type='application/json', headers=self.headers)
        data = json.loads(response.data)
        self.assertEqual(data["status"], 400)
        self.assertEqual(
            data["error"], "Valid location required. Location should be of type string")

    def test_create_new_red_flag_no_comment(self):
        input_data = incident3_data_dictionary
        input_data["videos"] = ["sfsfsdf.com/video/fsdffsdfdsf"]
        input_data["images"] = ["sfsfsdf.com/image/fsdffsdfdsf"]
        input_data["comment"] = ""
        response = self.client.post('/api/v1/red-flags', data=json.dumps(input_data),
                                    content_type='application/json', headers=self.headers)
        data = json.loads(response.data)
        self.assertEqual(data["status"], 400)
        self.assertEqual(
            data["error"], "Valid comment required. Comment should be of type string")

    def test_update_red_flag_location(self):
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
        response = self.client.patch('/api/v1/red-flags/' + str(id) + '/location', data=json.dumps(new_location),
                                     content_type='application/json', headers=self.headers)
        data = json.loads(response.data)
        self.assertEqual(data["status"], 200)
        self.assertEqual(
            data["data"][0]["message"],
            "Updated red-flag record’s location")

    
    def test_update_red_flag_status(self):
        redflag_incident = {
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
        response = self.client.patch('/api/v1/red-flags/' + str(id) + '/status', data=json.dumps(new_status),
                                     content_type='application/json', headers=self.headers_admin)
        data = json.loads(response.data)
        self.assertEqual(data["status"], 200)
        self.assertEqual(
            data["data"][0]["message"],
            "Updated red-flag record’s status")


    def test_update_red_flag_status_non_existent_id(self):
        response = self.client.patch('/api/v1/red-flags/' + str(100001002220) + '/status', data=json.dumps(new_status),
                                     content_type='application/json', headers=self.headers_admin)
        data = json.loads(response.data)
        self.assertEqual(data["status"], 404)
        self.assertEqual(
            data["error"], "Resource not found.")



    def test_update_red_flag_location_id_not_found(self):
        id = 15155200
        response = self.client.patch('/api/v1/red-flags/' + str(id) + '/location', data=json.dumps(new_location),
                                     content_type='application/json', headers=self.headers)
        data = json.loads(response.data)
        self.assertEqual(data["status"], 404)
        self.assertEqual(data["error"], "Resource not found.")

    def test_update_red_flag_comment(self):
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
        response = self.client.patch('/api/v1/red-flags/' + str(id) + '/comment', data=json.dumps(new_comment),
                                     content_type='application/json', headers=self.headers)
        data = json.loads(response.data)
        self.assertEqual(data["status"], 200)
        self.assertEqual(
            data["data"][0]["message"], "Updated red-flag record’s comment")

    def test_update_red_flag_comment_id_not_found(self):
        id = 15155200
        response = self.client.patch('/api/v1/red-flags/' + str(id) + '/comment', data=json.dumps(new_comment),
                                     content_type='application/json', headers=self.headers)
        data = json.loads(response.data)
        self.assertEqual(data["status"], 404)
        self.assertEqual(
            data["error"], "Resource not found.")

    def test_delete_red_flag_given_id(self):
        incidents.append(incident3)
        id = incidents[0].id
        response = self.client.delete(
            '/api/v1/red-flags/' + str(id),
            headers=self.headers)
        data = json.loads(response.data)
        self.assertEqual(data["status"], 200)
        self.assertEqual(
            data["data"][0]["message"],
            "red-flag record has been deleted")

    def test_delete_red_flag_given_wrong_id(self):
        response = self.client.delete(
            '/api/v1/red-flags/' + str(11), headers=self.headers)
        data = json.loads(response.data)
        self.assertEqual(data["status"], 404)
        self.assertEqual(data["error"], "Resource not found.")

    def test_create_new_red_flag_no_image(self):
        input_data = incident3_data_dictionary
        input_data["images"] = " "
        response = self.client.post('/api/v1/red-flags', data=json.dumps(input_data),
                                    content_type='application/json', headers=self.headers)
        data = json.loads(response.data)
        self.assertEqual(data["status"], 400)
        self.assertEqual(
            data["error"], "Add images links in this format: [a, b, c]")

    def test_create_new_red_flag_no_video(self):
        input_data = incident3_data_dictionary
        input_data["status"] = "red-flag"
        input_data["images"] = ["dsfdsf.com/images/image.jpg"]
        input_data["videos"] = " "
        response = self.client.post('/api/v1/red-flags', data=json.dumps(input_data),
                                    content_type='application/json', headers=self.headers)
        data = json.loads(response.data)
        self.assertEqual(data["status"], 400)
        self.assertEqual(
            data["error"], "Add video links in this format: [a, b, c]")

    def test_create_new_red_flag_no_status(self):
        input_data = incident3_data_dictionary
        input_data["status"] = " "
        response = self.client.post('/api/v1/red-flags', data=json.dumps(input_data),
                                    content_type='application/json', headers=self.headers)
        data = json.loads(response.data)
        self.assertEqual(data["status"], 400)
        self.assertEqual(
            data["error"], "Valid status required. Status should be of type string")
