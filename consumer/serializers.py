from rest_framework import serializers
from consumer.models import Product, Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'url', 'name', 'category', 'price', 'created_at', 'modified_at']


class OrderSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset= Product.objects.all(), many=False)
    class Meta:
        model = Order
        fields = ['url', 'id', 'session', 'product', 'quantity']