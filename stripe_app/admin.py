from django.contrib import admin
from .models import Product, Payment
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=("id","name","price", "quantity", "created_at")

@admin.register(Payment)
class ProductAdmin(admin.ModelAdmin):
    list_display=("user", "amount")