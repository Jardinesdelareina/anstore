from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    # Сериализация категорий товаров
    children = serializers.ListField(source='get_children', read_only=True, child=RecursiveField())
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'parent',
            'children',
            'slug',
        )
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
