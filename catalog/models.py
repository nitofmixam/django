from django.db import models
from users.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=50, verbose_name="Название категории", help_text="Введите строку названия категории"
    )
    description = models.TextField(verbose_name="Описание категории", help_text="Введите описание категории",
                                   blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("id",)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название товара", help_text="Введите строку названия товара")
    description = models.TextField(verbose_name="Описание товара", help_text="Введите описание товара", blank=True,
                                   null=True)
    image_preview = models.ImageField(
        upload_to="products/photo",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фото товара",
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categories", blank=True, null=True)
    price = models.FloatField(verbose_name="Стоимость товара", help_text="Введите строку стоимости товара",
                              blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Владелец', null=True, blank=True)
    public = models.BooleanField(default=False, verbose_name='Признак публикации')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ("name",)
        permissions = [
            (
                "delete_public_product", "Can disable product"
            ),
            (
                "change_product_description", "Can change product description"
            ),
            (
                "change_product_category", "Can change product category"
            ),
        ]


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="versions", )
    version_number = models.CharField(max_length=100, verbose_name="Номер версии", blank=True, null=True)
    version_name = models.CharField(max_length=100, verbose_name='Название версии', help_text='Введите название версии',
                                    blank=True, null=True)
    is_active = models.BooleanField(verbose_name='Признак текущей версии', help_text='Активно?')

    def __str__(self):
        return f"Product - {self.product}, Version - {self.version_number}"

    class Meta:
        verbose_name = "Версия продукта"
        verbose_name_plural = "Версии продуктов"
        ordering = ("product",)
