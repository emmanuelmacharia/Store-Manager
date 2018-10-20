from flask import Flask, request, jsonify, make_response
from flask_restful import Api, Resource
from .models import User, users
import re;

#from flask_jwt import JWT, jwt_required


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


class Register(Resource):
    '''Endpoint for registation of a new user'''
    def post(self):
        '''creates a new user'''

        data = request.get_json()
        userid = data['userid']
        username = data['username']
        email = data['email']
        password = User.generate_hash(data['password'])

        new_user = {'userid' : userid, 'username' : username, 'email' :email, 'password' : password}

       
        if username == '' :
            return {'message':'Username cannot be null'}, 401
        #elif re.match ('[a-zA-Z0-9.-]+@[(a-z|A-Z)-]+\.(com|net)', email) is not True:
        #    return {'message':'user must have a valid email'},401
        elif len(password)<6 and re.search('[a-zA-Z0-9]+', password) is not True:
            return {'message':'user must have a valid password(at least 6 characters, with lowercase,uppercase and integers)'},401
        #users[userid] = new_user

        #requester = User.single_user(email)
        #if requester == 'Not found':
        #    requester = User(username, email, password)
        #    requester.register()
            
        return {'new user': new_user}, 201

#class Login(Resource):
#    '''Endpoint for logging in'''
#    def post(self):
#        '''Endpoint for posting login information'''
#        data = request.get_json()
#        username = data['username']
#        email = data['email']
#        password = User.generate_hash(data['password'])
        
#        for user in users:
#            if user["username"] == username:
#                if User.verify_hash
