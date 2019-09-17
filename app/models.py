from django.db import models

class Orders(models.Model):
    #email = models.TextField()
    order_id = models.CharField(max_length = 15)
    user_id = models.CharField(max_length = 15)
    admin_id = models.CharField(max_length = 15)
    order_time = models.DateTimeField(auto_now = True) # Set default time to now
    delivered_time = models.DateTimeField(auto_now = True)
    est_delivery_time = models.DateTimeField(auto_now = True)
    is_upload = models.BooleanField(default = False)
    photo_url = models.TextField(blank = True)
    status = models.CharField(default = "pending", max_length = 10)
    total_price = models.IntegerField(default = 0)


class User(models.Model):

    user_id = models.CharField(max_length = 15)
    email_id = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    phone_no = models.IntegerField(default = 0)
    address = models.TextField()


class Admin(models.Model):

    admin_id = models.CharField(max_length = 15)
    name = models.CharField(max_length = 50)
    phone_no = models.IntegerField(default = 0)
    shop_name = models.CharField(max_length = 50)
    address = models.TextField()


class Medicine(models.Model):

    med_id = models.CharField(max_length = 15, blank = True)
    med_name = models.CharField(max_length = 50)
    qty = models.IntegerField(default = 0)
    is_available = models.BooleanField(default = False)
    order_id = models.CharField(max_length = 15)

class ChatLine(models.Model):

    line_id = models.CharField(max_length = 15, blank = True)
    order_id = models.CharField(max_length = 15)
    line_text = models.TextField()
    writer_id = models.CharField(max_length = 15)
    timestamp = models.DateTimeField(auto_now = True)






