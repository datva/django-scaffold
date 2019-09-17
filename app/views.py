from rest_framework import generics
from .models import Orders
from .serializers import OrdersSerializer


class ListOrdersView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

# Create your views here.
