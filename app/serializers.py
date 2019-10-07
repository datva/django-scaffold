from rest_framework import serializers
from .models import Orders, User, Medicine, FileUpload, ChatLine, Admin, AdminOrders



class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = "__all__"


class OrdersSerializer(serializers.ModelSerializer):

    #medicines = MedicineSerializer(many = True)
    class Meta:
        model = Orders
        # fields = (
        #     "order_id"
        #     #"medicines"
        #     )
        fields = "__all__"

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

class AdminPageSerializer(serializers.ModelSerializer):
    current_orders = OrdersSerializer(many=True, read_only=True)
    recent_orders = OrdersSerializer(many=True, read_only=True)

    class Meta:
        model = AdminOrders
        fields = ('current_orders', 'recent_orders')

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


            
        # for ingredient in ingredients_data:
        #     ingredient, created = Ingredient.objects.get_or_create(name=ingredient['name'])
        #     recipe.ingredients.add(ingredient)

        return admin_orders


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




