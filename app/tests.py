from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Orders
from .serializers import OrdersSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_order(email=""):
        if email != "":
            Orders.objects.create(email=email)

    def setUp(self):
        # add test data
        self.create_order("angadsharma1016@gmail.com")

# Create your tests here.
