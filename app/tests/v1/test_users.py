
import unittest
import json
from app import create_app




class TestUsersApi(unittest.TestCase):
    '''Tests all endpoints for users'''
    def setUp(self):
        self.app = create_app('testing').test_client()
        self.test_empty_username= {"username":"", "email":"user@inlook.com","password": "fdkff5A"}
        self.test_empty_email = {"username":"user", "email":"", "password": "fdkff5A"}
        self.test_empty_password = {"username":"user", "email":"solomarsha@outlook.com","password": ""}
        self.test_invalid_password = {"username":"user", "email":"solomarsha@outlook.com","password": "pass"}
        self.test_valid_input= {"username":"user", "email":"solomarsha@outlook.com","password": "pass1Word"}
        self.test_login_success = {"username":"user", "email":"solomarsha@outlook.com","password": "pass1Word"}


    def test_empty_username_registration_login(self):
        '''tests whether the username provided is an empty string, returns an error message'''
        #new_user = {"username":"", "email":"user@inlook.com","password": "fdkff5A"}
        response = self.app.post('api/v1/register', data = json.dumps(self.test_empty_username), content_type = 'application/json' )
        self.assertEqual(response.status_code, 406)

    def test_empty_email_registration_login(self):
        '''tests whether the username provided is an empty string, returns an error message'''
        #new_user = {"username":"user", "email":"", "password": "fdkff5A"}
        response = self.app.post('api/v1/register', data = json.dumps(self.test_empty_email), content_type = 'application/json' )
        self.assertEqual(response.status_code, 406)

    def test_empty_password_registration_login(self):
        '''tests whether the username provided is an empty string, returns an error message'''
        #new_user = {"username":"user", "email":"solomarsha@outlook.com","password": ""}
        response = self.app.post('api/v1/register', data = json.dumps(self.test_empty_password), content_type = 'application/json' )
        self.assertEqual(response.status_code, 406)

    def test_invalid_password_registration_login(self):
        '''tests whether the username provided is an empty string, returns an error message'''
        #new_user = {"username":"user", "email":"solomarsha@outlook.com","password": "pass"}
        response = self.app.post('api/v1/register', data = json.dumps(self.test_invalid_password), content_type = 'application/json' )
        self.assertEqual(response.status_code, 406)

    def test_register_success(self):
        '''tests whether the username, password and email provided are valid, returns 201'''
        response = self.app.post('api/v1/register', data = json.dumps(self.test_valid_input), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)

    def test_login_success(self):
        '''tests whether the input provided matches with an existing user, and returns 200 upon login success'''
        response = self.app.post('api/v1/login', data = json.dumps(self.test_login_success), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
