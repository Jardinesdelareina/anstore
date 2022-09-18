from django.db import models
from django.contrib.auth.models import AbstractUser


class AnstoreUser(AbstractUser):
    # Модель кастомного пользователя
    GENDER = (
        ('male', 'Мужской'), 
        ('female', 'Женский')
    )
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=7, choices=GENDER, default='male')
    phone = models.CharField(max_length=14)
    avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True)

    def __str__(self):
        return self.username
