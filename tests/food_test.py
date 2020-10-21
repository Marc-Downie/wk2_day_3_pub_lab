import unittest
from src.pub import Pub
from src.drinks import Drinks
from src.customer import Customer

class TestFood(unitest.TestCase):

    def setUp(self):
        self.food = Food("Kebab", 4, -3)
    
    # def test_food_has_name(self):
    #     self.assertEqual("Kebab", self.food.name)

    