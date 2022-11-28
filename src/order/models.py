from django.db import models
from django.conf import settings
from ..product.models import Product


class Order(models.Model):
    # Модель информации о заказе
    STATUS = (
        ('SUCCESS', 'Успех'),
        ('TIMEOUT', 'Закрытие по таймауту'),
        ('CREATED_PAY', 'Создание транзакции'),
        ('FINISHED', 'Окончание транзакции'),
        ('PAID', 'Оплачивается'),
    )
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    order_number = models.PositiveIntegerField('Номер заказа', unique=True)
    order_status = models.CharField('Статус заказа', choices=STATUS, default='PAID', max_length=11)
    order_description = models.CharField('Описание заказа', max_length=1000)
    order_price = models.FloatField('Сумма к оплате', default=0.0)
    order_time = models.DateTimeField('Время заказа', auto_now_add=True)

    signer_firstname = models.CharField('Фамилия заказчика', max_length=50)
    signer_lastname = models.CharField('Имя заказчика', max_length=50)
    signer_address = models.CharField('Адрес доставки', default='', max_length=500)
    signer_phone = models.CharField('Контактный телефон', max_length=11)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-order_time']

    def __str__(self):
        return str(self.order_number)


class OrderDetails(models.Model):
    # Модель деталей заказа
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='order_product')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    amount = models.PositiveIntegerField('Количество', default=0)
    adding_time = models.DateTimeField('Время добавления', auto_now_add=True)

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказа'

    def __str__(self):
        return str(self.order.order_number)
