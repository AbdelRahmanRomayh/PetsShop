from django.db import models
from pet.models import Dog
from datetime import datetime

class Order(models.Model):
    price = models.PositiveIntegerField(null=False)
    currency = models.CharField(max_length=255,null=False)
    dog = models.OneToOneField(Dog,on_delete=models.CASCADE,related_name="purchase_order")
    purchase_date = models.DateTimeField(auto_now=datetime.now())

    def __str__(self):
        return f"Dog Breed: {self.dog.breed}, Price: {self.price}, Purchase Date: {self.purchase_date}"