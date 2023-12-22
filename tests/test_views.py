from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(Title="Garlic mushrooms", Price=10, Inventory=50)
        Menu.objects.create(Title="super duper dish", Price=15.5, Inventory=30)
        Menu.objects.create(Title="Dessert", Price=20, Inventory=20)

    def test_getall(self):
        url = reverse('menu-list')
        client = APIClient()
        response = client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)
