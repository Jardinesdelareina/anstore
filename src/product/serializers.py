from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    # Категории товаров
    class Meta:
        model = Category
        fields = '__all__'
        lookup_field = 'slug'


class ProductSerializer(serializers.ModelSerializer):
    # Товар
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = '__all__'
        lookup_field = 'slug'
