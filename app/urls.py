from django.urls import path
from .views import ListOrdersView


urlpatterns = [
    path('orders/', ListOrdersView.as_view(), name="orders-all")
]
