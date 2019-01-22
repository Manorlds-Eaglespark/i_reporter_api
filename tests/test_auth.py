import unittest
import json
from app.views import create_app
from app.databases.database import Database
from tests.data_test import *


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.database = Database()
        self.database.create_all_tables()

    def test_register_new_user(self):
        response = self.client.post(
            '/api/v1/auth/register', data=json.dumps(register_user), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(data["status"], 201)
    
    def tearDown(self):
        self.database.delete_all_tables()


   
