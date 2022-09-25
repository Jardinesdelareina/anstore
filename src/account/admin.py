from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class AnstoreUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone', 'gender', 'created_at')

admin.site.register(AnstoreUser, AnstoreUserAdmin)
