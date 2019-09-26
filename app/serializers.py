from rest_framework import serializers
from .models import Orders, User, Medicine, FileUpload, ChatLine



class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = "__all__"


class OrdersSerializer(serializers.ModelSerializer):

    medicines = MedicineSerializer(many = True)
    class Meta:
        model = Orders
        fields = (
            "order_id",
            "medicines"
            )

class UserSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of User objects."""

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ('email_id',  'name', 'phone_no', 'address' , 'password', 'token',)
        read_only_fields = ('token',)


    def update(self, instance, validated_data):
        
        password = validated_data.pop('password', None)

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance



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




