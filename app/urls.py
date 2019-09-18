from django.urls import path,include
from .views import ListOrdersView, AddOrderView, UserView, ListMedicinesView, AddMedicineView, OrderView, upload_file
from rest_framework import routers
router = routers.DefaultRouter()




urlpatterns = [
    path('orders/', ListOrdersView.as_view(), name="orders-all"),
    path('user/', UserView.as_view(), name="user"),
    #path('order/', AddOrderView),
    path('order/', OrderView.as_view()),
    #path('medicines/', ListMedicinesView.as_view(), name = "medicines-all"),
    path('medicine/', AddMedicineView),
    path('upload/', upload_file, name="upload")
]




   
