from django.contrib import admin
from .models import Product, Payment, Customer
# Register your models here.


@admin.register(Payment)
class ProductAdmin(admin.ModelAdmin):
    list_display=("user", "amount", "customer_id")

@admin.register(Customer)
class ProductAdmin(admin.ModelAdmin):
    list_display=("user", "customer_id")