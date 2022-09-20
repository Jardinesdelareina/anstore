from rest_framework.viewsets import ModelViewSet
from .serializers import *


class ProductView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(available=True)


class CategoryView(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryProductView(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(category_id=self.kwargs['category_id'], available=True)\
            .select_related('category')
    
