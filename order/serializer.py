from django.db.models import fields
from rest_framework import serializers
from order.models import Order

class OrderSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'