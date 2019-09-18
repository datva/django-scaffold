from rest_framework import generics
from .models import Orders, User, Medicine
from .serializers import OrdersSerializer, UserSerializer, MedicineSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


class ListOrdersView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


class OrderView(generics.ListAPIView):

    """
    GET and POST orders at /order
    """

    def get(self, request):
        orders = Orders.objects.all()
        serializer_class = OrdersSerializer
        return Response({"orders": orders})

    def post(self, request):

        order = request.data.get('order')
        # Create an article from the above data
        serializer_class = OrdersSerializer(data=order)
        if serializer_class.is_valid(raise_exception=True):
            order_saved = serializer.save()
        return Response({"success": "Order '{}' created successfully"
            .format(order_saved.title)})




@api_view(['POST'])
def AddOrderView(request):

    serializer = OrdersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class UserView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ListMedicinesView(generics.ListAPIView):

    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

@api_view(['POST'])
def AddMedicineView(request):

    serializer = MedicineSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Create your views here.
