from django.db import models, connection

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    image_preview = models.ImageField(upload_to='catalog/', verbose_name='Изображение (превью)', **NULLABLE)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, verbose_name='Категория', **NULLABLE,
                                 related_name='products')
    price = models.IntegerField(verbose_name='Цена за покупку')
    created_at = models.DateField(**NULLABLE, verbose_name='Дата создания (записи в БД)')
    updated_ad = models.DateField(**NULLABLE, verbose_name='Дата последнего изменения (записи в БД)')

    view_counter = models.PositiveIntegerField(
        verbose_name='Количество просмотров',
        help_text='Количество просмотров данного товара',
        default=0
    )

    def __str__(self):
        return f'{self.product_name} {self.price} {self.category}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = (
            "price",
            "category",
            "created_at",
            "updated_ad",
        )


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.category_name

    @classmethod
    def truncate_table_restart_id(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE')
            #
            # cursor.execute(f"ALTER SEQUENCE catalog_category_id_seq RESTART WITH 1")
            # cursor.execute(f"ALTER SEQUENCE catalog_product_id_seq RESTART WITH 1")

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'