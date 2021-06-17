from django.db import models


class order(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    amount = models.IntegerField(max_length=100)
    order_id = models.IntegerField(max_length=100)
