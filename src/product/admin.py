from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'available', 'created_at')
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    list_display = ('title',)
    mptt_level_indent = 5
    prepopulated_fields = {'slug': ('title',)}
