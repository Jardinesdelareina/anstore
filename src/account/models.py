from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from .utils import get_path_upload_avatar, validate_size_avatar
from .managers import AnstoreUserManager


class AnstoreUser(AbstractUser):
    # Кастомная модель пользователя
    username = None
    GENDER = (
        ('male', 'Мужской'), 
        ('female', 'Женский')
    )
    email = models.EmailField('Электронная почта', unique=True)
    phone = models.CharField('Номер телефона', max_length=11, unique=True)
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=100)
    gender = models.CharField('Пол', max_length=7, choices=GENDER)
    avatar = models.ImageField(
        'Аватар', 
        upload_to=get_path_upload_avatar,
        blank=True, 
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg']), validate_size_avatar]
    )
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
