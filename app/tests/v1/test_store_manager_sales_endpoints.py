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

if __name__ == '__main__':
    unittest.main(exit= False)
