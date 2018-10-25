import re;


class Validators():
    '''contains validator methods that ensure the input entered is correct'''
    def product_validator(self, name, description, category, quantity, price):
        '''validates the inputs for the post products methods'''
        if name, description, category == '':
            return {'message': 'name,description or category fields cannot be empty'}
        elif not isinstance((quantity, category), int):
            return{'message':'quantity and price must be integers'}
        elif not isinstance((name, description, category), str):
            return {'message':'name,description or category fields must be strings'}
        else:
            return True




        
