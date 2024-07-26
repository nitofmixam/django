from django.db import models

from users.models import User


# Create your models here.
NULLABLE = dict(blank=True, null=False)


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название', help_text='Введите название')
    slug = models.CharField(max_length=150, unique=True, verbose_name='Slug', blank=True, null=True,)
    body = models.TextField(verbose_name='Содержимое', help_text='Введите содержимое', blank=True, max_length=100)
    image_preview = models.ImageField(
        upload_to="blog/photo",
        blank=True,
        null=True,
        verbose_name="Изображение")
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', blank=True, null=True)
    is_public = models.BooleanField(default=True, verbose_name='Публикация')
    count_view = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Владелец', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ("pk", )