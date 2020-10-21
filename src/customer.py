class Customer:
    def __init__(self, name, wallet, age, drunkeness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkeness = drunkeness

    def buy_drink(self, drinks):
        self.wallet -=  drinks.price

    def add_drink_units(self, drinks):
        self.drunkeness += drinks.units