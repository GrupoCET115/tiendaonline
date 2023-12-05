from rest_framework import serializers
from shop.models import Product, FeedbackShop


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name','description','price','slug']

class FeedbackShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackShop
        fields = ['usuario', 'mensaje', 'creado']