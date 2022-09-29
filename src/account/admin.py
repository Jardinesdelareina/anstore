from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import AnstoreUser


@admin.register(AnstoreUser)
class AnstoreUserAdmin(UserAdmin):
    list_display = ('id', 'email', 'phone', 'gender', 'birthday', 'is_active')
    list_display_links = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'phone')}),
        (_('Personal info'), {'fields': ('last_name', 'first_name', 'gender', 'birthday', 'avatar')}),
        (_('Permissions'), {'fields': ('is_staff', 'is_active')}),
    )
    search_fields = ('email',)
    ordering = ('email',)
