from django.db import models
from django.contrib.auth.models import User



class Product(models.Model):
    user_id=models.CharField(max_length=255, default="")
    name=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=50, decimal_places=2, default=0)
    quantity=models.IntegerField(default=1)
    description=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
class Payment(models.Model):
    user=models.CharField(max_length=255, unique=True)
    amount=models.DecimalField(max_digits=10, decimal_places=2)
