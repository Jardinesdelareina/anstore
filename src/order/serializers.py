from rest_framework import serializers
from ..product.serializers import ProductSerializer
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    # Сериализация информации о товаре в заказе
    product = ProductSerializer(many=False, read_only=True)
    class Meta:
        model = OrderItem
        fields = (
            'id',
            'product',
            'amount',
            'total_price',
        )


class OrderSerializer(serializers.ModelSerializer):
    # Сериализация информации о заказе
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    #order_number = serializers.SerializerMethodField()
    order_status = serializers.CharField(read_only=True)
    order_time = serializers.CharField(read_only=True)
    order_items = OrderItemSerializer(many=True, read_only=True)

    """ def get_order_number(self):
        # Создание номера заказа
        # Текущее время + id пользователя + рандомное число
        from time import strftime
        from random import Random

        random_number = Random()
        order_number = '{time_now}{user_id}{random_int}'.format(
            time_now=strftime('%Y%m%d%H%M%S'),
            user_id=self.context['request'].user.id,
            random_int=random_number.randint(10, 99)
        )
        return str(order_number) """

    class Meta:
        model = Order
        fields = (
            'id',
            'user',
            'order_status',
            'order_comment',
            'order_time',
            'order_items',
            'to_pay',
            'signer_firstname',
            'signer_lastname',
            'signer_address',
            'signer_phone',
        )


class OrderListSerializer(serializers.ModelSerializer):
    # Сериализация нформации о заказах в списке
    #order_number = serializers.CharField(read_only=True)
    order_status = serializers.CharField(read_only=True)
    order_time = serializers.CharField(read_only=True)
    class Meta:
        model = Order
        fields = (
            'id',
            'order_time',
            'order_status',
            'to_pay',
        )
