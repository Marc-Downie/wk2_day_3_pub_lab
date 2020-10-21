import unittest
from src.drinks import Drinks

class TestDrinks(unittest.TestCase):

    def setUp(self):
        self.drinks = Drinks("Lager", 2.50, 2)

    def test_drink_has_name(self):
        self.assertEqual("Lager", self.drinks.name)