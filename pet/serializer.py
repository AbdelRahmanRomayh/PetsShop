
from rest_framework import serializers
from rest_framework.fields import CharField, IntegerField
from pet.models import BreedCategory,Dog

class BreedCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BreedCategory
        fields = '__all__'

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = '__all__'

class UpdateDogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = '__all__'

    age = serializers.IntegerField(required=False)
    gender = serializers.CharField(required=False)

class GetDogBreedSerializer(serializers.Serializer):
    breed_id = serializers.IntegerField()

class CreateDogBreedSerilaizer(serializers.Serializer):
    breed_id = serializers.IntegerField()
    age = serializers.IntegerField()
    is_vacinated = serializers.BooleanField()
    gender = serializers.CharField()