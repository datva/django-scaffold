from django.urls import path
from .views import ListOrdersView, AddOrderView, UserView, ListMedicinesView, AddMedicineView, OrderView

urlpatterns = [
    path('orders/', ListOrdersView.as_view(), name="orders-all"),
    path('user/', UserView.as_view(), name="user"),
    #path('order/', AddOrderView),
    path('order/', OrderView.as_view()),
    #path('medicines/', ListMedicinesView.as_view(), name = "medicines-all"),
    path('medicine/', AddMedicineView)

]

