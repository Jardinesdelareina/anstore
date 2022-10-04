from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from ..cart.models import Cart
from .models import Order, OrderDetails
from .serializers import OrderDetailsSerializer, OrderSerializer


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return OrderDetailsSerializer
        return OrderSerializer

    def perform_create(self, serializer):
        order = serializer.save()
        carts = Cart.objects.filter(user=self.request.user)
        for cart in carts:
            order_products = OrderDetails()
            order_products.product = cart.product
            order_products.amount = cart.amount
            order_products.order = order
            order_products.save()
            cart.delete()
        return order
