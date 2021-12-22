import re
from django.test import TestCase,Client
from django.urls import reverse
from pet.models import Dog,BreedCategory
from order.models import Order
from rest_framework import status

class TestOrderViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.create_order_url = reverse('create_order')

    def test_create_order_POST_new_order(self):
        breed_1 = BreedCategory.objects.create(name="Rot")
        dog = Dog.objects.create(age=1,gender="M",breed=breed_1)
        response = self.client.post(self.create_order_url,{"price":200,"currency":"EGP","dog":dog.id})
        self.assertEqual(response.status_code,status.HTTP_201_CREATED) 

    def test_create_order_POST_dog_already_sold(self):
        breed_1 = BreedCategory.objects.create(name="Rot")
        dog = Dog.objects.create(age=1,gender="M",breed=breed_1)
        self.client.post(self.create_order_url,{"price":200,"currency":"EGP","dog":dog.id})
        response2 = self.client.post(self.create_order_url,{"price":200,"currency":"EGP","dog":dog.id})
        self.assertEqual(response2.status_code,status.HTTP_400_BAD_REQUEST) 