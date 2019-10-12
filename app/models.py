import uuid
import jwt

from datetime import datetime, timedelta

from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)

#from django.contrib.auth.models import User

class UserManager(BaseUserManager):
   

    def create_user(self, email_id, name, address, phone_no, password):

        user = self.model(email_id=email_id, password = password, address = address, phone_no = phone_no, name = name)
        user.set_password(password)
        user.save()

        return user

    
    def create_superuser(self, email_id, name, phone_no, address, password, username=None, email=None):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        print("username is ", username)
        print("email is ", email)
        print("password is ", password)

        user = self.create_user(email_id,name, address, phone_no, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    
    email_id = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=60)
    name = models.TextField()
    phone_no = models.TextField()
    address = models.TextField()
    # More fields required by Django when specifying a custom user model.

    # The `USERNAME_FIELD` property tells us which field we will use to log in.
    # In this case we want it to be the email field.
    USERNAME_FIELD = 'email_id'
    REQUIRED_FIELDS = ['password', 'name', 'phone_no', 'address']

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()

    def __str__(self):
        """
        Returns a string representation of this `User`.

        This string is used when a `User` is printed in the console.
        """
        return self.email_id

    @property
    def token(self):
        """
        Allows us to get a user's token by calling `user.token` instead of
        `user.generate_jwt_token().

        The `@property` decorator above makes this possible. `token` is called
        a "dynamic property".
        """
        return self._generate_jwt_token()


    def _generate_jwt_token(self):
        """
        Generates a JSON Web Token that stores this user's ID and has an expiry
        date set to 60 days into the future.
        """
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%S'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')



class Orders(models.Model):

    #order_id = models.CharField(max_length = 36, primary_key=True)
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #user_id = models.CharField(max_length = 36)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, db_column = "user_id")
    #admin_id = models.CharField(max_length = 36)
    order_time = models.DateTimeField(auto_now_add = True) # Set default time to now
    delivered_time = models.DateTimeField(auto_now_add = True) 
    est_delivery_time = models.DateTimeField(auto_now_add = True)
    is_upload = models.BooleanField(default = False)
    photo_url = models.TextField(blank = True)
    status = models.CharField(default = "pending", max_length = 10, choices = [("pending", "PENDING"), 
        ("rejected", "REJECTED")
        ,("approved", "APPROVED"), 
        ("delivered", "DELIVERED")])
    total_price = models.IntegerField(default = 0)
    @property
    def medicines(self):
        return self.medicine_set.all()
    

class Admin(models.Model):

    admin_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    phone_no = models.TextField()
    shop_name = models.TextField(blank = True)
    shop_address = models.TextField(blank = True)

# class AdminOrders(models.Model):
#     @property
#     def current_orders(self):
#         return self.orders_set.all()

#     @property
#     def recent_orders(self):
#         return self.orders_set.all()
#     #admin_name = models.TextField() 
#     #current_orders = models.ManyToManyField(Orders)
#     #recent_orders = models.ManyToManyField(Orders)



class Medicine(models.Model):

    #med_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    med_name = models.CharField(max_length = 50)
    qty = models.IntegerField(default = 0)
    is_available = models.BooleanField(default = False)
    order_id = models.ForeignKey(Orders, on_delete = models.CASCADE, db_column = "order_id")

class ChatLine(models.Model):

    msg_id = models.CharField(max_length = 36, primary_key=True)
    order_id = models.CharField(max_length = 36)
    line_text = models.TextField()
    src_id = models.CharField(max_length = 36)
    timestamp = models.DateTimeField(auto_now_add = True)
    dest_id = models.CharField(max_length = 36)

class FileUpload(models.Model):
    name = models.CharField(max_length=200)
    pic = models.FileField(blank=False, null=False)
    
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    

