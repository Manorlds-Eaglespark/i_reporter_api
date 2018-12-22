import unittest
import json
from app.views import create_app
from app.data_store.data import register_user, user2_data, login_user

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

    def test_register_new_user_firstname_number(self):
        register_user["firstname"] = 45
        response = self.client.post(
            '/api/v1/auth/register', data=json.dumps(register_user), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertIn(
            'Make sure to strings use only ', data['message'])

    def test_register_new_user_firstname_space(self):
        register_user["firstname"] = " "
        response = self.client.post(
            '/api/v1/auth/register', data=json.dumps(register_user), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertIn(
            'Make sure to have no empty spaces in fields', data['message'])

    def test_register_new_user_short_password(self):
        register_user["firstname"] = "my first name"
        register_user["password"] = "5A"
        response = self.client.post(
            '/api/v1/auth/register', data=json.dumps(register_user), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertIn(
            'Make sure your password is at lest 4 letters', data['message'])

    def test_register_new_user_no_digit(self):
        register_user["firstname"] = "my first name"
        register_user["password"] = "sdfsds"
        response = self.client.post(
            '/api/v1/auth/register', data=json.dumps(register_user), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertIn(
            'Make sure your password has a number in it', data['message'])

    def test_register_new_user_no_capital_letter(self):
        register_user["firstname"] = "my first name"
        register_user["password"] = "sdf7sds"
        response = self.client.post(
            '/api/v1/auth/register', data=json.dumps(register_user), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertIn('Make sure your password has a capital letter in it', data['message'])

    def test_register_new_user_invalid_email(self):
        register_user["firstname"] = "my first name"
        register_user["email"] = "sdf7sds"
        response = self.client.post(
            '/api/v1/auth/register', data=json.dumps(register_user), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertIn(
            'Please enter a valid Email.', data['message'])

    def test_register_existing_user(self):
        response = self.client.post(
            '/api/v1/auth/register', data=json.dumps(user2_data), content_type='application/json')
        data = json.loads(response.data) 
        self.assertEqual(response.status_code, 400)
        self.assertIn(
            'That Email already is registered. Login or use a different Email to register.', data['message'])

    def test_login_user(self):
        response = self.client.post('/api/v1/auth/login', data=json.dumps(login_user),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('You logged in successfully.', data['message'])

    def test_login_user_email_space(self):
        login_user["email"] = " "
        response = self.client.post('/api/v1/auth/login', data=json.dumps(login_user),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('Provide an Email', data['message'])

    def test_login_user_no_email(self):
        login_user["email"] = ""
        response = self.client.post('/api/v1/auth/login', data=json.dumps(login_user),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('Provide an Email', data['message'])

    def test_login_user_number_email(self):
        login_user["email"] = 5
        response = self.client.post('/api/v1/auth/login', data=json.dumps(login_user),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('Type str required for email.', data['message'])

    def test_login_user_no_password(self):
        login_user["email"] = "bob.marley@gmail.com"
        login_user["password"] = ""
        response = self.client.post('/api/v1/auth/login', data=json.dumps(login_user),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('Provide a Password', data['message'])

    def test_login_user_wrong_password(self):
        login_user["email"] = "bob.marley@gmail.com"
        login_user["password"] = "afsQdas21"
        response = self.client.post('/api/v1/auth/login', data=json.dumps(login_user),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 401)
        data = json.loads(response.data)
        self.assertIn('Enter a correct Password', data['message'])

    def test_login_user_wrong_email(self):
        login_user["email"] = "bob.ley@gmail.com"
        login_user["password"] = "afsQdas21"
        response = self.client.post('/api/v1/auth/login', data=json.dumps(login_user),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 401)
        data = json.loads(response.data)
        self.assertIn('Email not registered on any account.', data['message'])
