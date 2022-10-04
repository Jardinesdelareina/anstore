from django.db import models
from ..account.models import AnstoreUser
from ..product.models import Product


class Cart(models.Model):
    # Модель корзины покупок пользователя
    user = models.ForeignKey(AnstoreUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    amount = models.PositiveIntegerField('Количество', default=0)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = verbose_name
        unique_together = ('user', 'product')

    def __str__(self):
        return '%s(%d)'.format(self.product.title, self.amount)
