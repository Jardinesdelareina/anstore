from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    # Сериализация категорий товаров
    class Meta:
        model = Category
        fields = '__all__'
        lookup_field = 'slug'


class ProductSerializer(serializers.ModelSerializer):
    # Сериализация информации о товаре
    category = CategorySerializer()
    price = serializers.FloatField(read_only=True)
    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'slug',
            'image',
            'description',
            'price',
            'available',
            'created_at',
            'category',
        )
        lookup_field = 'slug'
