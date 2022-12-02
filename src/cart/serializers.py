from rest_framework import serializers
from ..product.serializers import ProductSerializer
from ..product.models import Product
from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    # Сериализация информации о товаре в корзине
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    product = ProductSerializer(many=False, read_only=True)
    class Meta:
        model = Cart
        fields = (
            'id',
            'user',
            'product', 
            'amount',
            'total_price',
        )


class CartDetailSerializer(serializers.Serializer):
    # Сериализация корзины пользователя
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    product = serializers.PrimaryKeyRelatedField(required=True, queryset=Product.objects.all())
    amount = serializers.IntegerField(
        required=True, 
        label='Количество', 
        min_value=1,
        error_messages={
            'min_value': 'Количество товаров не может быть меньше одного', 
            'required': 'Пожалуйста, выберите количество покупок'
        }
    )
    class Meta:
        model = Cart
        fields = (
            'user',
            'product',
            'amount',
        )

    def create(self, validated_data):
        user = self.context['request'].user
        product = validated_data['product']
        amount = validated_data['amount']

        existed = Cart.objects.filter(user=user, product=product)

        # Определяет, есть ли в данный момент запись
        if existed:
            existed = existed[0]
            existed.amount += amount
            existed.save()
        else:
            existed = Cart.objects.create(**validated_data)
        return existed

    def update(self, instance, validated_data):
        # Изменить количество товара
        instance.amount = validated_data['amount']
        instance.save()
        return instance
