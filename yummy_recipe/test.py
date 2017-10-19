import unittest
from tabledef import Recipe, Recipecategory

class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.first_recipecategory = Recipecategory('Indian')
        self.first_recipe = Recipe('Naan', 'Cook it', self.first_recipecategory)

    def test_subclass(self):
        self.assertTrue(issubclass(Recipe, Recipecategory), msg="Not True Subclass")

    
