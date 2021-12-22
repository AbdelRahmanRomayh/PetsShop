from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from pet.models import Dog,BreedCategory
from pet.serializer import BreedCategorySerializer,DogSerializer,GetDogBreedSerializer,UpdateDogSerializer
from pet import errors
from utils.error_handling import api_error_handling


class BreedCategoryView(APIView):
    def get(self, request):
        breed = BreedCategory.objects.all()
        if breed.count() == 0:
            error = api_error_handling(errors.no_breedcategory_found)
            status_code = status.HTTP_404_NOT_FOUND
        else:
            error = api_error_handling(errors.success_code)
            status_code = status.HTTP_200_OK

        breed_serializer = BreedCategorySerializer(breed, many=True)
        return Response(data={
            "data": breed_serializer.data,
            "error": error,
        },
        status=status_code)

    def post(self, request):
        breed_serializer = BreedCategorySerializer(data=request.data)
        if breed_serializer.is_valid():
            breed_serializer.save()
            error = api_error_handling(errors.success_code)
            return Response(data={
            "data": breed_serializer.data,
            "error": error,
            },
            status=status.HTTP_201_CREATED)
        else:
             return Response(breed_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DogBreedView(APIView):
    def get(self, request):
        breed_id  = request.GET.get("breed_id",None)
        if breed_id is not None and int(breed_id):
            dogs = Dog.objects.filter(breed_id = breed_id)
            if dogs.count() == 0:
                error = api_error_handling(errors.no_dog_found)
                status_code = status.HTTP_404_NOT_FOUND
            else:
                error = api_error_handling(errors.success_code)
                status_code = status.HTTP_200_OK

            dog_serializer = DogSerializer(dogs, many=True)
            return Response(data={
                "data": dog_serializer.data,
                "error": error,
            },
            status=status_code)
        else:
            error = api_error_handling(errors.breed_id_not_provided)
            return Response({"error":error}, status=status.HTTP_400_BAD_REQUEST)

    def post(self,request):
        dog_breed_serialzier = DogSerializer(data=request.data)
        if dog_breed_serialzier.is_valid():
            try:
                dog_breed_serialzier.save()
                error = api_error_handling(errors.success_code)
                return Response(data={
                    "data": dog_breed_serialzier.data,
                    "error": error,
                    },status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response(data= {"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
        else:
             return Response(dog_breed_serialzier.errors, status=status.HTTP_400_BAD_REQUEST)
        # dog_breed_serialzier = CreateDogBreedSerilaizer(data=request.data)
        # if dog_breed_serialzier.is_valid():
        #     breed_id = request.data["breed_id"]
        #     age = request.data["age"]
        #     gender = request.data["gender"]
        #     is_vaccinated = request.data["is_vaccinated"]
        #     try:
        #         dog_object = Dog.objects.create(breed_id=breed_id,aga=age,gender=gender,is_vaccinated=is_vaccinated)
        #         dog_serializer  = CreateDogBreedSerilaizer(data = dog_object)
        #         error = api_error_handling(errors.success_code)
        #         return Response(data={
        #         "data": dog_serializer.data,
        #         "error": error,
        #         },status=status.HTTP_201_CREATED)
        #     except Exception as e:
        #         return Response(data = {"error": e}, status=status.HTTP_400_BAD_REQUEST)
        # else:
        #      return Response(dog_breed_serialzier.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request):
        dog_id = request.data.get("dog_id",None)
        if dog_id is not None:
            try:
                dog_instance = Dog.objects.get(id=dog_id)
            except:
                error = api_error_handling(errors.no_dog_found_with_provided_id)
                return Response(data = {"error": error}, status=status.HTTP_404_NOT_FOUND)
            dog_serialzier = UpdateDogSerializer(instance=dog_instance,data=request.data)
            if dog_serialzier.is_valid():
                try:
                    dog_serialzier.save()
                    error = api_error_handling(errors.success_code)
                    return Response(data={
                    "data": dog_serialzier.data,
                    "error": error,
                    },status=status.HTTP_201_CREATED)
                except Exception as e:
                    error = dog_serialzier.errors
                    return Response(data={
                    "data": dog_serialzier.data,
                    "error": str(e),
                    },status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(dog_serialzier.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            error=api_error_handling(errors.success_code)
            return Response({"error":error}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request):
        dog_id = request.data.get("dog_id",None)
        if dog_id is not None:  # get only one object details
            try:
                Dog.objects.get(id=dog_id).delete()
            except Exception as e:
                error = api_error_handling(errors.delete_item_error)
                return Response(
                    data={
                        "error": error
                    }, status=status.HTTP_404_NOT_FOUND)
            error = api_error_handling(errors.success_code)
            api_status = status.HTTP_200_OK
        else:
            error = api_error_handling(errors.dog_id_not_provided)
            api_status = status.HTTP_400_BAD_REQUEST
        return Response(
            data={
                "error": error
            }, status=api_status)

