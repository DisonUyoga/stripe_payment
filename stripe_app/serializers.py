from rest_framework import serializers
from .models import Product, Payment


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=(
            "id",
            "name",
            "price",
            "description",
            "quantity"
        )
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields=(
            "id",
            "amount",
            "user"
        )