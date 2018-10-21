from flask import Flask, jsonify, request
from passlib.hash import pbkdf2_sha256 as sha256
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

        payload = {'userid' : self.userid, 'username' : self.username, 'email' : self.email, 'password' : self.password}
        
        users[self.userid] = payload

        return {'userid': self.userid, 'username':self.username, 'email':self.email, 'passowrd': self.password}, 201


    def single_user(self):
        '''Finds a single user, if not found, should return 404'''
        for key in users:
            print(key)
            for key in users[self.userid]:
            #if key == self.userid
                print(key)
                print(self.email)
                if key == self.email:
                    print(key)
                    return users[email]
                else:
                    return 'Not found'

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)