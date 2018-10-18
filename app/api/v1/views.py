from flask import Flask, request, jsonify, make_response
from flask_restful import Api, Resource

app  = Flask(__name__)
api = Api(app)


products = {}

class AdminProducts(Resource):
    '''Endpoints for creating and viewing products in the application'''

    def get(self):
        '''Views all the products in the application'''
        return jsonify({'products':products})

    def post(self):
        '''Creates a new product in the store'''
        can_post = True
        if can_post:
            id = len(products)+1
            data = request.get_json()
            name = data['name']
            description = data['description']
            category = data['category']
            price = data['price']

            payload = {'name': name, 'description': description, 'category': category, 'price': price}

            products[id] = payload

            return products, 201
        return 'User not allowed to create a product'


class Product(Resource):
    '''Endpoint that allows a user to view a single product'''

    def get(self, id):
        '''view a single product'''
        if id in products:
            return products[id], 200
        return 'Not found', 404
        
