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
            '/api/v2/auth/signup', data=json.dumps(register_user), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(data["status"], 201)

    def test_register_new_user_no_firstname(self):
        register_user["firstname"] = ""
        response = self.client.post(
            '/api/v2/auth/signup', data=json.dumps(register_user), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(data["status"], 400)
        self.assertIn(
            data['error'],
            'Make sure you fill all the required fields')

    def test_register_new_user_firstname_number(self):
        register_user["firstname"] = 45
        response = self.client.post(
            '/api/v2/auth/signup', data=json.dumps(register_user), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 406)
        self.assertIn(data['error'], 'Make sure to strings use only ')

    def test_register_new_user_firstname_space(self):
        register_user["firstname"] = " "
        response = self.client.post(
            '/api/v2/auth/signup', data=json.dumps(register_user), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 406)
        self.assertIn(
            data['error'],
            'Make sure to use the English alphabert in the fields')

    def test_register_new_user_short_password(self):
        register_user["firstname"] = "my first name"
        register_user["password"] = "5A"
        response = self.client.post(
            '/api/v2/auth/signup', data=json.dumps(register_user), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 406)
        self.assertIn(
            data['error'],
            'Make sure your password has atlest 4 letters')

    def test_register_new_user_no_digit(self):
        register_user["firstname"] = "my first name"
        register_user["password"] = "sdfsds"
        response = self.client.post(
            '/api/v2/auth/signup', data=json.dumps(register_user), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(data["status"], 406)
        self.assertIn(
            data['error'],
            'Make sure your password has a number in it')

    def test_register_new_user_no_capital_letter(self):
        register_user["firstname"] = "my first name"
        register_user["password"] = "sdf7sds"
        response = self.client.post(
            '/api/v2/auth/signup', data=json.dumps(register_user), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(data["status"], 406)
        self.assertIn(
            data['error'],
            'Make sure your password has a capital letter in it')

    def test_register_new_user_invalid_email(self):
        register_user["firstname"] = "my first name"
        register_user["email"] = "sdf7sds"
        response = self.client.post(
            '/api/v2/auth/signup', data=json.dumps(register_user), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(data["status"], 406)
        self.assertIn(data['error'], 'Please enter a valid Email.')

    def test_register_existing_user(self):
        self.client.post(
            '/api/v2/auth/signup', data=json.dumps(register_user), content_type='application/json')
        response = self.client.post(
            '/api/v2/auth/signup', data=json.dumps(register_user), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(data["status"], 401)
        self.assertIn(
            data['error'],
            'That Email is already taken.')

    def test_login_user(self):
        self.client.post(
            '/api/v2/auth/signup', data=json.dumps(register_user), content_type='application/json')
        response = self.client.post('/api/v2/auth/login', data=json.dumps(login_user),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_login_user_email_space(self):
        login_user["email"] = " "
        response = self.client.post('/api/v2/auth/login', data=json.dumps(login_user),
                                    content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(data["status"], 406)
        self.assertIn(data['error'], 'Provide an Email')

    def test_login_user_no_email(self):
        login_user["email"] = ""
        response = self.client.post('/api/v2/auth/login', data=json.dumps(login_user),
                                    content_type='application/json')

        data = json.loads(response.data)
        self.assertEqual(data["status"], 406)
        self.assertIn(data['error'], 'Provide an Email')

    def test_login_user_number_email(self):
        login_user["email"] = 5
        response = self.client.post('/api/v2/auth/login', data=json.dumps(login_user),
                                    content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(data['status'], 406)
        self.assertIn(data['error'], 'Type str required for email.')

    def test_login_user_no_password(self):
        login_user["email"] = "bob.marley@gmail.com"
        login_user["password"] = ""
        response = self.client.post('/api/v2/auth/login', data=json.dumps(login_user),
                                    content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(data["status"], 406)
        self.assertIn(data["error"], 'Provide a Password')

    def test_login_user_wrong_password(self):
        register_user["email"] = "bob_marley@gmail.com"
        self.client.post(
            '/api/v2/auth/signup', data=json.dumps(register_user), content_type='application/json')
        login_user["email"] = "bob_marley@gmail.com"
        login_user["password"] = "afsQdas21"
        response = self.client.post('/api/v2/auth/login', data=json.dumps(login_user),
                                    content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(data["status"], 401)
        self.assertIn(data["error"], 'Enter a correct Password')

    def test_login_user_wrong_email(self):
        login_user["email"] = "bob.ley@gmail.com"
        login_user["password"] = "afsdfas2A1"
        response = self.client.post('/api/v2/auth/login', data=json.dumps(login_user),
                                    content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(data["status"], 401)
        self.assertIn(data['error'], 'Email not registered on any account.')

    def tearDown(self):
        self.database.delete_all_tables()
