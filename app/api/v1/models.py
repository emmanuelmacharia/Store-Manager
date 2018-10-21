from flask import Flask, jsonify, request
from passlib.hash import pbkdf2_sha256 as sha256
import re



users = {}
class User:
    '''models for the users who have registered'''
    def register(username, email, password):
        '''registers a new user'''
        userid = len(users)+1
        payload = {'username' : username, 'email' : email, 'password' : password}
        users[userid] = payload
        return users[userid]



    def single_user(email):
        '''Finds a single user, if not found, should return 404'''
        for key in users:
            for key in users[key]:
                if key == 'email':
                    if email == users[userid]['email']:
                        result = users[userid]
                else:
                    return 'Not found'

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)

    # def signin(self, username, email, password):
    #     for
