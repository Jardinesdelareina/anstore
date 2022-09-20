from django.contrib import admin
from .models import *


class AnstoreUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone', 'gender', 'birthday')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

admin.site.register(AnstoreUser, AnstoreUserAdmin)
