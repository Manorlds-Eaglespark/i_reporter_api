import unittest
import json
from app.views import create_app
from app.data_store.data import incidents, incident5_data_dictionary, incident1_data_dictionary, incident2_data_dictionary, incident6_data_dictionary, incident3_data_dictionary, new_location, new_comment


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()

    def test_get_list_of_users(self):
        response = self.client.get('/api/v1/red-flags')
        data = json.loads(response.data)
        self.assertEqual(data["status"], 200)

    def test_get_an_incident(self):
        id = incidents[0].id
        response = self.client.get('/api/v1/red-flags/'+str(id))
        data = json.loads(response.data)
        self.assertEqual(data["status"], 200)
        self.assertEqual(data["data"][0]["location"], "0.215, 0.784")

    def test_get_an_incident_with_unknown_id(self):
        response = self.client.get('/api/v1/red-flags/'+str(1000010))
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["error"], "Resource not found.")

    def test_create_new_red_flag(self):
        response = self.client.post('/api/v1/red-flags', data=json.dumps(incident6_data_dictionary),
                                    content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(data["status"], 201)
        self.assertEqual(data["data"][0]["message"], "Created red-flag record")

    def test_create_new_red_flag_already_saved(self):
        response = self.client.post('/api/v1/red-flags', data=json.dumps(incident6_data_dictionary),
                                    content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(data["status"], 400)
        self.assertEqual(data["error"], "a similar resource already exists.")

    def test_create_new_red_flag_no_creator_id(self):
        input_data = incident5_data_dictionary
        input_data["created_by"] = ""
        response = self.client.post('/api/v1/red-flags', data=json.dumps(input_data),
                                    content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(data["status"], 400)
        self.assertEqual(
            data["error"], "created_by field should be of type int")

    def test_create_new_red_flag_string_creator_id(self):
        input_data = incident5_data_dictionary
        input_data["created_by"] = "fsadfas"
        response = self.client.post('/api/v1/red-flags', data=json.dumps(input_data),
                                    content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(data["status"], 400)
        self.assertEqual(
            data["error"], "created_by field should be of type int")

    def test_create_new_red_flag_no_doc_type(self):
        input_data = incident1_data_dictionary
        input_data["type"] = ""
        response = self.client.post('/api/v1/red-flags', data=json.dumps(input_data),
                                    content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(data["status"], 400)
        self.assertEqual(
            data["error"], "Type should be of type string: Either 'red-flag' or 'intervation'")

    def test_create_new_red_flag_other_doc_type(self):
        input_data = incident1_data_dictionary
        input_data["type"] = "redd_flag"
        response = self.client.post('/api/v1/red-flags', data=json.dumps(input_data),
                                    content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(data["status"], 400)
        self.assertEqual(
            data["error"], "Valid status required. Status should be of type string")

    def test_create_new_red_flag_no_location(self):
        input_data = incident2_data_dictionary
        input_data["location"] = ""
        response = self.client.post('/api/v1/red-flags', data=json.dumps(input_data),
                                    content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(data["status"], 400)
        self.assertEqual(
            data["error"], "Valid location required. Location should be of type string")

    def test_create_new_red_flag_no_comment(self):
        input_data = incident3_data_dictionary
        input_data["comment"] = ""
        response = self.client.post('/api/v1/red-flags', data=json.dumps(input_data),
                                    content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(data["status"], 400)
        self.assertEqual(data["error"], "Valid comment required. Comment should be of type string")

    def test_update_red_flag_location(self):
        id = incidents[1].id
        response = self.client.patch('/api/v1/red-flags/'+str(id)+'/location', data=json.dumps(new_location),
                                    content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(data["status"], 200)
        self.assertEqual(data["data"][0]["message"], "Updated red-flag record’s location")

    def test_update_red_flag_location_id_not_found(self):
        id = 15155200
        response = self.client.patch('/api/v1/red-flags/'+str(id)+'/location', data=json.dumps(new_location),
                                     content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(data["status"], 404)
        self.assertEqual(data["error"], "Resource not found.")

    def test_update_red_flag_comment(self):
        id = incidents[1].id
        response = self.client.patch('/api/v1/red-flags/'+str(id)+'/comment', data=json.dumps(new_comment),
                                     content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(data["status"], 200)
        self.assertEqual(
            data["data"][0]["message"], "Updated red-flag record’s comment")

    def test_update_red_flag_comment_id_not_found(self):
        id = 15155200
        response = self.client.patch('/api/v1/red-flags/'+str(id)+'/comment', data=json.dumps(new_comment),
                                     content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(data["status"], 404)
        self.assertEqual(
            data["error"], "Resource not found.")

    def test_delete_red_flag_given_id(self):
        id = incidents[3].id
        response = self.client.delete('/api/v1/red-flags/'+str(id))
        data = json.loads(response.data)
        self.assertEqual(data["status"], 200)
        self.assertEqual(data["data"][0]["message"], "red-flag record has been deleted")

    def test_create_new_red_flag_no_image(self):
        input_data = incident3_data_dictionary
        input_data["images"] = " "
        
        response = self.client.post('/api/v1/red-flags', data=json.dumps(input_data),
                                    content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(data["status"], 400)
        self.assertEqual(
            data["error"], "Valid images link required. Images should be of type string")
  
    def test_create_new_red_flag_no_video(self):
        input_data = incident3_data_dictionary
        input_data["status"] = "sfdfdas"
        input_data["images"] = "sdafsdsad"
        input_data["videos"] = " "
        response = self.client.post('/api/v1/red-flags', data=json.dumps(input_data),
                                    content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(data["status"], 400)
        self.assertEqual(
            data["error"], "Valid video link required. Vidoes should be of type string")

    def test_create_new_red_flag_no_status(self):
        input_data = incident3_data_dictionary
        input_data["status"] = " "
        response = self.client.post('/api/v1/red-flags', data=json.dumps(input_data),
                                    content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(data["status"], 400)
        self.assertEqual(
            data["error"], "Valid status required. Status should be of type string")
