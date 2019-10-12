from django.urls import path,include
from django.urls import path, include
from .views import (
    UserView,
    ListMedicinesView,
    AddMedicineView,
    AdminOrderView,
    UserOrderView,
    SingleOrderView,
    ChatView,
    SignupView,
    LoginView
)
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router = routers.DefaultRouter()


urlpatterns = [
    path('user/', UserView.as_view(), name="user"),
    path('admin/order/', AdminOrderView.as_view()),
    path('user/order/', UserOrderView.as_view()),
    path('admin/order/', AdminOrderView.as_view()),
    path('order/', SingleOrderView.as_view()),
    path('medicine/', AddMedicineView),

    #path('chat/', ChatView.as_view())
    # path('upload/', upload_file, name="upload")
    path('chat/', ChatView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("signup/", SignupView.as_view()),
    path("login/", LoginView.as_view())
       
]
