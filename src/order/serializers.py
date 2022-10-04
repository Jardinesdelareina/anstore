from rest_framework import serializers
from ..product.serializers import ProductSerializer
from .models import Order, OrderDetails


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # Информация, недоступная для изменения пользователем
    order_number = serializers.CharField(read_only=True)
    order_status = serializers.CharField(read_only=True)
    order_time = serializers.CharField(read_only=True)

    def generate_order_number(self):
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
        return order_number

    def validate(self, attrs):
        attrs['order_number'] = self.generate_order_number()
        return attrs

    class Meta:
        model = Order
        fields = ('__all__')


class OrderDetailsSerializers(serializers.ModelSerializer):
    products = ProductSerializer(many=False)
    model = OrderDetails
    fields = ('__all__')