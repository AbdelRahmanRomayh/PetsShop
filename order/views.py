from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from order.serializer import OrderSeralizer
from order import errors
from utils.error_handling import api_error_handling

@api_view(["POST"])
def create_order(request):
    order_serialzier = OrderSeralizer(data = request.data)
    if order_serialzier.is_valid():
        try:
            order_serialzier.save()
            error = api_error_handling(errors.Order_created)
            return Response(data={
                "data": order_serialzier.data,
                "error": error,
                },status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(data= {"error":e},status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(data= order_serialzier.errors,status=status.HTTP_400_BAD_REQUEST)

