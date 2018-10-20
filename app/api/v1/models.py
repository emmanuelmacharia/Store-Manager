from flask import Flask, jsonify, request
#from flask_jwt import JWT, jwt_required, current_identity
import re



users = {}
class User:
    '''Endpoint for user authentication'''
    def __init__(self, username,email, password):
        self.username = username
        self.email  = email
        self.password = password
        self.userid = len(users)+1

    def register(self):
        '''registers a new user'''

        payload = {'userid' : self.userid, 'username' : self.username, 'email' : self.email, 'passowrd' : self.password}
        users[self.userid] = payload

        #return jsonify({'userid': self.userid, 'username':self.username, 'email':self.email, 'passowrd': self.password, }), 201


    def single_user(self, email):
        '''Finds a single user, if not found, should return 404'''
        for key in User.users:
            #if key == self.userid
            if key == self.email:
                return users[self.email]
            else:
                return 'No User by that email, please register first'