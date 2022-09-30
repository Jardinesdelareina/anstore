from django.db import models
from django.urls import reverse


class Category(models.Model):
    # Модель категории товаров
    title = models.CharField('Категория', max_length=70, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)

    class Meta:
        ordering = ['title']
        index_together = (('id', 'slug'),)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Product(models.Model):
    # Модель товара
    title = models.CharField('Название', max_length=100, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    image = models.ImageField('Изображение', upload_to='product/image/', blank=True)
    description = models.TextField('Описание', max_length=1000, blank=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    available = models.BooleanField('Наличие', default=True)
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)
    updated_at = models.DateTimeField('Изменено', auto_now=True)
    category = models.ForeignKey(Category, related_name='product', on_delete=models.PROTECT)

    class Meta:
        ordering = ['-created_at']
        index_together = (('id', 'slug'),)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def get_absolute_url(self):
        return reverse('product', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
