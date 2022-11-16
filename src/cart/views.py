from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .serializers import CartSerializer, CartDetailSerializer
from .models import Cart


class CartViewSet(ModelViewSet):
    # Вывод корзины пользователя
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'products_id'

    def get_serializer_class(self):
        if self.action == 'list':
            return CartDetailSerializer
        else:
            return CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
