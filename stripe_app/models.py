from django.db import models
from django.contrib.auth.models import User



class Product(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=50, decimal_places=2, default=0)
    quantity=models.IntegerField(default=1)
    description=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
