from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('image', 'description')


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'price', 'category')


class CategoryProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('image', 'description')
