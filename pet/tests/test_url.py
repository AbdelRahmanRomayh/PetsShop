from django.test import TestCase
from django.urls import reverse, resolve
from pet.views import DogBreedView,BreedCategoryView

class TestPetUrls(TestCase):
    def test_breed_category_url(self):
        url = reverse('breed_category')
        self.assertEqual(resolve(url).func.view_class, BreedCategoryView)

    def test_dog_breed_url(self):
            url = reverse('dog_breed')
            self.assertEqual(resolve(url).func.view_class, DogBreedView)