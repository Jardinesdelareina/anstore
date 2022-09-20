from rest_framework.viewsets import ModelViewSet
from .serializers import *


class ProductView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(available=True)
    lookup_field = 'slug'


class CategoryView(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    