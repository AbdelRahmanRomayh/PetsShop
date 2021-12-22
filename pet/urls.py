from django.urls import path
from pet.views import BreedCategoryView,DogBreedView
urlpatterns = [
    path('breed_category/',BreedCategoryView.as_view(),name="breed_category"),
    path('dog_breed/',DogBreedView.as_view(),name="dog_breed"),
]
