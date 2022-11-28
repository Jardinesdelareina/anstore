from django.db import models
from django.conf import settings
from ..product.models import Product


class Cart(models.Model):
    # Модель корзины покупок пользователя
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='carts')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    amount = models.PositiveIntegerField('Количество', default=0)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = verbose_name
        unique_together = ('user', 'product')

    def __str__(self):
        return '%s(%d)'.format(self.product.title, self.amount)
