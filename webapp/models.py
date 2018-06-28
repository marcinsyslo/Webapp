from django.db import models


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=200)
    user_email = models.CharField(max_length=200)


class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField(max_length=10000)


class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    products = models.ManyToManyField(Product)
    price = models.FloatField(max_length=100000)
