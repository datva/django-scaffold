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
