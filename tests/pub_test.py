import unittest
from src.pub import Pub
from src.drinks import Drinks
from src.customer import Customer

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_increase_till(self):
        drinks = Drinks("Wine", 3.00)
        self.pub.increase_till(drinks)
        self.assertEqual(103.00, self.pub.till)

    def test_customer_age__return_False(self):
        customer = Customer("Keith", 20.00, 17)
        self.pub.check_age(customer)
        self.assertEqual(False, self.pub.check)

    def test_customer_age__return_True(self):
        customer = Customer("Jane", 20.00, 19)
        self.pub.check_age(customer)
        self.assertEqual(True, self.pub.check)