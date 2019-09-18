from rest_framework import serializers
from .models import Orders, User, Medicine,FileUpload


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ("order_id", "user_id", "admin_id", "order_time", "delivered_time", "est_delivery_time",
            "is_upload", "photo_url", "status", "total_price")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("user_id", "email_id", "name", "phone_no", "address")

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = ("med_id", "med_name", "qty", "is_available", "order_id")




class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = "__all__"

