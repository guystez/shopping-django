from rest_framework import serializers
from .models import Product,Cart_new




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'



class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Cart_new
        fields = '__all__'

class CartSerializertwo(serializers.ModelSerializer):
    class Meta:
        model = Cart_new
        fields = '__all__'
        