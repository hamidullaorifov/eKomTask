from django.test import TestCase


class FormTestCase(TestCase):  

    def test_response_status(self):
        data = {'my_email':'example@example.com'}
        response = self.client.post('/get_form/',data=data)
        self.assertEqual(response.status_code,200)
    def test_exist_phone_field(self):
        data = {'finish_field':'+7 222 325 45 54'}
        response = self.client.post('/get_form/',data=data)
        self.assertEqual(response.status_code,200)
        resp_data = response.json()
        self.assertListEqual(resp_data,["friendForm","theyForm"])
    def test_exist_date_phone_fields(self):
        data = {
            'view_field':'+7 222 325 45 54',
            'across_field':'01.12.2022'
        }
        response = self.client.post('/get_form/',data=data)
        self.assertEqual(response.status_code,200)
        resp_data = response.json()
        self.assertListEqual(resp_data,["ratherForm"])
    def test_nonexist_fields(self):
        data = {
            'type_field':'+7 222 325 45 54',
            'nonexist_field':'test@gmail.com'
        }
        response = self.client.post('/get_form/',data=data)
        self.assertEqual(response.status_code,200)
        resp_data = response.json()
        self.assertDictEqual(resp_data,{'type_field':'telephone','nonexist_field':'email'})

        

