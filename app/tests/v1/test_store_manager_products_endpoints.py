import unittest
from app import create_app
import json



#remember to change the urls for these methods
class TestProductApis(unittest.TestCase):
    '''tests all the endpoints created for the store manager application'''
    def setUp(self):
        self.app = create_app('testing').test_client()
        
    def test_get_admin_products(self):
        '''Tests the get (view all) products method, asserts true if the test passes and gives a status code of 200'''
        response = self.app.get('api/v1/admin/products')
        self.assertEqual(response.status_code, 200)

    def test_get_attendant_products(self):
        '''Tests the get (view all) products method for the attendant, asserts true if the test passes and gives a status code of 200'''
        response = self.app.get('api/v1/attendant/products')
        self.assertEqual(response.status_code, 200)

    def test_post_products(self):
        '''Tests whether the admin can create a new product successfully; (POST method); asserts true if the test passes and gives a status code of 201'''
        datapoint = {"name" : "hp", "description" : "elite", "category" : "computers", "quantity" : 10, "price" : 50000}
        response = self.app.post('api/v1/admin/products', data = json.dumps(datapoint), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)

    def test_single_product(self):
        '''Tests for the get function to view a single product'''
        datapoint ={"name" : "hp", "description" : "elite", "category" : "computers", "quantity" : 10, "price" : 50000}
        response = self.app.post('api/v1/admin/products', data = json.dumps(datapoint), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
        response = self.app.get('api/v1/products/1')
        self.assertEqual(response.status_code, 200)

    def test_no_product_found(self):
        '''Tests for non existent items'''
        response = self.app.get('api/v1/products/100')
        self.assertEqual(response.status_code, 404)

    

if __name__ == '__main__':
    unittest.main(exit= False)
