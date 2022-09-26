from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

@admin.register(AnstoreUser)
class AnstoreUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'phone', 'gender', 'created_at')
    list_display_links = ('username',)
