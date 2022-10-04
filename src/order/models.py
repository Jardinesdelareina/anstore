from django.db import models
from ..account.models import AnstoreUser


class Order(models.Model):
    # Модель информации о заказе
    STATUS = (
        ('SUCCESS', 'Успех'),
        ('TIMEOUT', 'Закрытие по таймауту'),
        ('CREATED_PAY', 'Создание транзакции'),
        ('FINISHED', 'Окончание транзакции'),
        ('PAID', 'Оплачивается'),
    )
    user = models.ForeignKey(AnstoreUser, on_delete=models.CASCADE)
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
        return self.order_number
