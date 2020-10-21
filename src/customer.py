class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age

    def buy_drink(self, drinks):
        #reduce customer  wallet
        #buy price of drink
        self.wallet -=  drinks.price