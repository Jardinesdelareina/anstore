from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, parsers
from ..cart.models import Cart
from .models import Order, OrderDetail
from .serializers import OrderSerializer, OrderDetailSerializer


class OrderView(ModelViewSet):
    # Вывод информации о заказе
    parser_classes = (parsers.MultiPartParser,)
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user.id)

    def get_serializer_class(self):
        if self.action == 'list':
            return OrderSerializer
        else:
            return OrderDetailSerializer

    def perform_create(self, serializer):
        order = serializer.save()
        carts = Cart.objects.filter(user=self.request.user.id)
        for cart in carts:
            order_products = OrderDetail()
            order_products.product = cart.product
            order_products.amount = cart.amount
            order_products.total_price = cart.total_price
            order_products.order = order
            order_products.save()
            cart.delete()
        return order

    def perform_destroy(self, serializer):
        cart = serializer.save()
        orders = OrderDetail.objects.filter(user=self.request.user.id)
        for order in orders:
            cart_products = Cart()
            cart_products.product = order.product
            cart_products.amount = order.amount
            cart_products.total_price = order.total_price
            cart_products.order = order
            cart_products.save()
            order.delete()
        return cart
