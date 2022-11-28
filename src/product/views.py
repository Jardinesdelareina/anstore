from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework import permissions, filters
from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category


class ProductViewSet(ModelViewSet):
    # Вывод товара
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(available=True).select_related('category')
    lookup_field = 'slug'


class SearchProductList(ListAPIView):
    # Вывод результатов поиска
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title',]


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
        queryset = category.product.filter(available=True)
        return queryset
