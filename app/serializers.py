from rest_framework import serializers
from .models import Orders, User, Medicine, FileUpload, ChatLine, AuthenUser



class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = "__all__"


class OrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Orders
        fields = "__all__"
        depth = 1

class AuthenUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthenUser
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserSignupSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = "__all__"

class UserLoginSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ("email_id", "password")



class ChatLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatLine
        fields = "__all__"


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineSerializer
        fields = "__all__"


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = "__all__"




