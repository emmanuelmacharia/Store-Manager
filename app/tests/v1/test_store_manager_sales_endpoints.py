import unittest
from .api.v1.views import app
import json

#remember to change the urls for these methods
class TestProductApis(unittest.TestCase):
    '''tests all the endpoints created for the store manager application'''
     def setUp(self):
        self.app = app.test_client()

    def test_get_admin_sales(self):
        '''Tests the get (view all) sales method for the admin, asserts true if the test passes and gives a status code of 200'''
        response = self.app.get('http://localhost:50931/admin/sales')
        self.assertEqual(response.status_code, 200)

    def test_get_attendant_sales(self):
        '''Tests the get (view all) sales method by the attendant for the attendant, assets true if the test passes and gives the status code of 200'''
        response = self.app.get('http://localhost:50931/attendant/sales')
        self.assertEqual(response.status_code, 200)

    def test_single_sale_found(self):
        '''Tests whether the sale with the id provided is there, returns status_code 404'''
        newsale = {'saleid':1, 'product': 'Hp', 'quantity': 1, 'price': 5000}
        response = self.app.post('http://localhost:50931/attendant/sales', data = json.dumps(newsale), content_type = 'application/json')
        response = self.app.get('http://localhost:50931/admin/sales/1')
        self.assertEqual(response.status_code, 200)


    def test_post_sales(self):
        '''Tests whether the attendant can successfully create a new sale record (POST method); asserts true if the test passes and status code = 201'''
        newsale = {'productname': 'Hp', 'description':'elite x', 'quantity': 1, 'price': 5000}
        response = self.app.post('http://localhost:50931/attendant/sales', data = json.dumps(newsale), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)







if __name__ == '__main__':
    unittest.main(exit= False)
