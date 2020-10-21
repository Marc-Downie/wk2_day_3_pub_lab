import unittest
from src.pub import Pub
from src.drinks import Drinks
from src.customer import Customer
from src.food import Food

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_increase_till(self):
        drinks = Drinks("Wine", 3.00, 1)
        self.pub.increase_till(drinks)
        self.assertEqual(103.00, self.pub.till)

    def test_customer_age__return_False(self):
        customer = Customer("Keith", 20.00, 17, 0)
        self.assertEqual(False, self.pub.check_age(customer))

    def test_customer_age__return_True(self):
        customer = Customer("Jane", 20.00, 19, 0)
        self.assertEqual(True, self.pub.check_age(customer))
    
    # def test_drink_transaction_True(self):
    #     customer = Customer("Jane", 20.00, 19, 0)
    #     drinks = Drinks("Wine", 3.00, 1)
    #     self.pub.drink_transaction(customer, drinks)
    #     self.assertEqual(17.00, customer.wallet)
    #     self.assertEqual(103.00, self.pub.till)
    
    def test_drink_transaction_True(self):
        customer = Customer("Jane", 20.00, 19, 0)
        drinks = Drinks("Wine", 3.00, 1)
        self.pub.drink_transaction(customer, drinks)
        self.assertEqual(17.00, customer.wallet)
        self.assertEqual(103.00, self.pub.till)
    
    def test_drink_transaction_False(self):
        customer = Customer("Bob", 20.00, 40, 11)
        drinks = Drinks("Wine", 3.00, 1)
        self.pub.drink_transaction(customer, drinks)
        self.assertEqual(20.00, customer.wallet)
        self.assertEqual(100.00, self.pub.till)

    def test_sober_enough__False(self):
        customer = Customer("Bob", 20.00, 40, 11)
        self.assertEqual(False, self.pub.sober_enough(customer))

    def test_sober_enough__True(self):
        customer = Customer("Jack", 20.00, 21, 8)
        self.assertEqual(True, self.pub.sober_enough(customer))