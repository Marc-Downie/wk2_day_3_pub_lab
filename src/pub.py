class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.check = False
    
    def increase_till(self, drinks):
        self.till += drinks.price
    
    def check_age(self, customer):
        #check the customers age 
        #check they are at least 18
        #update self.check so it returns True
        if customer.age >= 18:
            self.check = True
    