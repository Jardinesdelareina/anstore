from rest_framework.viewsets import ModelViewSet
from .serializers import *


class ProductListView(ModelViewSet):
    # Список товаров
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()


class ProductView(ModelViewSet):
    # Конкретный товар, который есть в наличии
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(available=True)


class CategoryListView(ModelViewSet):
    # Список категорий товаров
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()


class CategoryProductListView(ModelViewSet):
    # Список товаров по категориям
    serializer_class = CategoryProductListSerializer
    queryset = Product.objects.all().select_related('category')
