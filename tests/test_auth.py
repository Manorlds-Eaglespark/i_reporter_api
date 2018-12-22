import unittest
import json
from app.views import create_app
from app.data_store.data import register_user

class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()

    def test_register_new_user(self):
        response = self.client.post(
            '/api/v1/auth/register', data=json.dumps(register_user), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('You registered successfully. Login to continue.', data['message'])

    def test_register_new_user_no_firstname(self):
        register_user["firstname"] = ""
        response = self.client.post(
            '/api/v1/auth/register', data=json.dumps(register_user), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertIn(
            'Make sure you fill all the required fields', data['message'])
