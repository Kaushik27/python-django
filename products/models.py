from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(blank=True)
    stock = models.IntegerField(blank=True)
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField(blank=True)
