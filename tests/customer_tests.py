import unittest
from src.customer import Customer
from src.drinks import Drinks
from src.pub import Pub
from src.food import Food

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("Dave", 50.00, 30, 0)

    def test_customer_has_name(self):
        self.assertEqual("Dave", self.customer.name)
    
    def test_buy_drink(self):
        drink = Drinks("Wine", 3.00, 1)
        self.customer.buy_drink(drink)
        self.assertEqual(47.00, self.customer.wallet)

    def test_drink_units(self):
        drink = Drinks("Wine", 3.00, 1)
        self.customer.add_drink_units(drink)
        self.assertEqual(1, self.customer.drunkeness)
    
    def test_rejuvenation_level__True(self):
        customer = Customer("Bob", 20.00, 40, 11)
        food = Food("Kebab", 4, 3)
        customer.rejuvenation_level(food)
        self.assertEqual(8, customer.drunkeness)