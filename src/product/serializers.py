from rest_framework import serializers
from .models import *


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'price', 'category')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('slug', 'image', 'description')


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title')


class CategoryProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('slug', 'image', 'description')
