import unittest
import json
from .views.api.v1.views import app


class TestProductApis(unittest.TestCase):
    '''Tests all the endpoints created in v1'''
    def setUp(self):
        '''instantiates flask's test_client'''
        self.app = app.test_client()

    def test_get_admin_products(self):
        '''Tests the get (view all) products method, asserts true if the test passes and gives a status code of 200'''
        response = self.app.get('/admin/products')
        self.assertEqual(response.status_code, 200)

    def test_get_attendant_products(self):
        '''Tests the get (view all) products method for the attendant, asserts true if the test passes and gives a status code of 200'''
         response = self.app.get('/attendant/products')
         self.assertEqual(response.status_code, 200)

    
