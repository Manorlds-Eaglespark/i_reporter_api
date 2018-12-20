import unittest
import json
from app import create_app
from app.database.Database import Database
from tests.data import *
from app.models.Admin import Admin
from app.data_store.data import admin_login, admin_data


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.database = Database()
        self.database.create_all_tables()

    def test_get_all_red_flags(self):
        response = self.client.get('/api/v1/red-flags')
        self.assertEqual(response.status_code, 200)
