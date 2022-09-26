from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from .serializers import *


class ProductViewSet(ModelViewSet):
    # Вывод списка товаров
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(available=True).select_related('category')
    lookup_field = 'slug'


class CategoryViewSet(ModelViewSet):
    # Вывод списка категорий товаров
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryProductViewSet(ModelViewSet):
    # Вывод списка товаров определенной категории
    serializer_class = ProductSerializer
    lookup_field = 'slug'

    def get_queryset(self):   
        category = get_object_or_404(Category, slug__iexact=self.kwargs.get('slug'))
        queryset = category.product.all()
        return queryset
