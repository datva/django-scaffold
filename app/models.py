import uuid
from django.db import models

#from django.contrib.auth.models import User

class User(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email_id = models.CharField(max_length=60, unique=True)
    password = models.CharField(max_length=60)
    name = models.CharField(max_length=36)
    phone_no = models.TextField()
    is_admin = models.BooleanField(default=False)
    address = models.TextField()


class Orders(models.Model):

    #order_id = models.CharField(max_length = 36, primary_key=True)
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #user_id = models.CharField(max_length = 36)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, db_column = "user_id")
    admin_id = models.CharField(max_length = 36)
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



class Admin(models.Model):

    admin_id = models.CharField(max_length=36, primary_key=True)
    name = models.CharField(max_length=50)
    phone_no = models.TextField()
    shop_name = models.CharField(max_length = 50)
    shop_address = models.TextField()



class Medicine(models.Model):

    med_id = models.CharField(max_length = 36, blank = True, primary_key=True)
    med_name = models.CharField(max_length = 50)
    qty = models.IntegerField(default = 0)
    is_available = models.BooleanField(default = False)
    order_id = models.CharField(max_length = 36)

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

    

