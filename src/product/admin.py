from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'available')
    prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)
