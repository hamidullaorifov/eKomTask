from django.test import TestCase
from tinydb import TinyDB,Query

data = [
    {
        "name" : "UserForm",
        "user_email" : "email",
        "user_phone" : "phone",
        "birth_day" : "date",
    },
    {
        "name" : "CustomerForm",
        "customer_phone" : "phone",
        "description" : "text",
         "birth_day": "date"
    },
    {
        "name" : "OrderForm",
        "customer_phone" : "text",
        "order_date" : "date"
    },


]

class FormTestCase(TestCase):  
    def setUp(self):
        db = TinyDB('db.json')
        for item in data:
            if not db.search(Query().fragment(item)):
                db.insert(item)

    def test_response_status(self):
        data = {'user_email':'example@example.com'}
        response = self.client.post('/get_form/',data=data)
        self.assertEqual(response.status_code,200)


    def test_valid_phone_field(self):
        data = {'user_phone':'+7 222 325 45 54'}
        response = self.client.post('/get_form/',data=data)
        self.assertEqual(response.status_code,200)
        resp_data = response.json()
        self.assertEqual(resp_data,"UserForm")
    
    def test_valid_date_phone_fields(self):
        data = {
            'customer_phone':'+7 222 325 45 54',
            'birth_day':'01.12.2022'
        }
        response = self.client.post('/get_form/',data=data)
        self.assertEqual(response.status_code,200)
        resp_data = response.json()
        self.assertEqual(resp_data,"CustomerForm")
    
    def test_invalid_phone_field(self):
        data = {'customer_phone':'+7 222 325 45 5455'}
        response = self.client.post('/get_form/',data=data)
        self.assertEqual(response.status_code,200)
        resp_data = response.json()
        self.assertEqual(resp_data,"OrderForm")


    def test_nonexist_fields(self):
        data = {
            'user_phone':'+7 222 325 45 54',
            'nonexist_field':'test@gmail.com'
        }
        response = self.client.post('/get_form/',data=data)
        self.assertEqual(response.status_code,200)
        resp_data = response.json()
        self.assertDictEqual(resp_data,{'user_phone':'phone','nonexist_field':'email'})

    