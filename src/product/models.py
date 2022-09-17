from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=70, db_index=True)
    slug = models.SlugField(max_length=70, db_index=True, unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    image = models.ImageField(upload_to='products', blank=True)
    description = models.TextField(max_length=1000, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)

    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title


