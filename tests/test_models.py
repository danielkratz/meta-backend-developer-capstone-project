from django.test import TestCase
from restaurant.models import Menu 

class MenuTest(TestCase):
    def test_menu_representation(self):
        menu_item = Menu.objects.create(Title="Ice cream", Price=5, Inventory=100)
        expected_representation = "Ice cream : 5"

        # Calling the assertEqual method to compare the string representation
        self.assertEqual(str(menu_item), expected_representation)
