from rest_framework.viewsets import ModelViewSet
from .serializers import *


class ProductListView(ModelViewSet):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()


class ProductView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(available=True)


class CategoryProductListView(ModelViewSet):
    serializer_class = CategoryProductListSerializer
    queryset = Category.objects.all()
