import unittest
import json
from app.views import create_app
from app.databases.database import Database
from tests.data_test import *


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.email = self.app.config["ADMIN_EMAIL"]
        self.password = self.app.config["ADMIN_PASSWORD"]
        self.client = self.app.test_client()
        self.database = Database()
        self.database.create_all_tables()
        self.database.create_default_admin(self.email, self.password)

        self.response = self.client.post('/api/v2/auth/signup', data=json.dumps(register_user_2),
                                         content_type='application/json')

        self.response = self.client.post('/api/v2/auth/login', data=json.dumps(login_user_2),
                                         content_type='application/json')
        data = json.loads(self.response.data)
        self.token = data["data"][0]["access_token"]
        self.headers = ({"Authorization": "Bearer " + self.token})
        self.header_old = (
            {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NDc1OTUwMjksImlhdCI6MTU0NzU4NzgyOSwic3ViIjoxNjEwNSwiYWRuIjoiRmFsc2UifQ.AxU19wAI4_oPw0vyTgweu7MZ4Bf4VV6tsk4pJK68GrA"})

    def test_get_list_of_interventions_no_token_header(self):
        response = self.client.get('/api/v2/interventions')
        data = json.loads(response.data)
        self.assertEqual(data["status"], 401)

    def test_get_an_interventions_no_token_header(self):
        response = self.client.get(
            '/api/v2/interventions/' + str(id))
        data = json.loads(response.data)
        self.assertEqual(data["status"], 401)

    def test_create_new_intervention_no_token_header(self):
        response = self.client.post('/api/v2/interventions', data=json.dumps(incident6_data_dictionary),
                                    content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(data["status"], 401)

    def test_delete_intervention_id_no_token_header(self):
        response = self.client.delete(
            '/api/v2/interventions/' + str(id))
        data = json.loads(response.data)
        self.assertEqual(data["status"], 401)

    def test_update_intervention_comment_no_token_header(self):
        response = self.client.patch('/api/v2/interventions/' + str(id) + '/comment', data=json.dumps(new_comment),
                                     content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(data["status"], 401)


    def test_get_list_of_incidents_expired_token_header(self):        
        response = self.client.get(
            '/api/v2/interventions',
            headers=self.header_old)
        data = json.loads(response.data)
        self.assertEqual(data["status"], 401)

    def test_get_an_intervention_expired_token_header(self):

        response = self.client.get(
            '/api/v2/interventions/' + str(id), headers=self.header_old)
        data = json.loads(response.data)
        self.assertEqual(data["status"], 401)

    def test_create_new_interventions_expired_token_header(self):
        response = self.client.post('/api/v2/interventions', data=json.dumps(incident6_data_dictionary),
                                    content_type='application/json', headers=self.header_old)
        data = json.loads(response.data)
        self.assertEqual(data["status"], 401)

    def test_delete_intervention_given_id_expired_token_header(self):
        response = self.client.delete(
            '/api/v2/interventions/' + str(id), headers=self.header_old)
        data = json.loads(response.data)
        self.assertEqual(data["status"], 401)

    def test_update_intervention_comment_expired_token_header(self):
        response = self.client.patch('/api/v2/interventios/' + str(id) + '/comment', data=json.dumps(new_comment),
                                     content_type='application/json', headers=self.header_old)
        data = json.loads(response.data)
        self.assertEqual(data["status"], 401)


    def tearDown(self):
        self.database.delete_all_tables()
