from rest_framework import serializers
from .models import Orders, User, Medicine, FileUpload, ChatLine


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = "__all__"


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


class ChatLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatLine
        fields = "__all__"
