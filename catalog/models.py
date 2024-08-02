from django.db import models

from users.models import User

# Create your models here.

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.CharField(**NULLABLE, verbose_name='Описание')
    image = models.ImageField(upload_to='product/', **NULLABLE, verbose_name='Изображение (превью)')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', blank=True, null=True)
    price = models.IntegerField(verbose_name='цена', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True, **NULLABLE, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, **NULLABLE, verbose_name='Дата последнего изменения')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return f'{self.name} {self.description} {self.category} {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукт'
        ordering = ('name',)
        permissions = [
            (
                'set_published',
                'Can publish product'
            ),
            (
                'change_description',
                'Can change description'
            ),
            (
                'change_category',
                'Can change category'
            )
        ]


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.CharField(max_length=50, verbose_name='Номер версии', **NULLABLE)
    version_name = models.CharField(max_length=50, verbose_name='Название версии', blank=True, null=True)
    is_active = models.BooleanField(verbose_name='Признак текущей версии', default=False)

    def __str__(self):
        return f'{self.version_number} - {self.version_name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'