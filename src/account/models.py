from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.core.validators import FileExtensionValidator
from .managers import AnstoreUserManager
from .services import validate_size_image

class AnstoreUser(AbstractBaseUser, PermissionsMixin):
    # Кастомная модель пользователя

    GENDER = (('male', 'Мужской'), ('female', 'Женский'))
    username = models.CharField(max_length=50, db_index=True, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    gender = models.CharField(max_length=7, choices=GENDER, default='male')
    phone = models.CharField(max_length=14)
    avatar = models.ImageField(
        upload_to='account/avatar/', 
        blank=True, 
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg']), validate_size_image]
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Определяет, какое поля используется для входа в систему
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = AnstoreUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-created_at']
