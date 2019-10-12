from rest_framework import serializers
from django.db import models
import uuid
from .models import Orders, User, Medicine, FileUpload, ChatLine, Admin



class MedicineSerializer(serializers.ModelSerializer):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Medicine
        fields = (
            "id",
            "med_name",
            "qty",
            "is_available",
            "order_id"
            )
        read_only_fields = ("order_id",)


class OrdersSerializer(serializers.ModelSerializer):

    medicines = MedicineSerializer(many = True)
    class Meta:
        model = Orders
        fields = (
            "status",
            "medicines",
            "user_id",
            "order_id"
            )
        #fields = ('medicines',)
        #fields = "__all__"

    # def create(self, validated_data):
    #     medicine_dict = validated_data['medicines']
    #     order = Orders.objects.create(**validated_data)
    #     medicine_dict['order'] = order
    #     Medicine.objects.create(**medicine_dict)
    #     return order
    def create(self, validated_data):
        medicines = validated_data.pop('medicines')
        order = Orders.objects.create(**validated_data)
        for med in medicines:
            Medicine.objects.create(**med, order_id = order)
        return order
    # def create(self, validated_data):
    #     medicines = validated_data.pop('medicines')
    #     med_ord = Orders.objects.create(**validated_data)

    #     for med in medicines:
    #         med, created = Orders.objects.get_or_create(status='pending')
    #         admin_orders.current_orders.add(curr_ord)


    #     for rec_ord in recent_orders:
    #         rec_ord, created = Orders.objects.get_or_create(status='delivered')
    #         admin_orders.recent_orders.add(rec_ord)

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
"""
class AdminPageSerializer(serializers.ModelSerializer):
    current_orders = OrdersSerializer(many=True)
    recent_orders = OrdersSerializer(many=True)
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Orders
        fields = ('current_orders', 'recent_orders', 'id',)
    
    def create(self, validated_data):
        current_orders = validated_data.pop('current_orders')
        recent_orders = validated_data.pop('recent_orders')
        admin_orders = AdminOrders.objects.create(**validated_data)

        for curr_ord in current_orders:
            curr_ord, created = Orders.objects.get_or_create(status='pending')
            admin_orders.current_orders.add(curr_ord)


        for rec_ord in recent_orders:
            rec_ord, created = Orders.objects.get_or_create(status='delivered')
            admin_orders.recent_orders.add(rec_ord)

        return admin_orders
""" 

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


# class MedicineSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MedicineSerializer
#         fields = "__all__"


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = "__all__"




