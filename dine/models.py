from django.db import models

class Food_info(models.Model):
    food_name = models.CharField(max_length=200)
    food_price = models.DecimalField(max_digits=5, decimal_places=2)
    food_imag = models.ImageField(upload_to='img', height_field=100, width_field=100)
    food_type = models.CharField(max_length=30)
    food_sold_num = models.IntegerField(default=0)
    food_left_num = models.IntegerField()

class Drinks_info(models.Model):
    drink_name = models.CharField(max_length=100)
    drink_price = models.DecimalField(max_digits=5, decimal_places=2)
   # drink_img = models.ImageField()

class user_info(models.Model):
    user_name = models.CharField(max_length=200)
    user_pwd = models.CharField(max_length=200)
    user_phone = models.CharField(max_length=200)
    user_address = models.CharField(max_length=200)
   # user_img = models.ImageField()
class Order(models.Model):
    order_price = models.FloatField()
    order_name = models.CharField(max_length=200)