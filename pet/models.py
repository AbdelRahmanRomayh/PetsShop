from django.db import models

class BreedCategory(models.Model):
    name = models.CharField(max_length=255,null=False,unique=True)

    def __str__(self):
        return self.name

class Dog(models.Model):
    gender_choices = ("M","male"),("F","female")
    age = models.IntegerField(null=False)
    is_vaccinated = models.BooleanField(null=False,default=True)
    gender = models.CharField(max_length=20,choices=gender_choices,null=False)
    breed = models.ForeignKey(BreedCategory,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return f"id: {self.id}, Breed: {self.breed}, Age: {self.age}"

    def breed_count(self,breed_id):
        breed_counter = Dog.objects.filter(breed_id=breed_id).count()
        return breed_counter