class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
    
    def increase_till(self, drinks):
        self.till += drinks.price
    
    def check_age(self, customer):
        #check the customers age 
        #check they are at least 18
        #update self.check so it returns True
        return customer.age >= 18 
    
    def drink_transaction(self, customer, drinks):
        if self.check_age(customer) is True:
            customer.buy_drink(drinks)
            self.increase_till(drinks)

    def sober_enough(self, customer):
        return customer.drunkeness <= 9
        #cut off at 9