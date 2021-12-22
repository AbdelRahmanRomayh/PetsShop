from django.test import TestCase,Client
from django.urls import reverse, resolve
from pet.views import DogBreedView,BreedCategoryView
from pet.models import Dog,BreedCategory
from rest_framework import status

class TestPetUrls(TestCase):
    def setUp(self):
        self.client = Client()
        self.dog_breed_url = reverse('dog_breed')
        self.breed_category_url = reverse('breed_category')

    def test_breed_category_GET_not_found(self):
        response = self.client.get(self.breed_category_url)
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)

    def test_breed_category_GET_found(self):
        BreedCategory.objects.create(
            name = "Rot"
        )
        response = self.client.get(self.breed_category_url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_breed_category_POST_success_add_new_breed(self):
        response = self.client.post(self.breed_category_url,{"name":"Rot"})
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_breed_category_POST_faliure_add_new_breed(self):
        response = self.client.post(self.breed_category_url,{"diffent_name":"Rot"})
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        response = self.client.post(self.breed_category_url,{})
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

    def test_dog_breed_GET_breed(self):
        breed = BreedCategory.objects.create(name="Rot")
        Dog.objects.create(age=1,gender="M",breed=breed)
        response = self.client.get(self.dog_breed_url+ "?breed_id=1")
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_dog_breed_GET_no_breed_id(self):
        response = self.client.get(self.dog_breed_url)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

    def test_dog_breed_GET_no_breed(self):
        response = self.client.get(self.dog_breed_url+ "?breed_id=1")
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)

    def test_dog_breed_POST_with_breed_id(self):
        breed = BreedCategory.objects.create(name="Rot")
        response = self.client.post(self.dog_breed_url,{
            "age":1,"gender":"M","is_vaccinated":False,"breed":1
        })
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_dog_breed_POST_with_wrong_breed_id(self):
        breed = BreedCategory.objects.create(name="Rot")
        response = self.client.post(self.dog_breed_url,{
            "age":1,"gender":"M","is_vaccinated":False,"breed":2
        })
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)  
        

    def test_dog_breed_PUT_with_dog_id(self):
        breed_1 = BreedCategory.objects.create(name="Rot")
        breed_2 = BreedCategory.objects.create(name="Husky")
        Dog.objects.create(age=1,gender="M",breed=breed_1)
        response = self.client.put(self.dog_breed_url,{"dog_id":1,"age": 1,"gender":"M","is_vaccinated":False},'application/json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_dog_breed_PUT_without_dog_id(self):
        breed_1 = BreedCategory.objects.create(name="Rot")
        breed_2 = BreedCategory.objects.create(name="Husky")
        Dog.objects.create(age=1,gender="M",breed=breed_1)
        response = self.client.put(self.dog_breed_url,{"age": 1,"gender":"M","is_vaccinated":False},'application/json')
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

    def test_dog_breed_PUT_with_wrong_dog_id(self):
        breed_1 = BreedCategory.objects.create(name="Rot")
        breed_2 = BreedCategory.objects.create(name="Husky")
        Dog.objects.create(age=1,gender="M",breed=breed_1)
        response = self.client.put(self.dog_breed_url,{"dog_id":3,"age": 1,"gender":"M","is_vaccinated":False},'application/json')
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)  


    def test_dog_breed_DELETE_with_dog_id(self):
        breed_1 = BreedCategory.objects.create(name="Rot")
        Dog.objects.create(age=1,gender="M",breed=breed_1)
        response = self.client.delete(self.dog_breed_url,{"dog_id":1},'application/json')
        self.assertEqual(response.status_code,status.HTTP_200_OK) 


    def test_dog_breed_DELETE_without_dog_id(self):
        breed_1 = BreedCategory.objects.create(name="Rot")
        Dog.objects.create(age=1,gender="M",breed=breed_1)
        response = self.client.delete(self.dog_breed_url,{},'application/json')
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST) 


    def test_dog_breed_DELETE_with_wrong_dog_id(self):
        breed_1 = BreedCategory.objects.create(name="Rot")
        Dog.objects.create(age=1,gender="M",breed=breed_1)
        response = self.client.delete(self.dog_breed_url,{"dog_id":3},'application/json')
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)  