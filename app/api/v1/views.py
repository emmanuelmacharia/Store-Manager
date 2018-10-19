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
            if len(data) > 5:
                return ('Can take only 5 arguments; name, description, category, quantity, price')
            elif 'name' and 'description' and 'category' and 'quantity' and 'price' not in data.keys():
                return ('Can take only these arguments; name, description, category, quantity, price')
            name = data['name']
            description = data['description']
            category = data['category']
            quantity = data['quantity']
            price = data['price']

            payload = {'name': name, 'description': description, 'category': category, 'quantity': quantity, 'price': price}

            products[id] = payload

            return products, 201

        return 'User not allowed to create a product'

class AttendantProducts(Resource):
    '''endpoints for viewing all the products in the inventory by the attendant'''

    def get(self):
        '''Views all the products in the application'''
        attendant_products = AdminProducts.get(self)
        return attendant_products

class Product(Resource):
    '''Endpoint that allows a user to view a single product'''

    def get(self, id):
        '''view a single product'''
        if id in products:
            return products[id], 200
        return 'Not found', 404


sales ={}

class AttendantSales(Resource):
    '''endpoint for creating and viewing sales'''
    def get(self):
        '''views all sales made by the attendant'''
        return jsonify({'sales':sales})

    def post(self):
        '''Creates a new sale by the attendant'''
        id = len(sales)+1
        data = request.get_json()
        productname = data['productname']
        price = data['price']
        quantity = data['quantity']
        description = data['description']
        
        payload = { 'productname': productname, 'description': description, 'quantity': quantity , 'price': price }

        sales[id] = payload

        return sales, 201


class AdminSale(Resource):
    '''Endpoints for viewing sales by Admin'''

    def get(self):
      '''views all sales made by the attendants'''
      allsales = AttendantSales.get(self)
      return allsales

class Sale(Resource):
    '''Endpoint for viewing a single sale'''
    def get(self, id):
        #'''views single sale'''
        if id not in sales.keys():
            return 'Not Found', 404
        else:
            return sales[id] ,200
