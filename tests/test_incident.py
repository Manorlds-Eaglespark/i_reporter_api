import unittest
import json
from app.views import create_app
from app.data_store.data import incidents, incident5_data, incident1_data, incident2_data, incident3_data, new_location, new_comment


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
        self.assertEqual(
            data["message"], "created_by field required for user creating this redflag")
        self.assertEqual(str(type(data["data"])), "<class 'NoneType'>")

    def test_create_new_red_flag_string_creator_id(self):
        input_data = incident5_data
        input_data["created_by"] = "fsadfas"
        response = self.client.post('/api/v1/red-flags', data=json.dumps(input_data),
                                    content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            data["message"], "created_by should be of type int.")
        self.assertEqual(str(type(data["data"])), "<class 'NoneType'>")

    def test_create_new_red_flag_no_doc_type(self):
        input_data = incident1_data
        input_data["doc_type"] = ""
        response = self.client.post('/api/v1/red-flags', data=json.dumps(input_data),
                                    content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            data["message"], "doc_type should either be red-flag or intervation. You entered: ")
        self.assertEqual(str(type(data["data"])), "<class 'NoneType'>")

    def test_create_new_red_flag_other_doc_type(self):
        input_data = incident1_data
        input_data["doc_type"] = "redd_flag"
        response = self.client.post('/api/v1/red-flags', data=json.dumps(input_data),
                                    content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            data["message"], "doc_type should either be red-flag or intervation. You entered: redd_flag")
        self.assertEqual(str(type(data["data"])), "<class 'NoneType'>")

    def test_create_new_red_flag_no_location(self):
        input_data = incident2_data
        input_data["location"] = ""
        response = self.client.post('/api/v1/red-flags', data=json.dumps(input_data),
                                    content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            data["message"], "Location field required.")
        self.assertEqual(str(type(data["data"])), "<class 'NoneType'>")

    def test_create_new_red_flag_no_comment(self):
        input_data = incident3_data
        input_data["comment"] = ""
        response = self.client.post('/api/v1/red-flags', data=json.dumps(input_data),
                                    content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            data["message"], "Make sure you filled these required fields: Status, images, videos and comment")
        self.assertEqual(str(type(data["data"])), "<class 'NoneType'>")

    def test_update_red_flag_location(self):
        id = incidents[1].id
        response = self.client.patch('/api/v1/red-flags/'+str(id)+'/location', data=json.dumps(new_location),
                                    content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            data["message"], "Updated red-flag record’s location")
        self.assertEqual(str(type(data["data"])), "<class 'dict'>")

    def test_update_red_flag_location_id_not_found(self):
        id = 15155200
        response = self.client.patch('/api/v1/red-flags/'+str(id)+'/location', data=json.dumps(new_location),
                                     content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            data["message"], "Red-flag not found")
        self.assertEqual(str(type(data["data"])), "<class 'NoneType'>")

    def test_update_red_flag_comment(self):
        id = incidents[1].id
        response = self.client.patch('/api/v1/red-flags/'+str(id)+'/comment', data=json.dumps(new_comment),
                                     content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            data["message"], "Updated red-flag record’s comment")
        self.assertEqual(str(type(data["data"])), "<class 'dict'>")

    def test_update_red_flag_comment_id_not_found(self):
        id = 15155200
        response = self.client.patch('/api/v1/red-flags/'+str(id)+'/comment', data=json.dumps(new_comment),
                                     content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            data["message"], "Resource with that id not found")
        self.assertEqual(str(type(data["data"])), "<class 'NoneType'>")

    def test_delete_red_flag_given_id(self):
        id = incidents[3].id
        response = self.client.delete('/api/v1/red-flags/'+str(id))
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            data["message"], "red-flag record has been deleted")
        self.assertEqual(str(type(data["data"])), "<class 'NoneType'>")
