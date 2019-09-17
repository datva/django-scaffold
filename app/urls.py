from django.urls import path
from .views import ListOrdersView, AddOrderView, UserView, ListMedicinesView, AddMedicineView

urlpatterns = [
    path('orders/', ListOrdersView.as_view(), name="orders-all"),
    path('user/', UserView.as_view(), name="user"),
    path('order/', AddOrderView),
    path('medicines/', ListMedicinesView.as_view(), name = "medicines-all"),
    path('medicine/', AddMedicineView)

]
