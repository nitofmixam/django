from django.db import models, connection
from django.db.models import IntegerField
from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', help_text='Введите наименование товара')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    @classmethod
    def truncate_table_restart_id(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', help_text='Введите наименование товара',
                            null=True, blank=True, default=None)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    image = models.ImageField(upload_to='product/photo', verbose_name='Изображение', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = IntegerField(verbose_name='Цена ')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='Дата последнего изменения')
    owner = models.ForeignKey(User, verbose_name='Влааделец', null=True, blank=True, on_delete=models.SET_NULL)
    publication = models.BooleanField(verbose_name='Опубликовано', null=True, blank=True)

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ["category", "name"]
        permissions = [
            ("can_canceled_public", "может отменять публикацию продукта"),
            ("can_edit_category ", "может менять описание любого продукта"),
            ("can_edit_desk", "может менять категорию любого продукта")
        ]

    def __str__(self):
        return self.name


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.IntegerField(verbose_name='Номер версии', null=True, blank=True)
    version_name = models.CharField(max_length=100, verbose_name='Название версии', null=True, blank=True)
    is_active = models.BooleanField(default=False, verbose_name='признак текущей версии')

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'

    def __str__(self):
        return self.version_name
