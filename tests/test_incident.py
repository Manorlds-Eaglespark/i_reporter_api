import unittest
import json
from app.views import create_app
from app.data_store.data import incidents, incident5_data


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()

    def test_get_list_of_users(self):
        response = self.client.get('/api/v1/red-flags')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(type(data["data"])), "<class 'list'>")

    def test_get_an_incident(self):
        id = incidents[0].id
        response = self.client.get('/api/v1/red-flags/'+str(id))
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(type(data["data"])), "<class 'dict'>")
        self.assertEqual(data["data"]["location"], "0.215, 0.784")

    def test_get_an_incident_with_unknown_id(self):
        response = self.client.get('/api/v1/red-flags/'+str(1000010))
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["message"], "Resource not found with given id")

    def test_create_new_red_flag(self):
        response = self.client.post('/api/v1/red-flags', data=json.dumps(incident5_data),
                         content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data["message"], "Created red-flag record")
        self.assertEqual(str(type(data["data"])), "<class 'dict'>")

    def test_create_new_red_flag_no_creator_id(self):
        input_data = incident5_data
        input_data["created_by"] = ""
        response = self.client.post('/api/v1/red-flags', data=json.dumps(input_data),
                                    content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["message"], "created_by field required for user creating this redflag")
        self.assertEqual(str(type(data["data"])), "<class 'NoneType'>")
