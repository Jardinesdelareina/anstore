from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import AnstoreUserManager


class AnstoreUser(AbstractUser):
    # Кастомная модель пользователя
    username = None
    email = models.EmailField('Электронная почта', unique=True)
    phone = models.CharField('Номер телефона', max_length=11, unique=True)
    birthday = models.DateField('День рождения', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AnstoreUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-date_joined']
