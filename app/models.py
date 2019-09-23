from django.db import models


class Orders(models.Model):

    order_id = models.CharField(max_length=36, primary_key=True)
    user_id = models.CharField(max_length=36)
    admin_id = models.CharField(max_length=36)
    order_time = models.DateTimeField(
        auto_now_add=True)  # Set default time to now
    delivered_time = models.DateTimeField(auto_now_add=True)
    est_delivery_time = models.DateTimeField(auto_now_add=True)
    is_upload = models.BooleanField(default=False)
    photo_url = models.TextField(blank=True)
    status = models.CharField(
        default="pending",
        max_length=10,
        choices=[
            ("pending",
             "PENDING"),
            ("rejected",
             "REJECTED"),
            ("approved",
             "APPROVED"),
            ("rejected",
             "REJECTED")])
    total_price = models.IntegerField(default=0)


class User(models.Model):

    user_id = models.CharField(max_length=36)
    password = models.CharField(max_length=40)
    email_id = models.CharField(max_length=36)
    name = models.CharField(max_length=36)
    phone_no = models.TextField()
    address = models.TextField()


class Admin(models.Model):

    admin_id = models.CharField(max_length=36)
    name = models.CharField(max_length=50)
    phone_no = models.TextField()
    shop_name = models.CharField(max_length=50)
    shop_address = models.TextField()


class Medicine(models.Model):

    med_id = models.CharField(max_length=36, blank=True)
    med_name = models.CharField(max_length=50)
    qty = models.IntegerField(default=0)
    is_available = models.BooleanField(default=False)
    order_id = models.CharField(max_length=36)


class ChatLine(models.Model):

    msg_id = models.CharField(max_length=36)
    order_id = models.CharField(max_length=36)
    line_text = models.TextField()
    src_id = models.CharField(max_length=36)
    timestamp = models.DateTimeField(auto_now_add=True)
    dest_id = models.CharField(max_length=36)


class FileUpload(models.Model):

    name = models.CharField(max_length=200)
    pic = models.FileField(blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
