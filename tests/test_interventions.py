import unittest
import json
from app.views import create_app
from app.databases.database import Database
from tests.data_test_intervention import *

class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.database = Database()
        self.database.create_all_tables()
        self.database.create_default_admin()

        self.response = self.client.post('/api/v2/auth/signup', data=json.dumps(register_user_2),
                                         content_type='application/json')
    
        self.response = self.client.post('/api/v2/auth/login', data=json.dumps(login_user_2),
                                         content_type='application/json')
        data = json.loads(self.response.data)
        self.token = data["data"][0]["access_token"]
        self.headers = ({"Authorization": "Bearer " + self.token})
        self.header_old = (
            {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NDc1OTUwMjksImlhdCI6MTU0NzU4NzgyOSwic3ViIjoxNjEwNSwiYWRuIjoiRmFsc2UifQ.AxU19wAI4_oPw0vyTgweu7MZ4Bf4VV6tsk4pJK68GrA"})

    def test_create_new_intervention(self):
        response = self.client.post('/api/v1/red-flags', data=json.dumps(incident6_data_dictionary),
                                    content_type='application/json', headers=self.headers)
        data = json.loads(response.data)
        self.assertEqual(data["status"], 201)
        self.assertEqual(data["data"][0]["message"], "Created red-flag record")

   
    def test_create_new_intervention_already_saved(self):
        self.client.post('/api/v1/red-flags', data=json.dumps(incident6_data_dictionary),
                         content_type='application/json', headers=self.headers)
        response = self.client.post('/api/v1/red-flags', data=json.dumps(incident6_data_dictionary),
                                    content_type='application/json', headers=self.headers)
        data = json.loads(response.data)
        self.assertEqual(data["status"], 400)
        self.assertEqual(data["error"], "a similar resource already exists.")

    def test_create_new_intervention_no_location(self):
        input_data = incident2_data_dictionary
        input_data["location"] = ""
        response = self.client.post('/api/v1/red-flags', data=json.dumps(input_data),
                                    content_type='application/json', headers=self.headers)
        data = json.loads(response.data)
        self.assertEqual(data["status"], 400)
        self.assertEqual(
            data["error"], "Valid location required. Location should be of type string")

    def test_create_new_intervention_no_comment(self):
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

    def test_create_new_intervention_no_image(self):
        input_data = incident3_data_dictionary
        input_data["images"] = " "
        response = self.client.post('/api/v1/red-flags', data=json.dumps(input_data),
                                    content_type='application/json', headers=self.headers)
        data = json.loads(response.data)
        self.assertEqual(data["status"], 400)
        self.assertEqual(
            data["error"], "Add images links in this format: [a, b, c]")

    def test_create_new_intervention_no_video(self):
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

    def test_create_new_intervention_no_status(self):
        input_data = incident3_data_dictionary
        input_data["status"] = " "
        response = self.client.post('/api/v1/red-flags', data=json.dumps(input_data),
                                    content_type='application/json', headers=self.headers)
        data = json.loads(response.data)
        self.assertEqual(data["status"], 400)
        self.assertEqual(
            data["error"], "Valid status required. Status should be of type string")


    def tearDown(self):
        self.database.delete_all_tables()


   
