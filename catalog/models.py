from django.db import models

NULLABEL = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABEL)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)  # сортировка по данному параметру

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABEL)
    preview = models.ImageField(upload_to='products_foto', verbose_name='Изображение',
                                **NULLABEL)  # blank=True. null=True

    category = models.ForeignKey(Category, related_name='products', on_delete=models.SET_NULL, null=True)
    price = models.IntegerField(verbose_name='Цена')
    date_of_creation = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    last_modified_date = models.DateField(auto_now=True, verbose_name='Дата изменения')

    # manufactured_at = models.DateField(auto_now=True, verbose_name='Дата производства', **NULLABEL)

    # Необходимо для отображения модели на русскорм языке в административной панели
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)  # сортировка по данному параметру. В кортежах и списках ставим запятую в конце!!!

    def __str__(self):
        return self.name
