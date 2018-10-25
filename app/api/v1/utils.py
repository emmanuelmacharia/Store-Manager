import re;


class Validators():
    '''contains validator methods that ensure the input entered is correct'''
    def product_validator(self, name, description, category, quantity, price):
    '''validates the inputs for the post products methods'''
        if name or description or category == '':
            return {'message': 'name,description or category fields cannot be empty'}
        elif isinstance((quantity, category), int) == False:
            return{'message':'quantity and price must be integers'}
        elif isinstance((name, description, category), str) == False:
            return {'message':'name,description or category fields must be strings'}
        else:
            return True

    def user_validator(self, username,email, password):
        '''validates the inputs for the register and login methods'''
        if username == '' or if not isinstance(username, str):
            return {'message':'Username cannot be null or a number'}, 400
        elif not re.search (r"(^[a-zA-Z0-9_.-]+@[a-zA-Z-]+\.[.a-zA-Z-]+$)", email):
             return {'message':'user must have a valid email'},400
        elif len(password)>6 and re.search('[a-zA-Z0-9]+', password) is not True:
            return {'message':'user must have a valid password(at least 6 characters, with lowercase, uppercase and integers)'}
