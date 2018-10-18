import unittest
from .api.v1.views import app
import json



#remember to change the urls for these methods
class TestProductApis(unittest.TestCase):
    '''tests all the endpoints created for the store manager application'''
     def setUp(self):
        self.app = app.test_client()

     def test_get_admin_products(self):
        '''Tests the get (view all) products method, asserts true if the test passes and gives a status code of 200'''
        response = self.app.get('/admin/products')
        self.assertEqual(response.status_code, 200)

     def test_get_attendant_products(self):
        '''Tests the get (view all) products method for the attendant, asserts true if the test passes and gives a status code of 200'''
        response = self.app.get('/attendant/products')
        self.assertEqual(response.status_code, 200)

    def test_post_products(self):
        '''Tests whether the admin can create a new product successfully; (POST method); asserts true if the test passes and gives a status code of 201'''
        datapoint = {"name" : "hp", "description" : "elite", "category" : "computers", "price" : 50000}
        response = self.app.post('http://localhost:50931/admin/products', data = json.dumps(datapoint), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)

    def test_single_product(self):
        '''Tests for the get function to view a single product'''
        datapoint ={"name" : "hp", "description" : "elite", "category" : "computers", "price" : 50000}
        response = self.app.post('http://localhost:50931/admin/products', data = json.dumps(datapoint), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
        response = self.app.get('http://localhost:50931/products/1')
        self.assertEqual(response.status_code, 200)

    

if __name__ == '__main__':
    unittest.main(exit= False)
